#! /usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface_tutorial', anonymous=True)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()    
group = moveit_commander.MoveGroupCommander("arm")
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=1)
rospy.loginfo(f"Create plan for group {group.get_name()}'s end effector link: {group.get_end_effector_link()}")
rospy.loginfo(f"{group.get_planning_frame()=}")
rospy.loginfo(f"{robot.get_group_names()=}")
rospy.loginfo(f"{group.get_current_pose()=}")
rospy.loginfo(f"{robot.get_current_state()=}")

pose_target = geometry_msgs.msg.Pose()
pose_target.orientation.w = 1.0
pose_target.position.x = 0.96
pose_target.position.y = 0
pose_target.position.z = 1.18
group.set_pose_target(pose_target)

plan1 = group.plan()

group.go(wait=True)
rospy.sleep(5)
moveit_commander.roscpp_shutdown()