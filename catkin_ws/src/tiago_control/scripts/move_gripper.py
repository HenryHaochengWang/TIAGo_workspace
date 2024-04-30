#!/usr/bin/env python3
import rospy
from control_msgs.msg import GripperCommandAction, GripperCommandGoal
import actionlib

def move_gripper(position):
    rospy.init_node('gripper_controller')

    client = actionlib.SimpleActionClient('gripper_controller/gripper_cmd', GripperCommandAction)
    client.wait_for_server()

    goal = GripperCommandGoal()
    goal.command.position = position 
    goal.command.max_effort = -1.0 

    client.send_goal(goal)
    client.wait_for_result()

    return client.get_result()

if __name__ == '__main__':
    target_position = 0.04 
    result = move_gripper(target_position)
    print("Gripper moved to position: {}".format(target_position))
