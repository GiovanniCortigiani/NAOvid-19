# NAOvid-19
This repository contains the package needed to run the project on the NAO Robot. The robot is in charge of being a shopassistant: he welcomes venue visitors by checking their QR Code and answering questions, and says goodbye to visitors exiting from the Shop. Further, through shirt and face detection he identifies the visitors, thus knowing whether a visitor has already entered in the shop, not asking again for the QR Code. Taking into account the number of visitors inside the shop, he denies the entrance if the shop is full. If a customer wishes also to talk with a real human, a teleoperator handles the control of the NAO Robot, to talk with the customer, drive him somewhere or do whatever the visitor asks. One the teleoperator is done, the robot is able to return to his position by checking his position with respect to an ArUco Marker.

Collaborators: Giovanni Cortigiani, Bernhard Glas, Ziting Huang

![Shop Entrance](/Figures/NAO_ShopEntrance_cut.jpg)


## Execution

To run the project properly, the following commands need to be executed in different terminals:

```
$ roslaunch nao_bringup nao_full_py.launch
```

The launch file of the NAO robot;

```
$ roslaunch Naovid nao_apps.launch
```

This launches the speech, tactile and led apps of the robot;

```
$ docker run -p 8000:8000 -e CERT_COUNTRY=DE ghcr.io/merlinschumacher/open-covid-certificate-validator:main
```

Needed for the Vaccination Certificate Check;

```
$ roslaunch Naovid nao.launch
```

The last one is the main launch file and will make the execution start.
Please be aware that the robot will stand up at the beginning of the project.

![Teleassistant Screen Layout](/Figures/NAO_Teleassisant_Screen_Overview.png)
After executing the four commands in four different terminals, the execution should like the above-shown overview of the Teleassistant Screen Layout (with live-streams from both NAO cameras at the left side, the third-person camera-view of the utilized laptop at the upper right side, the four terminals executing the required commands in the background (the project’s executable was run on the teleoperator’s computer in our setup) and the window of the teleoperator instructions at the bottom in order to ensure intuitive control which is doable by a randomly selected person with minimal training).

### Structure of the package

The main code is in the client.cpp. This file contains the main loop where a state machine determines the behaviour of the robot in the different situations. A service-client structure is usually exploited for robot movements, gestures and speech.

### Dependencies and libraries

To run the project properly, the following dependencies have to be installed:

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
$ sudo docker --version
```

Docker-compose is additionally needed for the Covid Certificate interface. Please find a tutorial to install it [here.](https://docs.docker.com/compose/install/)

```
$cmake_minimum_required(VERSION 2.8.3)  
```

The CMake requirement was also added to the CMakeList, in order to ensure a smooth compilation.

Furthermore, all the libraries, tools and frameworks from the tutorial sessions of the course "Humanoid Robotic Systems" (e.g., OpenCV, Rospy, ROS Kinetic, TF) were utilized within this project and should already be pre-installed on the student computers which are run by Ubuntu 14.04.

### Hardware

The code is launched by the teleoperator in a separate room. If in the computer is not integrated a speaker or microphone, and additional device can be connected do it to be able to listen and speak. A common Xbox joystick was utilised to control the robot in the teloperation. The communication between the visitor and the teleoperator can be done with any device, e.g. using a Zoom videocall on a computer located in the shop entrance where NAOvid-19 lies. In this way, the teleoperator can both interact with the visitor speaking and listening, while at the same time have an external camera pointing to the robot.
