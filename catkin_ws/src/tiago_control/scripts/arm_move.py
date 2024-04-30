#!/usr/bin/env python3
import sys
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

class ArmMover:
    def __init__(self):
        moveit_commander.roscpp_initialize(sys.argv)
        rospy.init_node('tiago_arm_mover')

        self.robot = moveit_commander.RobotCommander()
        self.scene = moveit_commander.PlanningSceneInterface()
        self.group = moveit_commander.MoveGroupCommander("arm")

    def move_to_pose(self, pose, orientation):
        pose_target = geometry_msgs.msg.Pose()

        pose_target.position.x = pose['x']
        pose_target.position.y = pose['y']
        pose_target.position.z = pose['z']

        pose_target.orientation.x = orientation['x']
        pose_target.orientation.y = orientation['y']
        pose_target.orientation.z = orientation['z']
        pose_target.orientation.w = orientation['w']

        self.group.set_pose_target(pose_target)

        plan = self.group.plan()
        self.group.go(wait=True)

        self.group.stop()
        self.group.clear_pose_targets()
    
    def shutdown(self):
        moveit_commander.roscpp_shutdown()


if __name__ == '__main__':
    mover = ArmMover()
    try:
        pose = {'x': 0.3, 'y': 0.3, 'z': 0.3}
        orientation = {'x': 0.0, 'y': 0.0, 'z': 0.0, 'w': 1.0}
        mover.move_to_pose(pose, orientation)
    except rospy.ROSInterruptException:
        pass
    finally:
        mover.shutdown()