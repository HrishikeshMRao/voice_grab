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
find_package(moveit_task_constructor_core REQUIRED)
find_package(std_msgs)  
find_package(sensor_msgs)
find_package(audio_common_msgs REQUIRED)
find_package(PythonInterp REQUIRED)

# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)
include_directories(include)
include_directories("${PROJECT_SOURCE_DIR}")
include_directories(${PORTAUDIO_INCLUDE_DIRS})

add_executable(mtc_node src/mtc_node.cpp)
target_include_directories(mtc_node PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include>)
target_compile_features(mtc_node PUBLIC c_std_99 cxx_std_17)  # Require C99 and C++17
ament_target_dependencies(
  mtc_node
  "moveit_task_constructor_core"
  "rclcpp"
)

# Python Executables
ament_python_install_package(${PROJECT_NAME})

install(TARGETS mtc_node
  DESTINATION lib/${PROJECT_NAME})

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

install(DIRECTORY 
    launch
    DESTINATION share/${PROJECT_NAME}
)

ament_package()
