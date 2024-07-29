set(_AMENT_PACKAGE_NAME "octomap")
set(octomap_VERSION "2.1.5")
set(octomap_MAINTAINER "Hrishikesh M Rao <mraohrishikesh@gmail.com>")
set(octomap_BUILD_DEPENDS "rclpy" "moveit_task_constructor_core")
set(octomap_BUILDTOOL_DEPENDS "ament_cmake" "ament_cmake_python")
set(octomap_BUILD_EXPORT_DEPENDS "rclpy" "moveit_task_constructor_core")
set(octomap_BUILDTOOL_EXPORT_DEPENDS )
set(octomap_EXEC_DEPENDS "launch" "launch_ros" "rclpy" "moveit_task_constructor_core")
set(octomap_TEST_DEPENDS "ament_cmake_pytest")
set(octomap_GROUP_DEPENDS )
set(octomap_MEMBER_OF_GROUPS )
set(octomap_DEPRECATED "")
set(octomap_EXPORT_TAGS)
list(APPEND octomap_EXPORT_TAGS "<build_type>ament_cmake</build_type>")