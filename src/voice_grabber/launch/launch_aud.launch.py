from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
  return LaunchDescription([
    Node(
      package='voice_grabber',  # package name
      executable='Speech_Listner_Node',  # node executable name
    )
  ])
