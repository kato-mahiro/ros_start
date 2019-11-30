#!/usr/bin/env python
#encoding:utf-8

"""
- 独自に作成したService型，SetVelocityResponseを使う
- 指定できる速度，角速度の値の範囲が決まっており，それ以上の速度は無視
- 値をセットできたかできなかったが戻り値でわかる
"""

import rospy
from geometry_msgs.msg import Twist

"定義した「srv」の型のSetVelocityとその戻り値SetVelocityResponseをimport"
from ros_start.srv import SetVelocity
from ros_start.srv import SetVelocityResponse

MAX_LINEAR_VELOCITY = 1.0
MIN_LINEAR_VELOCITY = -1.0
MAX_ANGULAR_VELOCITY = 2.0
MIN_ANGULAR_VELOCITY = -2.0

def velocity_handler(req):
    vel = Twist()
    is_set_success = True
    if (req.linear_velocity <= MAX_LINEAR_VELOCITY) and \
       (req.linear_velocity >= MIN_LINEAR_VELOCITY):
        vel.linear.x = req.linear_velocity
    else:
        is_set_success = False

    if (req.angular_velocity <= MAX_ANGULAR_VELOCITY) and\
       (req.angular_velocity >= MIN_ANGULAR_VELOCITY):
        vel.angular.z = req.angular_velocity
    else:
        is_set_success = False

    if is_set_success:
        pub.publish(vel)

    return SetVelocityResponse(success = is_set_success)

if __name__=='__main__':
    rospy.init_node('velocity_server')

    "速度発行用のPublisherを作成"
    pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=10)

    "ServiceServerを作成"
    service_server = rospy.Service('set_velocity', SetVelocity, velocity_handler)

    rospy.spin()
