#!/usr/bin/env python3

# MIT License
#
# Copyright (c) 2023 ROM ROBOTICS
import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command, LaunchConfiguration, PathJoinSubstitution
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node 

def generate_launch_description():
    gazebo_package = get_package_share_directory('gazebo_ros')
    rom_gazebo_package = get_package_share_directory('rom2109_gazebo')
    #bringup_package = get_package_share_directory('mini_pupper_bringup')
    #description_package = get_package_share_directory('mini_pupper_description')

    # description_path = os.path.join(description_package, 'urdf', 'mini_pupper_description.urdf.xacro')
    # bringup_launch_path = os.path.join(bringup_package, 'launch', 'bringup.launch.py')
    default_world_path = os.path.join(rom_gazebo_package, 'worlds', 'rom2109.world')

    robot_name = LaunchConfiguration("robot_name")
    sim = LaunchConfiguration("sim")
    #hardware_connected = LaunchConfiguration("hardware_connected")
    rviz = LaunchConfiguration("rviz")
    lite = LaunchConfiguration("lite")
    world = LaunchConfiguration("world"),
    world_init_x = LaunchConfiguration("world_init_x"),
    world_init_y = LaunchConfiguration("world_init_y"),
    world_init_z = LaunchConfiguration("world_init_z"),
    world_init_heading = LaunchConfiguration("world_init_heading"),
    gui = LaunchConfiguration("gui"),

    declare_rviz = DeclareLaunchArgument(
        name="rviz",
        default_value="false",
        description="Launch rviz"
    )
    declare_robot_name = DeclareLaunchArgument(
        name="robot_name",
        default_value="rom2109",
        description="Robot name"
    )
    declare_lite = DeclareLaunchArgument(
        name="lite",
        default_value="false",
        description="Lite"
    )
    declare_world = DeclareLaunchArgument(
        name="world",
        default_value=default_world_path,
        description="Gazebo world path"
    )
    declare_gui = DeclareLaunchArgument(
        name="gui",
        default_value="true",
        description="Use gui"
    )
    declare_world_init_x = DeclareLaunchArgument(
        name="world_init_x",
        default_value="0.0"
    )
    declare_world_init_y = DeclareLaunchArgument(
        name="world_init_y",
        default_value="0.0"
    )
    declare_world_init_z = DeclareLaunchArgument(
        name="world_init_z",
        default_value="0.0"
    )
    declare_world_init_heading = DeclareLaunchArgument(
        name="world_init_heading",
        default_value="0.0"
    )
    declare_sim = DeclareLaunchArgument(
        name='sim',
        default_value='true',
        description='Enable use_sime_time to true'
    )

    # mini_pupper_bringup_launch = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource(bringup_launch_path),
    #     launch_arguments={
    #         "use_sim_time": sim,
    #         "robot_name": robot_name,
    #         "gazebo": sim,
    #         "rviz": rviz,
    #         "hardware_connected": hardware_connected,
    #         "publish_foot_contacts": "true",
    #         "close_loop_odom": "true",
    #         "joint_controller_topic": "joint_group_effort_controller/joint_trajectory",
    #         "joints_map_path": joints_config_path,
    #         "links_map_path": links_config_path,
    #         "gait_config_path": gait_config_path,
    #         "description_path": description_path,
    #         "ros_control_file": ros_control_config_path
    #     }.items(),
    # )
    # champ_gazebo_launch = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource(os.path.join(
    #         get_package_share_directory("champ_gazebo"), "launch", "gazebo.launch.py")),
    #     launch_arguments={
    #         "use_sim_time": sim,
    #         "robot_name": robot_name,
    #         "world": world,
    #         "lite": lite,
    #         "world_init_x": world_init_x,
    #         "world_init_y": world_init_y,
    #         "world_init_heading": world_init_heading,
    #         "gui": gui,
    #         "close_loop_odom": "true",
    #     }.items(),
    # )

    gazebo_launch = IncludeLaunchDescription(PythonLaunchDescriptionSource(os.path.join(gazebo_package, 'launch', 'gazebo.launch.py')))

    start_gazebo_spawner_cmd = Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        output="screen",
        arguments=[
            "-entity",
            robot_name,
            "-topic",
            "/robot_description",
            "-robot_namespace",
            "rom",
            "-x",
            world_init_x,
            "-y",
            world_init_y,
            "-z",
            world_init_z,
            "-R",
            "0",
            "-P",
            "0",
            "-Y",
            world_init_heading,
        ],
    )

    return LaunchDescription([
        #declare_rviz,
        declare_robot_name,
        #declare_lite,
        declare_world,
        declare_gui,
        declare_world_init_x,
        declare_world_init_y,
        declare_world_init_z,
        declare_world_init_heading,
        declare_sim,
        gazebo_launch,
        start_gazebo_spawner_cmd,
    ])
