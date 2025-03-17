#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def hello_world_pub():
    rospy.init_node('hello_world_pub_node', anonymous=True)
    pub = rospy.Publisher('hello_world', String, queue_size=10)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        hello_str = "Welcome to IE416 %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    hello_world_pub()
