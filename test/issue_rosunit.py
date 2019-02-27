#!/usr/bin/env python3

import rospy
import unittest


class TestROSUnitIssue(unittest.TestCase):
    def test_true(self):
        self.assertTrue(1 == 1)

    def test_false(self):
        self.assertTrue(1 != 1)


if __name__=='__main__':
    import rostest
    rospy.init_node('tests_node')
    rostest.rosrun('ros_python3_issues', 'issue_rosunit', TestROSUnitIssue)