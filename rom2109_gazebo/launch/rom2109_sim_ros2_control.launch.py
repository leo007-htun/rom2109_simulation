#!/usr/bin/env python3
import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument, ExecuteProcess, IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource

import xacro

def generate_launch_description():
    gazebo_pkg = get_package_share_directory('rom2109_gazebo')
    description_pkg = get_package_share_directory('rom2109_description')
    default_world_path = os.path.join(gazebo_pkg, 'worlds', 'cafe.world')

    urdf_file = os.path.join(description_pkg,'urdf', 'urdf.urdf')
    # robot_description_config = xacro.process_file(xacro_file)
    # my_xml = robot_description_config.toxml()

    bot = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            description_pkg, 'launch', 'description_ros2_control.launch.py'
        )]), launch_arguments={'use_sim_time': 'true'}.items()
    )

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        arguments=['-d', os.path.join(gazebo_pkg, 'rviz2', 'display.rviz')],
        condition=IfCondition(LaunchConfiguration('open_rviz'))
    )

    gazebo_params_file = os.path.join(get_package_share_directory(
        'rom2109_gazebo'), 'config', 'gazebo_params.yaml')

    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(
            get_package_share_directory("gazebo_ros"), "launch", "gazebo.launch.py")),
        launch_arguments={
            "use_sim_time": "true",
            "robot_name": "rom2109",
            "world": default_world_path,
            "lite": "false",
            "world_init_x": "0.0",
            "world_init_y": "0.0",
            "world_init_heading": "0.0",
            "gui": "true",
            "close_loop_odom": "true",
            "extra_gazebo_args": "--ros-args --params-file " + gazebo_params_file
        }.items(),
    )

    spawn_robot_node = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        # arguments=['-database', 'rom2109_tall_ros', '-entity', 'rom2109_tall_ros',
        arguments=['-file', urdf_file, '-entity', 'rom2109_tall_ros',
                   "-x", '0.0',
                   "-y", '0.0',
                   "-z", '0.3'],
        output='screen'
    )

    diff_drive_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["diff_cont"],
    )

    joint_broad_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["joint_broad"],
    )

    
    joy_params = os.path.join(get_package_share_directory('rom_robotics_joy'), 'config', 'joystick.yaml')

    joy_node = Node(
        package='joy',
        executable='joy_node',
        parameters=[joy_params,{'use_sim_time': 'true'}],
    )
    teleop_node = Node(
        package="teleop_twist_joy",
        executable='teleop_node',
        name='teleop_node',
        parameters=[joy_params,{'use_sim_time': 'true'}],
        remappings=[('/cmd_vel', '/cmd_vel_joy')]
    )

    return LaunchDescription(
        [
            DeclareLaunchArgument('open_rviz', default_value='true', description='Open RViz.'),
            DeclareLaunchArgument('use_joystick', default_value='false', description='JoyStick.'),
            DeclareLaunchArgument('use_sim_time', default_value='true', description='Sim Time'),
            bot,
            gazebo_launch,
            rviz_node,
            spawn_robot_node,
            #diff_drive_spawner,
            #joint_broad_spawner,
            
        ]
    )
