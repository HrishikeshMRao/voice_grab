import os

from ament_index_python import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    
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
            launch_arguments={"ur_type": "ur5e"}.items()
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(MoveGroup_launch_path),
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(octomap_launch_path),
        ),
    ])
