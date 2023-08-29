#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
import math

rospy.init_node('turtlebot_controller', anonymous=True)
velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

# Proportional controller gains for linear and angular velocities
linear_kp = 0.07
angular_kp = 0.07

# Maximum allowed angular velocity
max_angular_velocity = 0.15  # Adjust as needed

# Minimum obstacle distance to trigger a turn
min_obstacle_distance = 0.7 # Adjust as needed

def scan_callback(scan_data):
    global vel_msg  # Declare vel_msg as a global variable

    # Find the minimum range value within the scan data, ignoring NaN values
    min_range = min([r for r in scan_data.ranges if not math.isnan(r)])

    print("Distance to any obstacle: {:.2f}".format(min_range))
    # Set the linear velocity based on the minimum range
    
   

    
    # Only apply angular velocity adjustments if an obstacle is near
    if min_range < min_obstacle_distance:
        print("Obstacle too close: {:.2f}".format(min_range))
        # Calculate the desired angular velocity based on obstacle distances
        left_obstacle_distance = min(scan_data.ranges[:len(scan_data.ranges)//2])
        right_obstacle_distance = min(scan_data.ranges[len(scan_data.ranges)//2:])
        
        # Choose the direction with the closer obstacle to turn away from it
        if left_obstacle_distance < right_obstacle_distance:
            angular_velocity = -angular_kp * (1.0 / left_obstacle_distance)  # Negative for turning left
        else:
            angular_velocity = angular_kp * (1.0 / right_obstacle_distance)   # Positive for turning right
        
        # Limit the angular velocity to the maximum allowed value
        angular_velocity = max(-max_angular_velocity, min(max_angular_velocity, angular_velocity))
        
        vel_msg.angular.z = angular_velocity
        vel_msg.linear.x = linear_kp * min_range
    else:
        vel_msg.angular.z = 0.0  # Reset angular velocity if no obstacle nearby
        vel_msg.linear.x = 0.2 * min_range
    
    print("Linear velocity : {:.2f}".format(vel_msg.linear.x))
    print("Angular velocity : {:.2f}".format(vel_msg.angular.z))

def move_turtlebot():
    rate = rospy.Rate(10)  # 10 Hz

    while not rospy.is_shutdown():
        velocity_publisher.publish(vel_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        vel_msg = Twist()
        scan_subscriber = rospy.Subscriber('/scan', LaserScan, scan_callback)
        move_turtlebot()
    except rospy.ROSInterruptException:
        pass