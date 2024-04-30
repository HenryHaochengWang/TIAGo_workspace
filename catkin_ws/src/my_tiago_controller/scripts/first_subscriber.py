#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import LaserScan

def laser_callback(msg):
    front_distance = msg.ranges[len(msg.ranges)//2]
    rospy.loginfo("Front distance: %f", front_distance)


if __name__ == '__main__':
    rospy.init_node("first_subscriber")
    rospy.loginfo("Node has been started")
    
    sub = rospy.Subscriber("/scan_front_raw", LaserScan, callback=laser_callback, queue_size=10)
    
    rospy.spin()