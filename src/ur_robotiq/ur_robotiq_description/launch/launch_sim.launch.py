import os

import launch_ros
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node

import launch
from launch import LaunchDescription, conditions
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration


def generate_launch_description():

    # Include the robot_state_publisher launch file, provided by our own package. Force sim time to be enabled
    # !!! MAKE SURE YOU SET THE PACKAGE NAME CORRECTLY !!!

    package_name='ur_robotiq_description' #<--- CHANGE ME
    rviz_world = [os.path.join(package_name, 'Rviz', 'Default.rviz')]
    rsp_launch = os.path.join(get_package_share_directory('ur_description'),'launch','view_ur.launch.py')
    ur3_launch = os.path.join(get_package_share_directory(package_name),'launch','rsp.launch.py')
    
    rsp = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([rsp_launch]), 
                launch_arguments={'use_sim_time': 'true'}.items()
    )
    
    ur3e = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([ur3_launch]), 
                launch_arguments={'ur_type': 'ur3e'}.items()
    )
    

    # Launch them all!
    return LaunchDescription([
        # rsp,
        ur3e,
        # Rviz,
        DeclareLaunchArgument(name='use_sim_time', default_value='True', description='Flag to enable use_sim_time'),
    ])