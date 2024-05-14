#include <portaudio.h>
#include <cstring>
#include <audio_common_msgs/msg/audio_data.hpp>
#include <rclcpp/rclcpp.hpp>
#include <memory>

#define SAMPLE_RATE 44100
#define FRAMES_PER_BUFFER 512

using namespace std::chrono_literals;

class SpeechListener : public rclcpp::Node
{
public:
	SpeechListener() : Node("Speech_Listner_Node")
	{
		// Create publisher
		this->publisher_ = create_publisher<audio_common_msgs::msg::AudioData>("audio_data", 10);

		this->err = Pa_Initialize(); // Initialize PortAudio
		check(err);

		startStreaming();

	}

	~SpeechListener()
	{
		// Stop and close stream
		Pa_StopStream(stream);
		Pa_CloseStream(stream);
		Pa_Terminate();
	}

private:
	PaStream* stream;
	PaError err;
	int device; // Fetch the device with name default 
	PaStreamParameters inputParameters;
	PaStreamParameters outputParameters;
	std::shared_ptr<SpeechListener> node;

	audio_common_msgs::msg::AudioData message;

	void startStreaming()
  	{
		int numDevices = Pa_GetDeviceCount();
		this->device = 8; //pulse audio

		const PaDeviceInfo *deviceInfo;
		for (int i = 0; i < numDevices; i++)
		{
			deviceInfo = Pa_GetDeviceInfo(i);
			RCLCPP_INFO(this->get_logger(), "\n%d] Name: %s \n    Input Channels: %d \n    Output Chnnels: %d \n    SampleRate: %f \n ", i+1, deviceInfo->name, deviceInfo->maxInputChannels, deviceInfo->maxOutputChannels, deviceInfo->defaultSampleRate); 
		}

		memset(&this->inputParameters, 0, sizeof(this->inputParameters));
		this->inputParameters.channelCount = 1;
		this->inputParameters.device = device;
		this->inputParameters.hostApiSpecificStreamInfo = NULL;
		this->inputParameters.sampleFormat = paFloat32;
		this->inputParameters.suggestedLatency =Pa_GetDeviceInfo(device)->defaultLowInputLatency;

		memset(&outputParameters, 0, sizeof(outputParameters));
		outputParameters.channelCount = 1;
		outputParameters.device = device;
		outputParameters.hostApiSpecificStreamInfo = NULL;
		outputParameters.sampleFormat = paFloat32;
		outputParameters.suggestedLatency =Pa_GetDeviceInfo(device)->defaultLowOutputLatency;

		// Open audio stream
		PaError err = Pa_OpenStream(&stream,     
					&inputParameters,   // Input channels
					&outputParameters,  // Output channels
					SAMPLE_RATE,        // Sample rate
					FRAMES_PER_BUFFER,  // Frames per buffer
					paNoFlag,           // Sample format
					PaCallback,         // Callback function
					&node);              // userdata   

		check(err);

		// Start streaming
		err = Pa_StartStream(stream);
		check(err);

		Pa_Sleep(10*1000);

		err = Pa_StopStream(stream);
		check(err);

		RCLCPP_INFO(this->get_logger(), "Stream Stopped: %d \n", err);

		err = Pa_CloseStream(stream);
		check(err);

		RCLCPP_INFO(this->get_logger(), "Stream Closed: %d \n", err);

		err = Pa_Terminate();
		check(err);

		RCLCPP_INFO(this->get_logger(), "PortAudio Terminated: %d \n", err);
	}

	static inline float max(float a, float b) {return a>b ? a : b;}

	static int PaCallback(const void *inputBuffer, void *outputBuffer, unsigned long framesPerBuffer, const PaStreamCallbackTimeInfo *timeInfo, PaStreamCallbackFlags statusFlags, void *userData)
	{
		(void) outputBuffer;
		(void) timeInfo;
		(void) statusFlags;

		std::shared_ptr<SpeechListener> node =  std::static_pointer_cast<SpeechListener>(std::shared_ptr<void>(userData, [](void*){}));
		float* in = (float*)inputBuffer;

		for(unsigned long i = 0; i<framesPerBuffer;i++)
		{
			node->message.data.push_back(in[i]);
			node->publisher_->publish(node->message);
		}

		return paContinue;
	}

	void check(PaError err){
		if (err != paNoError)
		{
			RCLCPP_ERROR(this->get_logger(), "Failed: %s", Pa_GetErrorText(err));
			Pa_Terminate();
			rclcpp::shutdown();
			return;
		}
	}

	rclcpp::Publisher<audio_common_msgs::msg::AudioData>::SharedPtr publisher_;
	rclcpp::TimerBase::SharedPtr timer_;
};


int main(int argc, char **argv)
{
	rclcpp::init(argc, argv);
	std::shared_ptr<SpeechListener> node = std::make_shared<SpeechListener>();
	rclcpp::spin(node);
	rclcpp::shutdown();
	return 0;
}