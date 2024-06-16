import os

from ament_index_python import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from moveit_configs_utils import MoveItConfigsBuilder


def generate_launch_description():
    moveit_config = (MoveItConfigsBuilder("ur").to_moveit_configs())
    mtc = Node(
        package="voice_grabber",
        executable="mtc_node",
        output="screen",
        parameters=[
            moveit_config.to_dict(),
        ],
    )
    return LaunchDescription([mtc])