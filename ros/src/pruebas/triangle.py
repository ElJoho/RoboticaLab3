#!/usr/bin/python3

import rospy
from turtlesim.srv import TeleportAbsolute
from std_srvs.srv import Empty

if __name__ == '__main__':
    rospy.init_node('turtlesimservice', anonymous=False)

    rospy.wait_for_service('turtle1/teleport_absolute')
    turtle1_teleport = rospy.ServiceProxy('turtle1/teleport_absolute', TeleportAbsolute)

    rospy.wait_for_service('tortuga2/teleport_absolute')
    tortuga2_teleport = rospy.ServiceProxy('tortuga2/teleport_absolute', TeleportAbsolute)

    rospy.wait_for_service('clear')
    clear1 = rospy.ServiceProxy('clear', Empty)

    rate = rospy.Rate(0.3)
    pos1=1
    pos2=1
    # Similar to while(ros::ok())
    while not rospy.is_shutdown():
        if (pos2==1):
            resp1 = tortuga2_teleport(2.25, 2.25, 0)
            clear1()
        if (pos2==2):
            resp1 = tortuga2_teleport(7.75, 2.25, 0)
        if (pos2==3):
            resp1 = tortuga2_teleport(5.5, 7.75, 0)
        if (pos2==4):
            resp1 = tortuga2_teleport(2.25, 2.25, 0)
        if (pos2>4):
            pos2=1
        pos2+=1
        if (pos1==1):
            resp1 = turtle1_teleport(4, 5, 0)
            clear1()
        if (pos1==2):
            resp1 = turtle1_teleport(4, 10, 0)
        if (pos1==3):
            resp1 = turtle1_teleport(8, 10, 0)
        if (pos1==4):
            resp1 = turtle1_teleport(8, 5, 0)
        if (pos1==5):
            resp1 = turtle1_teleport(4, 5, 0)
        if (pos1>5):
            pos1=1
        pos1+=1

    rate.sleep()