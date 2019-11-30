#!/usr/bin/env python
#encoding:utf-8

import rospy
import actionlib
from ros_start.msg import GoUntilBumperAction
from ros_start.msg import GoUntilBumperGoal

def go_until_bumper():
    action_client = actionlib.SimpleActionClient('bumper_action',GoUntilBumperAction)
    #サーバが準備できるまで待つ
    action_client.wait_for_server()
    goal = GoUntilBumperGoal()
    goal.target_vel.linear.x = 0.8
    goal.timeout_sec = 10

    action_client.send_goal(goal)
    action_client.wait_for_result()
    result = action_client.get_result()
    if result.bumper_hit:
        rospy.loginfo('bumper hit!')
    else:
        rospy.loginfo('failed')

if __name__ == '__main__':
    try:
        rospy.init_node('bumper_client')
        go_until_bumper()
    #Ctrl-Cで終了できるようにする
    except rospy.ROSInterruptException:
        pass
