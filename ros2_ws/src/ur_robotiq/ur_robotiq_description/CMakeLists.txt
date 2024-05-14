cmake_minimum_required(VERSION 3.8)
project(ur_robotiq_description)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# list(APPEND CMAKE_PREFIX_PATH /opt/ros/humble/include/)

# Locate and configure packages required by the project.
find_package(ament_cmake REQUIRED)
find_package(robotiq_description REQUIRED)
find_package(ur_description REQUIRED)
find_package(rclcpp REQUIRED)
# find_package(moveit REQUIRED)
# find_package(moveit_core REQUIRED) 
find_package(moveit_ros_planning_interface REQUIRED)
find_package(moveit_ros_move_group REQUIRED) 

set(SOURCES1 /home/fiend/voice_grab/ros2_ws/src/ur_robotiq/ur_robotiq_description/src/MoveTheArm.cpp)
add_executable(Move ${SOURCES1})
ament_target_dependencies(Move rclcpp moveit_ros_planning_interface moveit_ros_move_group)
target_link_libraries(Move)

# Copy necessary files to designated locations in the project
install(TARGETS
    Move 
    DESTINATION lib/${PROJECT_NAME})
install (DIRECTORY 
    urdf launch 
    DESTINATION share/${PROJECT_NAME})
install(DIRECTORY 
    urdf/meshes
    DESTINATION share/${PROJECT_NAME}/urdf
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
