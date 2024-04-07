# ROS_TIAGo_Learning

## 1. Launching simulation

`roslaunch tiago_gazebo tiago_gazebo.launch public_sim:=true end_effector:=pal-gripper world:=empty`

## 2. Sending velocity commands through command line

This section shows how to command the differential drive base of TIAGo through ROS topics.

### 2.1 Moving forward and backward

In the second console run the following instruction which will publish a constant linear velocity of 0.5 m/s along the X axis, i.e. the axis of the robot pointing forward

```
rostopic pub /mobile_base_controller/cmd_vel geometry_msgs/Twist "linear:
  x: 0.5
  y: 0.0
  z: 0.0
angular:
  x: 0.0
  y: 0.0
  z: 0.0" -r 3
```
or 
```
rostopic pub /mobile_base_controller/cmd_vel geometry_msgs/Twist -r 3 -- '[0.5,0.0,0.0]' '[0.0, 0.0, 0.0]'
```