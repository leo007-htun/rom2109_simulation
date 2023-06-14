### rom2109_autonomy

clone to your ROS2 workspace<br>
```
$ git clone git@github.com:BehaviorTree/BehaviorTree.CPP.git <br>
$ colcon build <br>

$ros2 pkg create test --build--type ament_cmake --dependencies behaviortree_cpp rclcpp <br>
$ colcon build
```

### 4 Patrol System 
Partol လှည့်ရန်။
```
ros2 launch rom2109_gazebo rom2109_sim_ros2_control.launch.py
ros2 launch rom2109_gazebo controller_spawner.launch.py
ros2 launch rom2109_nav2 sim_localization_init_pose_launch.py
ros2 launch rom2109_nav2 sim_navigation_launch.py map_subscribe_transient_local:=true
ros2 launch rom2109_autonomy autonomy.launch.py
```




<a href="https://github.com/ROM-robotics/rom2109">မူလစာမျက်နှာ </a>