#!/usr/bin/env python

from state1.srv import service1,service1Response
from state1.srv import *
import rospy
from geometry_msgs.msg import Twist
move=Twist()

def movement(req):
    a=False
    rate=rospy.Rate(10)
    

    if(req.state == "linear"):
        move.linear.x=1*req.dir
        move.angular.z=0
        a=True
        print('linear executed')

    elif(req.state == 'angular'):
        move.angular.z=float(1*req.dir)
        move.linear.x=0
        a=True
        print('angular executed')
    
    elif(req.state == 'stop'):
        move.linear.x=0
        move.angular.z=0
        a=True
        print('stop executed')
    
    elif(req.state == 'circle'):
        move.linear.x=1*req.dir
        move.angular.z=1*req.dir
        a=True
        print('circle executed')

    return service1Response(a)

def statemode():
    rospy.init_node('topic_publisher', anonymous=True)
    s=rospy.Service('turt', service1, movement)
    print('ready to move')
    while not rospy.is_shutdown():
        pub=rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=1)
        pub.publish(move)
    
    rospy.spin()

if __name__ == "__main__":
    statemode()
     