#!/usr/bin/env python3

import rospy

from std_msgs.msg import Int32


rospy.init_node('issue_yaml')

rate = rospy.Rate(1)
publisher = rospy.Publisher('~counter', Int32, queue_size=1)

i = 0
while not rospy.is_shutdown():
    publisher.publish(data=i)
    i += 1
    rate.sleep()
