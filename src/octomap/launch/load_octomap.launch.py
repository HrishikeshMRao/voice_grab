
import os

from ament_index_python import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    params_file = os.path.join(get_package_share_directory("octomap"), "config", "octomap_params.yaml")
    octomap_talker = Node(
        package="octomap_server",
        executable="octomap_server_node",
        output="screen",
        parameters=[params_file],
    )
    moveit_octomap_handler = Node(
        package="octomap",
        executable="octoload.py",
        output="screen",
    )
    return LaunchDescription([
        octomap_talker,
        moveit_octomap_handler
    ]) 