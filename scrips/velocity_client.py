#!/usr/bin/env python
#coding utf-8
import rospy
from geometry_msgs.msg import Twist
from ros_start.srv import SetVelocity
import sys

if __name__=='__main__':
    rospy.init_node('velocity_client')
    set_velocity = rospy.ServiceProxy('set_velocity',SetVelocity)
    linear_vel = float(sys.argv[1])
    angular_vel = float(sys.argv[2])
    response = set_velocity(linear_vel, angular_vel)
    if response.success:
        rospy.loginfo('set [%f,%f] success' % (linear_vel,angular_vel))
    else:
        rospy.loginfo('set [%f,%f] failure' % (linear_vel,angular_vel))
