from launch import LaunchDescription
from launch_ros.actions import Node

import os

from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    joy_params = os.path.join(get_package_share_directory('rom_robotics_joy'), 'config', 'joystick.yaml')

    joy_node = Node(
        package='joy',
        executable='joy_node',
        parameters=[joy_params],
    )
    test_node = Node(
        package='joy_tester',
        executable='test_joy',
        name='test_joy'
    )

    return LaunchDescription([
        joy_node,
        test_node,
    ])