import os

from ament_index_python import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource


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

    declared_arguments.append(
        DeclareLaunchArgument(
            "gripper_type",
            description="Type/series of used UR robot.",
            choices=["85", "140"],
        )
    )

    gazebo_launch_path = os.path.join(
        get_package_share_directory('ur_description'),
        'launch',
        'view_ur.launch.py'
    )
    
    MoveGroup_launch_path = os.path.join(
        get_package_share_directory('ur_moveit_config'),
        'launch',
        'move_group.launch.py'
    )
    
    octomap_launch_path = os.path.join(
        get_package_share_directory('octomap'),
        'launch',
        'load_octomap.launch.py'
    )
    
    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(gazebo_launch_path),
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(MoveGroup_launch_path),
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(octomap_launch_path),
        ),
    ])
