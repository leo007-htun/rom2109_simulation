## rom2109 Autonomous Mobile Robot ( Start Project - Sepetmber 2021)
model install လုပ်ရန် ./install_models

#### Install ပြုလုပ်ခြင်း ( Simulation Robot ) 
```
sudo apt install -y ros-humble-gazebo-ros* 
sudo apt install -y ros-humble-ros2-control*
sudo apt install -y ros-humble-controller-*
cd your/workspace/src
git clone git@github.com:ROM-robotics/rom2109_simulation.git
cd your/workspace && colcon build --symlink-install && source install/setup.bash
```
<img src="images/orange_bot.png" width="619" height="330" />
rom2109_tall ကို ကိုပြည့်စုံအောင် design ဆွဲပြီး rom2109_bot ကို ကိုစည်သူရဲထွန်း design ဆွဲပြီး မြန်မာပြည်တွင် တပ်ဆင်သည်။

#### Simulation  ပြုလုပ်ရန်
ros2 launch rom2109_gazebo rom2109_sim_gz_control.launch.py use_sim_time:=true
