# Copyright 2023 ROM Robotics
import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument

rom_robot = ['rom2109_tall.urdf', 'rom2109_short.urdf', 'rom2109_bot.urdf']
robot_name_in_model = 'rom2109'

def generate_launch_description():
    gazebo_ros_pkg = get_package_share_directory('gazebo_ros')
    rom2109_gazebo_pkg = get_package_share_directory('rom2109_gazebo')

    urdf_pkg = get_package_share_directory('rom2109_description')
    urdf_path= os.path.join(urdf_pkg, 'urdf', rom_robot[0])
    urdf = open(urdf_path).read()

    # Pose
    x_position = '0.0'
    y_position = '0.0'
    z_position = '0.0'
    yaw = '0.0000'

    # Arguments
    use_jointState = LaunchConfiguration('use_jointState')
    
    gazebo_launch = IncludeLaunchDescription(PythonLaunchDescriptionSource(os.path.join(gazebo_ros_pkg, 'launch', 'gazebo.launch.py')))
    
    spawn_node = Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        arguments=['-entity', robot_name_in_model,
        '-file', urdf_path,
        '-x', x_position,
        '-y', y_position,
        '-z', z_position,
        '-Y', yaw,
        '-package_to_model'],
        output="screen"
    )

    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        arguments=['-d', os.path.join(rom2109_gazebo_pkg, 'rviz2', 'gazebo.rviz' )],
        condition=IfCondition(LaunchConfiguration('use_rviz'))
    )

    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[{'robot_description': urdf}],
    )

    joint_state_publisher_node = Node(
        package="joint_state_publisher",
        executable="joint_state_publisher",
        name="joint_state_publisher",
        condition=IfCondition(use_jointState),
    )
    # first focus on spawn, second sensor and rviz
    return LaunchDescription(
        [
            DeclareLaunchArgument('use_jointState', default_value='True', description="Enable joint_state_publisher"),
            DeclareLaunchArgument('world', default_value=[os.path.join(rom2109_gazebo_pkg, 'worlds','rom2109_empty.world'), ''], description='SDF world file'),
            DeclareLaunchArgument('use_rviz', default_value='false', description='Open RViz.'),
            DeclareLaunchArgument('urdf_model', default_value=urdf_path, description='Absolute path to robot urdf file'),
            robot_state_publisher_node,
            gazebo_launch,
            spawn_node,
        ]
    )