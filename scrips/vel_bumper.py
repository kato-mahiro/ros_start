#!/usr/bin/env python
#coding:utf-8

import rospy
from geometry_msgs.msg import Twist # Twis型を使うためにimport
from kobuki_msgs.msg import BumperEvent

rospy.init_node('vel_publisher')
vel_x = rospy.get_param('~vel_x',0.5)
vel_rot = rospy.get_param('~vel_rot',1.0)
pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=10)

def callback(bumper):
    print bumper
    back_vel = Twist()
    back_vel.linear.x = -vel_x
    r = rospy.Rate(10.0)
    for i in range(5):
        pub.publish(back_vel)
        r.sleep()

sub = rospy.Subscriber('/mobile_base/events/bumper', BumperEvent,callback, queue_size=1) #トピック名，型名，呼び出す関数

while not rospy.is_shutdown():
    vel = Twist()
    direction = raw_input('f: forward, b: backward, l: left, r: right >')
    if 'f' in direction:
        vel.linear.x = 0.5
    if 'b' in direction:
        vel.linear.x = -0.5
    if 'l' in direction:
        vel.angular.z = 1.0
    if 'r' in direction:
        vel.angular.z = -1.0
    if 'q' in direction:
        break
    print vel
    r = rospy.Rate(10.0)
    for i in range(10):
        pub.publish(vel)
        r.sleep()
