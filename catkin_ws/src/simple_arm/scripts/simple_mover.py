#!/usr/bin/env python

import math
import rospy	# Importing the official Python client library for ROS
from std_msgs.msg import Float64	# Importing the ROS primitive message 
									# type Float64 from the srd_masg package

def mover():
	pub_j1 = rospy.Publisher('/simple_arm/joint_1_position_controller/command',
							Float64, queue_size = 10)	# Declaration of publisher
														# for joint 1 commands

	pub_j2 = rospy.Publisher('/simple_arm/joint_2_position_controller/command',
							Float64, queue_size = 10)	# Declaration of publisher
														# for joint 2 commands

	rospy.init_node('arm_mover')	# Initializes the "arm_mover" (this code) node and 
									# registers it with the master
	rate = rospy.Rate(10)	# Rate object used to limit the frequency at which 
							# certain loops spin in ROS (10Hz)
	start_time = 0		# Used to determine how much time has elapsed

	while not start_time:
		start_time = rospy.Time.now().to_sec()	# rospy.Time.now() will initially 
												# return 0, until the first mesage 
												# has been received on the /clock topic

	while not rospy.is_shutdown():
		elapsed = rospy.Time.now().to_sec() - start_time

		# Publishing messages:
		pub_j1.publish(math.sin(2*math.pi*0.1*elapsed) * (math.pi/2))
		pub_j2.publish(math.sin(2*math.pi*0.1*elapsed) * (math.pi/2))

		rate.sleep()	# It makes the loop to be traversed at apprx 10Hz

if __name__ == '__main__':
	try:
		mover()
	except rospy.ROSInterruptException:
		pass