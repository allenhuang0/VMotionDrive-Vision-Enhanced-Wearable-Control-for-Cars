# Table of Contents
* Abstract
* [Introduction](#1-introduction)
* [Related Work](#2-related-work)
* [Technical Approach](#3-technical-approach)
* [Evaluation and Results](#4-evaluation-and-results)
* [Discussion and Conclusions](#5-discussion-and-conclusions)
* [References](#6-references)

# Abstract

In the expansive domain of autonomous driving, where vehicles often operate in isolation from human intervention, our innovation strives to reintroduce human interaction – but from a perspective not previously explored. Instead of being limited within the cabin, we imagine a world where drivers can step out and control their vehicles from the outside. This proposal is advantageous for narrow parking situations or navigating congested areas. While adept at capturing gestures, vision-only systems often have difficulty achieving the precision needed for car controls, especially in environments with variable lighting or obstructions. On the other hand, while promising accuracy, wearable-only solutions suffer from their continuous signal transmission, which can blur the boundaries of intentional commands. We aim to capitalize on the gesture recognition of the former and the precision of the latter by fusing vision with wearables.

# 1. Introduction

This section should cover the following items:

* Motivation & Objective: This project aimed to transform how we interact with vehicles. We aimed to enable drivers to control their cars from outside, using gestures and wearables. This approach was born from the desire to make urban driving more manageable and intuitive, especially in tight spaces like narrow parking and congested areas.


* State of the Art & Its Limitations: Currently, autonomous driving technologies rely heavily on in-car controls and automated systems. While recent advancements in vision-based gesture control are impressive, they offer only discrete control options, limiting their practicality in complex driving scenarios. Our project sought to overcome this by integrating vision-based systems with wearable technology, allowing for more nuanced, continuous control — akin to using a hand as a mouse to navigate more precisely.

* Novelty & Rationale: The innovative aspect of our project lies in this seamless integration of gesture recognition with wearable tech. This combination enables continuous, fluid control commands, a significant leap from the binary commands typical in current systems. This approach will succeed because it aligns with natural human movements, making it more intuitive and effective for users.

* Potential Impact:  We can extend this method to many other applications. Specifically, We envision a world where I can turn it into a virtual mouse or an interactive tool for various devices with a flick of the hand. This technology can seamlessly integrate into everyday life, transforming our interactions with our surroundings. I could use gestures in smart homes to control lighting and temperature, creating a more responsive and intuitive living environment. It could revolutionize how presentations are conducted in office settings, making interactions more engaging and fluid.

* Challenges: One of the primary challenges lies in creating a gesture recognition system that boasts high accuracy and reliability across diverse environments. Moreover, minimizing the latency in gesture recognition is a significant consideration for precise control, especially considering the computational power limitations of the Raspberry Pi platform. Additionally, ensuring a fluid transition between the wearable control and vision recognition modes is crucial to maintaining system efficacy and user engagement. Lastly, it is essential to design these wearables in a way that they are intuitive, user-friendly, and comfortable for prolonged use, thereby encouraging widespread adoption and a positive user experience.

* Requirements for Success: To successfully complete our project,  we need access to technologies like MediaPipe for advanced media processing, along with algorithms designed to accelerate processing speeds. Proficiency in 3D printing is crucial for creating wearables, as is expertise in signal processing for accurate data interpretation. The project also demands high-performance computing solutions to address the limitations of platforms like Raspberry Pi.

* Metrics of Success: Success metrics for this project focus on several key performance indicators. High accuracy in gesture recognition is essential to ensure the system reliably interprets user commands. Low latency is also critical, as it directly impacts the system's responsiveness and efficiency. Seamless integration of vision and wearables is vital to demonstrating the system's adaptability and compatibility. A practical functionality test will be the system's ability to control a vehicle through a predetermined test course, demonstrating its effectiveness in real-world scenarios. 

# 2. Related Work

# 3. Technical Approach

A. Overview
Figure xx shows an overview of our car's system structure. The system is divided into two major signal-processing components. The first comes from MPU6050 Gyro data, which is connected to Esp 32 by wire connection, and then uses esp32 wireless transmission to Raspberry Pi via web socket. The camera detects gestures as the second signal processing component. The Raspberry Pi will process the data from both ends and then integrate it to operate the motor, which will provide the car's direction. 
B. Gesture Recognition 
C. CV Optimization
D. Wearable 
D.1 Data Transmission to ESP32: The data from the MPU6050 sensor is transmitted via a wired connection to an ESP32 microcontroller. The ESP32 serves as a critical node in our system, bridging the gap between the physical gesture inputs and the digital processing unit.
D.2 Wireless Communication to Raspberry Pi: Once the ESP32 receives the gyro data, it transmits this information wirelessly to the Raspberry Pi through a WebSocket connection. This method ensures a real-time and reliable transfer of gestural data for processing.
D.3 Data Optimization
D.4 Data Conversion  
E. Integration 


# 5. Discussion and Conclusions

# 6. References

