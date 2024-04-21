#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

if __name__ =='__main__':
    rospy.init_node("run_circle")
    rospy.loginfo("Node has been started")

    pub = rospy.Publisher("/mobile_base_controller/cmd_vel", Twist, queue_size=10)

    rate = rospy.Rate(2)

    # limit running time in 10 seconds
    start_time = rospy.Time.now()

    while not (rospy.is_shutdown() and rospy.Time.now() - start_time < rospy.Duration(100)):
        # publish cmd_vel message
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 1.0
        pub.publish(msg)
        rate.sleep()
    
    msg = Twist()
    msg.linear.x = 0.0
    msg.angular.z = 0.0
    pub.publish(msg)

    rospy.loginfo("Node has been stopped")