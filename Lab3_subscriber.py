#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "It is my Pleasure ! %s", data.data)

def hello_world_sub():
    
    rospy.init_node('hello_world_sub_node', anonymous=True)
    rospy.Subscriber("hello_world", String, callback)

    rospy.spin()


if __name__ == '__main__':
    hello_world_sub()
