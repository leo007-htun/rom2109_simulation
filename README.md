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
ပုံမှန်အားဖြင့် gazebo ထဲသို့ spawn လုပ်ရာတွင် topic, database, file နည်းလမ်းများဖြင့် လုပ်နိုင်သော်လည်း topic နည်းလမ်းသည်  robot_state_pubisher  မှ လာတာမို့လို့ urdf, xacro, sdf တွေမှာပြသနာရှိနိုင်ပါတယ်။ ဒါကြောင့်  database, file  နည်းလမ်းများကို သုံးထားပါတယ်။

###### (၁) ပုံမှန်  gazebo controller တွေနဲ့ simulation ပြုလုပ်လိုရင်
```
ros2 launch rom2109_gazebo rom2109_sim_gz_control.launch.py use_sim_time:=true
```
###### (၂) gazebo ros2 control  နဲ့ simulation ပြုလုပ်လိုရင်
```
ros2 launch rom2109_gazebo rom2109_sim_ros2_control.launch.py
```
###### (၃) Gazebo မှ တဆင့် simulation
```
ros2 launch gazebo_ros gazebo.launch.py
# insert ကိုနှိပ်ပြီး rom2109_tall or rom2109_tall_ros or rom2109_bot တခုခုထည့်ပါ။
# rom2109_tall_ros သုံးပြီး gazebo ros2 controller manager ကို လိုချင်ရင် 
# rom2109_description package ထဲက description_ros2_control.launch.py ကို 
# launch လုပ်ဖို့လိုအပ်ပါတယ်။
```

