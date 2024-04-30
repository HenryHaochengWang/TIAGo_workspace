#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan


def turn90left():
    pub = rospy.Publisher("/mobile_base_controller/cmd_vel", Twist, queue_size=10)
    

if __name__ =='__main__':
    rospy.init_node("run_circle")
    rospy.loginfo("Node has been started")

    pub = rospy.Publisher("/mobile_base_controller/cmd_vel", Twist, queue_size=10)

    rate = rospy.Rate(2)

    # limit running time in 10 seconds
    start_time = rospy.Time.now()

    while not rospy.is_shutdown() and rospy.Time.now() - start_time < rospy.Duration(50):
        rospy.loginfo("Publishing cmd_vel message")
        # publish cmd_vel message
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = -3.0
        pub.publish(msg)
        rate.sleep()


    rospy.loginfo("Stopping the robot")
    msg = Twist()
    msg.linear.x = 0.0
    msg.angular.z = 0.0
    pub.publish(msg)

    rospy.loginfo("Node has been stopped")
