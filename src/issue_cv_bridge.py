#!/usr/bin/env python3

import rospy
import cv_bridge

try:
    import PIL.Image
except ImportError:
    print('Missing library(Pillow)! you can install it using `pip3 install Pillow`')

try:
    import numpy
except ImportError:
    print('Missing library(numpy)! you can install it using `pip3 install numpy`')

from sensor_msgs.msg import Image


rospy.init_node('issue_cv_bridge_node')

bridge = cv_bridge.CvBridge()
empty_image = PIL.Image.new('RGB', (10, 10)) # create new empty 10*10 image
ros_image = bridge.cv2_to_imgmsg(numpy.asarray(empty_image), encoding='rgb8') # convert PIL image to ROS image

rate = rospy.Rate(1)
image_publisher = rospy.Publisher('~image', Image, queue_size=1)

while not rospy.is_shutdown():
        image_publisher.publish(ros_image)
        rate.sleep()
