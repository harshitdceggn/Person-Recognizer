# Person-Recognizer
Developed a facial recognition system using DeepFace for recognition and VGG-Face for detection, capable of real-time identification in live video streams. Optimized deep learning models for precision and speed, showcasing expertise in image processing, neural networks, and real-world AI applications.

# Real-Time Facial Recognition System
This repository contains a real-time facial recognition system built using DeepFace for face verification and OpenCV for face detection and video processing. The system identifies individuals in live video streams by comparing faces to a predefined set of images.

Features
A) Real-Time Detection: Identifies and recognizes faces from live video streams.
B) DeepFace Integration: Uses pre-trained models like VGG-Face for face recognition.
C) Customizable Database: Easily add or modify images for recognition by editing the image_list.
D) Performance Metrics: Displays real-time FPS (frames per second) to track performance.
E) Robust Face Detection: Handles various face orientations and uses OpenCV for efficient detection.

# How It Works
A) Face Detection:
   Faces are detected in the live video stream using OpenCV's face detection backend.

B) Face Recognition:
   Detected faces are cropped and verified against a predefined set of images using DeepFace's verification model (e.g., VGG-Face).

C) Real-Time Processing:
   The system processes frames continuously, updating the display with recognized names or marking unknown faces.

D) Multithreading:
   A threading mechanism ensures smooth video capture and processing without noticeable lag.

# Prerequisites
A) Python 3.7 or later
B) OpenCV
C) DeepFace
D) Threading and time modules (built-in)
E) Install required libraries with:


# This project uses the following libraries and tools:
  DeepFace for face verification
  OpenCV for video processing and face detection
# OUTPUT
![image](https://github.com/user-attachments/assets/662da5fd-7662-48ff-bc82-811c933840a5)
![image](https://github.com/user-attachments/assets/36c2b138-b4a6-4a3e-83a5-0d87f7b8b937)


License
This project is licensed under the MIT License. Feel free to modify and use it as needed!
