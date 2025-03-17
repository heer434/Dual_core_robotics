#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

def position_publisher():
    rospy.init_node('pos_pub_node')
    pub = rospy.Publisher('position_out', Int32, queue_size=10)
    rate = rospy.Rate(10)

    rospy.loginfo("Position Publisher Node Started")

    while not rospy.is_shutdown():
        pos_msg = 460
        rospy.loginfo(f"Publishing Position: {pos_msg}")
        pub.publish(pos_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        position_publisher()
    except rospy.ROSInterruptException:
        pass
