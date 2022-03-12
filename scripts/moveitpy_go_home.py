#! /usr/bin/env python

import rospy
from moveit_python import MoveGroupInterface
from moveit_msgs.msg import MoveItErrorCodes

rospy.init_node('moveit_python_tutorial', anonymous=True)

move_group = MoveGroupInterface("arm", "base_link")

joints = [
    "elbow_flex_joint",
    "forearm_roll_joint",
    "shoulder_lift_joint",
    "shoulder_pan_joint",
    "upperarm_roll_joint",
    "wrist_flex_joint",
    "wrist_roll_joint"]

pose = [1.7, 0.0, 1.4, 1.32, -0.2, 1.57, 0.0]

while not rospy.is_shutdown():

    result = move_group.moveToJointPosition(joints, pose, 0.02)
    if result:

        if result.error_code.val == MoveItErrorCodes.SUCCESS:
            rospy.loginfo("Trajectory successfully executed!")
            break
        else:
            rospy.logerr("Arm goal in state: %s",
                         move_group.get_move_action().get_state())
    else:
        rospy.logerr("MoveIt failure! No result returned.")

move_group.get_move_action().cancel_all_goals()
'''
    <group_state name="home" group="arm">
        <joint name="elbow_flex_joint" value="1.7"/>
        <joint name="forearm_roll_joint" value="0"/>
        <joint name="shoulder_lift_joint" value="1.4"/>
        <joint name="shoulder_pan_joint" value="1.32"/>
        <joint name="upperarm_roll_joint" value="-0.2"/>
        <joint name="wrist_flex_joint" value="1.57"/>
        <joint name="wrist_roll_joint" value="0"/>
    </group_state>
'''