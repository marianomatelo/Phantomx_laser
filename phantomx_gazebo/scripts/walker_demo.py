#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
import sensor_msgs.msg
from phantomx_gazebo.phantomx import PhantomX

def callback(data):
	n = 0
	while(n<720):
		rospy.loginfo("Distancia: %f Angulo: %f", data.ranges[n],n)
		if(data.ranges[n] > 1.1):
			rospy.loginfo("if")
			robot.set_walk_velocity(0, 0, 0)
			rospy.sleep(0.2)
			robot.set_walk_velocity(-1, 0, 0)
			rospy.sleep(1)
			robot.set_walk_velocity(1, 0, 0.5)
			rospy.sleep(2)
		else:
			rospy.loginfo("else")
			robot.set_walk_velocity(1, 0, 0)
			rospy.sleep(0.1)
		n=n+72

def listener():
	rospy.Subscriber("/phantomx/laser/scan", LaserScan, callback)
	rospy.spin()

if __name__ == '__main__':
	rospy.init_node('walker_demo')
	rospy.loginfo('Instanciando Phantomx')
	robot = PhantomX()
	rospy.sleep(1)
	rospy.loginfo('Robot Listo!')
	robot.set_walk_velocity(0, 0, 0)
	listener() 
	rospy.loginfo('Robot Apagado!')


