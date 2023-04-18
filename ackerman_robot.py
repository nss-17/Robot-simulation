# -*- coding: utf-8 -*-
"""ackerman robot .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1L7SGtPrwCegEKvci3VNacc-OFlIJpu47
"""

import numpy as np
import matplotlib.pyplot as plt

# Robot parameters
r = 0.05  # Radius of the wheels
l = 0.2  # Distance between two wheels
L = 1
R = 0.2

# Generate path (sin)
path_x = np.linspace(0, 2*np.pi, 50)   #50 points between 0 and 2pi
path_y = np.sin(path_x)

# Initial robot position and orientation
x = path_x[0]
y = path_y[0]
theta = np.pi/4
w_r = 0
w_l = 0
w = 0
phi = 0

# Simulation parameters
dt = 0.1  # Time step

# Arrays to store robot states
robot_x = np.array([x])
robot_y = np.array([y])
robot_theta = np.array([theta])
robot_wR = np.array([w_r])
robot_wL = np.array([w_l])
robot_w = np.array([w])

# Function to simulate path following
def simulate_path_following(phi):
    global x, y, theta, w_r, w_l, w
    global robot_x, robot_y, robot_theta, robot_wR, robot_wL, robot_w
    for t in np.arange(0, 1, dt):
        # Compute the desired linear and angular velocities to follow the path
        path_index = int(t/dt)
        dx = path_x[path_index+1] - path_x[path_index]   # Distance between current and next point on path   
        dy = path_y[path_index+1] - path_y[path_index]
        desired_theta = np.arctan2(dy, dx)    
        desired_v = (np.sqrt(dx**2 + dy**2))/dt     # v = S/t
        desired_w = (desired_theta - theta)/dt
    
        # Compute the left and right wheel velocities based on the desired linear and angular velocities
        w_l = (desired_v - l/2*desired_w)/r
        w_r = (desired_v + l/2*desired_w)/r

        # Compute the robot's new position and orientation based on the wheel velocities
        V = r/2*(w_l + w_r)
        x += V*np.cos(theta)*dt
        y += V*np.sin(theta)*dt
        theta += V*np.tan(phi)/L*dt
    
        # Store the robot new states
        robot_x = np.append(robot_x, x)
        robot_y = np.append(robot_y, y)
        robot_theta = np.append(robot_theta, theta)
        robot_wR = np.append(robot_wR, w_r)
        robot_wL = np.append(robot_wL, w_l)
    
    # Plot the result
    plt.plot(path_x, path_y, '.', label='Original Path')
    plt.plot(robot_x, robot_y, '.', label='Robot Path')
    plt.legend()
    plt.axis('equal')
    plt.show()

# Call the function to simulate path following
simulate_path_following(0)
simulate_path_following(-np.pi/4)
simulate_path_following(0)
simulate_path_following(np.pi/4)
simulate_path_following(0)

