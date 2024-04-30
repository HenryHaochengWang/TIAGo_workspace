#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist


class BaseController:
    def __init__(self):
        rospy.init_node("base_controller")
        
        self.base_pub = rospy.Publisher("/mobile_base_controller/cmd_vel", Twist, queue_size=10)
        rospy.Subscriber("/cmd_vel", Twist, callback=self.callback, queue_size=10)

    def callback(self, msg):
        self.base_pub.publish(msg)

    def run(self):
        rospy.spin()
    

if __name__ == '__main__':
    base_ctrl = BaseController()
    base_ctrl.run()