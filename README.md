# Construction-Site-Hazard-Detection

24-678: Computer Vision for Engineers - Carnegie Mellon University - Final Project

This project is made to create a Hazard Detection in a Construction Site based on the location of the worker in the site. 

The location of the worker is obtained by a camera feed on the site. The video feed is sent through a YoloV7 object detection program to identify the coordinates of the workers every frame. 

The coordinates are 2 Dimensional and they are then feed a global coordinate calculator program that uses transformation matrices to convert the 2D coordinates into 3D.

The new coordinates are cross referenced with the coordinates of the safe regions and the danger zones to identify the workers in the danger zone and raise a warning. 
