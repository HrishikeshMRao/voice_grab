import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import (Command, FindExecutable, LaunchConfiguration,
                                  PathJoinSubstitution)
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    declared_arguments = []
    # UR specific arguments
    declared_arguments.append(
        DeclareLaunchArgument(
            "ur_type",
            description="Type/series of used UR robot.",
            choices=["ur3", "ur3e", "ur5", "ur5e", "ur10", "ur10e", "ur16e", "ur20", "ur30"],
        )
    )

    # General arguments
    declared_arguments.append(
        DeclareLaunchArgument(
            "description_package",
            default_value="ur_description",
            description="Description package with robot URDF/XACRO files. Usually the argument "
            "is not set, it enables use of a custom description.",
        )
    )

    # General arguments
    description_package = LaunchConfiguration("description_package")

    world = PathJoinSubstitution(
        [FindPackageShare(description_package), "world", "empty.world"]
    )

    # Include the Gazebo launch file, provided by the gazebo_ros package
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory("gazebo_ros"), "launch", "gazebo.launch.py")
        ),
        launch_arguments={"verbose": "false",
                          "world":world}.items(),
    )

    # Run the spawner node from the gazebo_ros package. The entity name doesn't really matter if you only have a single robot.
    spawn_entity = Node(package='gazebo_ros', 
                        executable='spawn_entity.py',
                        arguments=['-topic', 'robot_description', '-entity', 'arm'],
                        output='screen')
    
    nodes_to_start = [
        gazebo,
        spawn_entity,     
    ]

    return LaunchDescription(declared_arguments + nodes_to_start)
