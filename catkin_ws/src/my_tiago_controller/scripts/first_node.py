#!/usr/bin/env python3
import rospy


if __name__ == '__main__':
    rospy.init_node('test_node') # name shown in rqt_graph & rosnode list
    rospy.loginfo('test_node has started')
    rospy.logwarn('This is a warning')
    rospy.logerr('This is an error')
    
    rospy.sleep(1.0)
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        rospy.loginfo("Hello")
        rate.sleep()
    
    rospy.loginfo('test_node has stopped')