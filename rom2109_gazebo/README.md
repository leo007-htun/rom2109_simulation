#### rom2109 Autonomous Mobile Robot

###### to install

$ sudo apt install ros-foxy-gazebo-ros*

$ sudo apt install ros-foxy-gazebo*

$ echo "source /usr/share/gazebo/setup.sh" >> ~/.bashrc

// export GAZEBO_MODEL_PATH=${GAZEBO_MODEL_PATH}:~/ROS2/workspace/src/rom2109/rom2109_description/meshes/bot/ 
// export GAZEBO_RESOURCE_PATH=${GAZEBO_RESOURCE_PATH}

- gazebo အလုပ်မလုပ်, rviz မှာ robot model ပေါ်ပါတယ်။

နောက်ဆုံး စမ်းသပ်ချက်
- bot urdf ထဲမှာ "package://" ကို "model://" နဲ့ အစားထိုးတဲ့အခါ  gazebo အလုပ်လုပ်တယ်။
- Gazebo ပွင့်လာပေမဲ့ robot မရောက်သေး rviz တွင် robot မပြနိုင်တော့ပေ။