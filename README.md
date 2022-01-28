# NAOVID-19
Giovanni Cortigiani, Bernhard Glas, Ziting Huang


## To run the project, please run these commands in separate terminals:

```
$ roslaunch nao_bringup nao_full_py.launch
```
```
$ roslaunch Naovid nao_apps.launch
```
```
$ docker run -p 8000:8000 -e CERT_COUNTRY=DE ghcr.io/merlinschumacher/open-covid-certificate-validator:main
```
```
$ roslaunch Naovid nao.launch
```

The last one is the main launch file and will make the execution start.
Please be aware that the robot will stand up at the beginning of the project.

## To run the project properly, the following dependencies have to be installed:
```
$ sudo apt-get install libsfml-dev
```
This will install the Simple and Fast Multimedia Library (SFML)-library which is needed for the teleoperation mode in order to process the inputs of the gamepad and create a window to explain the functionalities to a new teleoperator.
```
$ sudo apt-get install libboost-all-dev
```
This library is used to read files from the system.
```
$ sudo apt-get install libzbar0
```
This library will encode the shown QR-codes intro a string in line with OpenCV.
```
$ Docker is aditionally needed for the Covid Certificate interface. Please find a tutorial to install it [here.](https://docs.docker.com/compose/install/)

We also added the cmake minimum required version $cmake_minimum_required(VERSION 2.8.3) to the CMakeList. 

Furthermore, all the libraries, tools and frameworks from the tutorial sessions of the course "Humanoid Robotic Systems" (e.g., OpenCV, Rospy, ROS Kinetic, TF) were utilized within this project and should already be pre-installed on the student computers which are run by Ubuntu 14.04.
