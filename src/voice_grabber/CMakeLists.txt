cmake_minimum_required(VERSION 3.8)
project(voice_grabber)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

list(APPEND CMAKE_PREFIX_PATH /usr/local/lib/portaudio/)
# list(APPEND CMAKE_PREFIX_PATH /home/fiend/.local/lib/python3.10/site-packages)

# find dependencies
find_package(rclcpp REQUIRED)
find_package(rclpy REQUIRED)
find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(std_msgs)  
find_package(sensor_msgs)
find_package(audio_common_msgs REQUIRED)
find_package(portaudio REQUIRED)
find_package(PythonInterp REQUIRED)

# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)
include_directories(include)
include_directories("${PROJECT_SOURCE_DIR}")
include_directories(${PORTAUDIO_INCLUDE_DIRS})

# C++ executables
set(SOURCES2 /home/fiend/voice_grab/ros2_ws/src/voice_grabber/src/SpeechListner.cpp)
set(SOURCES3 /home/fiend/voice_grab/ros2_ws/src/voice_grabber/src/TextDisplay.cpp)

add_executable(Speech_Listner_Node ${SOURCES2})
ament_target_dependencies(Speech_Listner_Node rclcpp std_msgs sensor_msgs audio_common_msgs)
target_include_directories(Speech_Listner_Node PRIVATE /opt/portaudio/src/common/)
target_link_libraries(Speech_Listner_Node portaudio)

add_executable(Text_Display_Node ${SOURCES3})
ament_target_dependencies(Text_Display_Node rclcpp std_msgs sensor_msgs audio_common_msgs)
target_link_libraries(Text_Display_Node)

install(DIRECTORY 
    launch
    DESTINATION share/${PROJECT_NAME}
)

install(TARGETS
    Speech_Listner_Node Text_Display_Node
    DESTINATION lib/${PROJECT_NAME}
)

# Python Executables
ament_python_install_package(${PROJECT_NAME})

install(PROGRAMS
    py_scripts/Vosk.py
    DESTINATION lib/${PROJECT_NAME}
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
