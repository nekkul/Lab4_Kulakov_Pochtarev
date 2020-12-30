#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from datetime import datetime

def callback(data):
    current_datetime = datetime.now()
    rospy.loginfo(data.data + "%d:%d:%d", current_datetime.hour, current_datetime.minute, current_datetime.second)

    
def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("chatter", String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()

