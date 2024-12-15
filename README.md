Hand Tracking and Virtual Mouse Control

This project implements a virtual mouse control system using hand tracking techniques. It leverages computer vision and machine learning to track hand movements via a webcam and translate them into mouse pointer controls. The implementation uses Python libraries like OpenCV, MediaPipe, and AutoPy.

Features

Hand tracking using MediaPipe.

Mouse movement using the index finger.

Mouse click simulation using both the index and middle fingers.

Real-time FPS display.

Requirements

Python 3.x

OpenCV

MediaPipe

AutoPy

NumPy

Installation

Clone the repository or download the source code.

Install the required libraries using pip:

pip install opencv-python mediapipe autopy numpy

Run the main script:

python main.py

How It Works

Main Code

Camera Initialization:

Captures video from the webcam.

Sets the frame dimensions.

Hand Tracking:

Detects hands and identifies landmarks using the handDetector class from the module.

Interaction Modes:

Move Mode: Moves the mouse when only the index finger is up.

Click Mode: Simulates a mouse click when both the index and middle fingers are up and close to each other.

FPS Calculation:

Calculates and displays the real-time FPS on the output window.

Exit Condition:

Stops the program when the user presses the 'q' key.

Module Code

Hand Detection:

Uses MediaPipe to detect hand landmarks and draw them on the video frames.

Position Calculation:

Computes the position of hand landmarks and returns their coordinates.

Distance Calculation:

Measures the distance between two specified hand landmarks.

Finger State Detection:

Identifies which fingers are up by comparing the positions of landmarks.

Files

main.py: Main script for virtual mouse control.

modulesupport.py: Module containing the handDetector class for hand tracking and utility functions.

Usage

Run the main.py script.

Place your hand in front of the camera.

Use the index finger to move the mouse pointer.

Use the index and middle fingers to simulate a mouse click.

Results

Real-time hand tracking and interaction with the computer interface.

Smooth mouse pointer movements and reliable click detection.

High accuracy and fast performance with visible FPS.

Challenges

Achieving smooth and stable mouse pointer movements.

Handling variable lighting conditions and background noise.

Future Improvements

Add support for right-click and scroll gestures.

Optimize performance for lower-end hardware.

Enhance hand tracking robustness in different environments.
