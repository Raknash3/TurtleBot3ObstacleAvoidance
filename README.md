# TurtleBot3ObstacleAvoidance

The TurtleBot3 Obstacle Avoidance project showcases the capabilities of the TurtleBot3 robot within the Gazebo simulator. Using Python and ROS, this project enables the TurtleBot3 robot to autonomously navigate a simulated environment while avoiding obstacles. The robot employs a proportional controller for smooth motion and obstacle detection based on the /scan data. When an obstacle comes within 0.7 meters, the robot intelligently adjusts its trajectory to bypass the obstacle and continues moving forward.

## Features
- Autonomous obstacle avoidance using TurtleBot3 in Gazebo simulator.
- Proportional controller for smooth straight-line motion and rotation.
- Dynamic obstacle detection and response based on /scan data.
- Left or right turn decision based on obstacle position.
- Gazebo world simulation for realistic environment testing.

## Installation:
-  Clone the repository
-  Install ROS and turtlebot3 and other necessary dependencies
-  Compile the folder where the repository is clones

## Launching:
- Launch the gazebo simulator for turtlebot3 in house environment
- Start the obstacle avoidance program.

