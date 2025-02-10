#!/usr/bin/python3
import rospy
from turtlesim.msg import Pose

def poseMessageReceived(message):
    rospy.loginfo('position=(' + str(message.x) + ',' + str(message.y) + ')' + ' direction=' + str(message.theta))

if __name__ == '__main__':
    rospy.init_node('pysubpose', anonymous=False)
    sub = rospy.Subscriber('turtle1/pose', Pose, poseMessageReceived)
    rospy.spin()
