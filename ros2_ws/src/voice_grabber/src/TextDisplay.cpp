#include <rclcpp/rclcpp.hpp>
#include <ncurses.h>

class TextDisplay : public rclcpp::Node {
public:
    TextDisplay() : Node("Text_Display_Node") {
        // subscription_ = create_subscription<RecognizedText>("recognized_text", 10, std::bind(&TextDisplayNode::text_callback, this, std::placeholders::_1));
        // // Initialize ncurses
        // initscr();
    }

private:
    // rclcpp::Subscription<RecognizedText>::SharedPtr subscription_;
};

int main(int argc, char **argv) {
    // rclcpp::init(argc, argv);
    // rclcpp::spin(std::make_shared<WebcamPublisher>());
    // rclcpp::shutdown();
    return 0;
}