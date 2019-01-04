# Quick setup
```
wget -qO - http://bot.roboy.org:8081/~roboy/dists/stable/main/binary/public.key | sudo apt-key add -
echo "deb ftp://bot.roboy.org/dists/stable/main/binary /" | sudo tee -a /etc/apt/sources.list.d/ros2-latest.list
sudo apt update

sudo apt install ros-kinetic-roboy-msgs ros-bouncy-roboy-msgs ros-bouncy-roboy-ros1-bridge pyroboy

# start service clients
source /opt/ros/kinetic/setup.bash
roslaunch roboy_speech_recognition speech_recognition.launch &
roslaunch speech_synthesis speech_synthesis.launch 

# start ros1_bridge
source /opt/ros/boucny/setup.bash && source /opt/ros/kinetic/setup.bash
ros2 run ros1_bridge dynamic_bridge

# test pyroboy
python3
>>> import pyroboy
>>> pyroboy.say("hello")
>>> pyroboy.listen()
```
