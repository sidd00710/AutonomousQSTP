#! /usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

rospy.init_node('topic_publisher', anonymous=True)
pub=rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=1)
rate=rospy.Rate(10)
move=Twist()


def run(str, integer):
    if(str == ['linear']):
        move.linear.x=1*integer
        move.angular.z=0
        print('linear executed')

    elif(str == ['angular']):
        move.angular.z=float(1*integer)
        move.linear.x=0
        print('angular executed')
    
    elif(str == ['stop']):
        move.linear.x=0
        move.angular.z=0
    

while not rospy.is_shutdown():
    dir=input("Enter command:").split()
    pos=int(input("Enter magnitude (negative or positive):"))
    run(dir,pos)
    pub.publish(move)
    rate.sleep()
