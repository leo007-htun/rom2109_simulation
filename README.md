## rom2109 Autonomous Mobile Robot ( Start Project - Sepetmber 2021)
## Install ပြုလုပ်ရန် 
model install လုပ်ရန် 
```
./install_models
```
install လုပ်နေစဥ် ros2 workspace dir ကိုမေးပါမယ်။ path ကို ထည့်ပေးပါ။ ( ဥပမာ /home/yourName/pathToWorkspace )

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
rom2109_tall ကို ကိုပြည့်စုံအောင် design ဆွဲပြီး rom2109_bot ကို ကိုစည်သူရဲထွန်း design ဆွဲသည်။

<br><br>
#### Menu
<a href="https://github.com/ROM-robotics/rom2109_simulation/tree/humble-slam/rom2109_description"> 1)  Robot ရွေးချယ်ရန် </a><br><br>
<a href="https://github.com/ROM-robotics/rom2109_simulation/tree/humble-slam/rom2109_gazebo"> 2)  Simulation ပြုလုပ်ရန်</a> <br><br>
<a href="https://github.com/ROM-robotics/rom2109_simulation/tree/humble-slam/rom_robotics_joy"> 3)  Control with Joystick </a> <br><br>
<a href="https://github.com/ROM-robotics/rom2109_simulation/tree/humble-slam/rom2109_nav2"> 4)  Navigation ပြုလုပ်ရန်</a> <br><br>
<a href="https://github.com/ROM-robotics/rom2109_simulation/tree/humble-slam/rom2109_autonomy"> 5)  Patrol လှည့်ရန် </a><br>

