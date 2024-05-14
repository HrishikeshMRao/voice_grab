import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import LaunchConfiguration, Command
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue 

def generate_launch_description():

  use_sim_time = LaunchConfiguration('use_sim_time', default='true')

  xacro_file_name = 'urdf/zed_descr.xacro'
  rviz_file_name = '/home/fiend/voice_grab/ros2_ws/src/ur_robotiq/ur_robotiq_description/Rviz/Default.rviz'
  xacro = os.path.join(get_package_share_directory('ur_robotiq_description'),xacro_file_name)

  robot_description_config = Command(['xacro ', xacro, ' use_ros2_control:=', 'true', ' sim_mode:=', use_sim_time])
  params = {'robot_description': ParameterValue(robot_description_config, value_type=str),'use_sim_time': use_sim_time}
  
  print("urdf_file_name : {}".format(xacro))

  return LaunchDescription([

        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use simulation (Gazebo) clock if true'),

        ExecuteProcess(
            cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_factory.so'],
            output='screen'),

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[params],
        ),

        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            name='urdf_spawner',
            arguments=["-topic", "/robot_description", "-entity", "arm"]
        ),

        Node(
          package='rviz2',
          executable='rviz2',
          name='rviz',
          output='screen'
        )
  ])