# VMotionDrive: Vision Enhanced Wearable Control for Cars

This repo is created for the M202 Final Project in Fall 2023

## Table of Contents

1. [Team](#team)
2. [Abstract](#abstract)
3. [Objective](#objective)
4. [Setup](#setup)



## Team

* Guanyu Qian
* Allen (Yilun) Huang

## Abstract

In autonomous driving, where vehicles often operate in isolation from human intervention, our innovation strives to reintroduce human interaction – but from a perspective not previously explored. Instead of being limited within the cabin, we imagine a world where drivers can step out and control their vehicles from the outside. Our proposal is advantageous for narrow parking situations or navigating congested areas. 
While good at recognizing gestures, vision-based systems often have difficulty achieving the precision needed for car controls, especially for moving gestures. On the other hand, while promising accuracy, wearable-only solutions suffer from their continuous signal transmission, which can blur the boundaries of intentional commands. We aim to invent a novel control scheme that seamlessly integrates vision and wearable devices.

## Objective

Our approach is to interpret hand movements as sequenced motions. A gesture is not seen as an isolated movement but as part of a continuum. The initial hand gesture acts as an activation sign, a starting point for sending instruction signals. The wearable device then steps in and refines these commands, offering precise and nuanced control over the vehicle.\
We aim to use computer vision for gesture recognition utilizing Python and an accelerometer for the wearable device to send XYZ signals.


## Setup

### Hardware 

* Raspberry Pi 4
* Motors
* Router
* Camera

### Software

* Python
* C

## Required Submissions

- [Proposal](https://github.com/QGY511/VMotionDrive-Vision-Enhanced-Wearable-Control-for-Cars/blob/main/docs/proposal.md)
- [Midterm Checkpoint Presentation Slides](https://docs.google.com/presentation/d/1pWHNaR9iEYGdNeJO3ODqu5yN1HMn7bvlZhVNw9ZQYS4/edit?usp=sharing)
- [Final Presentation Slides](https://docs.google.com/presentation/d/13GRcztlCDkTzBT6fXpTf-_WH6NwUOQoknaz7muQz_2A/edit?usp=sharing)
- [Final Report](https://github.com/QGY511/VMotionDrive-Vision-Enhanced-Wearable-Control-for-Cars/blob/main/docs/report.md)
- [Demo Videos](https://youtu.be/3k7qivbMPUk)


## Gesture Extraction
![](images/gesture_demo.png)

![](images/hand_direction.png)


## Project Timeline

### Prototype (Nov 1, 2023)
![](images/prototype.png)

### Update (Nov 15, 2023)
![](images/1115_update.png)

### Update (Nov 20, 2023)
![](images/wearable.png)
![](images/wearable2.png)

### Final (Dec 10, 2023)
![](images/final_car.png)
![](images/testing.png)
