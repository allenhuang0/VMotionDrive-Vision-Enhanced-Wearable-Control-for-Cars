# Project Proposal

## 1. Motivation & Objective

In the expansive domain of autonomous driving, where vehicles often operate in isolation from human intervention, our innovation strives to reintroduce human interaction – but from a perspective not previously explored. Instead of being limited within the cabin, we imagine a world where drivers can step out and control their vehicles from the outside. This proposal is advantageous for narrow parking situations or navigating congested areas. We aim to invent a control system integrating gesture recognition and wearable control.

Our approach is to interpret hand movements as sequenced motions. A gesture is not seen as an isolated movement but as part of a continuum. The initial hand gesture acts as an activation sign, a starting point for sending instruction signals. The wearable device then refines these commands, offering precise and nuanced control over the vehicle.


## 2. State of the Art & Its Limitations

Current gesture control technology has made significant strides but is not without its limitations. One of the main challenges in current gesture recognition systems is the need for precise control over continuous variables. For instance, in vehicular technology, users can typically adjust speed through specific, predefined gestures. However, this form of control is discrete. It does not offer fine-tuned adjustments, leading to a binary outcome, such as accelerating or decelerating, without the subtlety of gradual change.
Moreover, the integration of wearable technology with gesture control is still in its infancy. Current wearables are limited in their ability to capture the full range of human motion and translate it into nuanced commands, which restricts the potential for more advanced interactions and control that are seamless and intuitive. This gap underlines future research and development opportunities to enhance the granularity and integration of gesture-based systems.

## 3. Novelty & Rationale

Our project introduces a groundbreaking hybrid model, seamlessly fusing the extensive gesture recognition capabilities of computer vision with the pinpoint accuracy of wearable technology. By interpreting hand movements as dynamic, continuous sequences, our system initiates with broad gesture recognition and refines control through wearable feedback, ensuring unparalleled precision in vehicular manipulation.

## 4. Potential Impact

The advancement of gesture-controlled autonomous vehicle technology stands to transform vehicle operation significantly. This innovation will make it possible for individuals to control their cars from the outside, easing parking in tight spots, even for those without a license, using simple hand gestures. Such improvements in vehicle interaction will enhance road safety, mitigate traffic congestion, and streamline traffic management. The ripple effects will benefit individual driving experiences and urban transportation systems, paving the way for a new era of smarter, safer, and more efficient travel.

## 5. Challenges

The project aims to refine computer vision and enhance the integration of wearables to enable sophisticated gesture control for autonomous vehicles. A key challenge is developing algorithms capable of interpreting complex gestures with high precision. The system must recognize subtle hand movements accurately. Determining when and how wearables should augment gesture detection is another complex issue, requiring a delicate balance to ensure they complement rather than override the user's commands. Addressing these challenges is crucial for a responsive and reliable gesture-based 


## 6. Requirements for Success


To successfully implement this gesture control technology, gesture recognition accuracy must be high. Users should be able to modulate the speed of the vehicle with precision based on the intensity of their hand movements. This means the system must be sensitive enough to detect and interpret the force and speed with which a gesture is made, translating it into corresponding vehicular speed changes. To accomplish this, sensors must be finely calibrated, and algorithms must be trained on various gestures under different conditions to ensure reliability. Additionally, the user interface must be intuitive, providing real-time feedback to users to adjust their gestures as needed. These requirements are essential to create a seamless and practical user experience that can adjust to individual preferences and driving situations.


## 7. Metrics of Success

We will measure success through several key indicators: accuracy of gesture recognition, precision in vehicular control, user satisfaction, and adaptability to varying environmental contexts. Additionally, system responsiveness, reliability, and ease of use will be critical metrics.

## 8. Execution Plan


Our execution plan will proceed in distinct phases, starting with developing computer vision and wearable technologies separately. The initial design will ensure these systems can independently achieve high accuracy in gesture recognition. We will integrate them to function cohesively with vehicle control systems upon achieving standalone reliability. This will be followed by comprehensive testing under different scenarios to ensure system robustness. We will employ a feedback-driven approach for constant refinement, setting the stage for a robust and user-centric final product.


## 9. Related Work

### 9.a. Papers

Two papers are considered (full link in the reference section):

Easy Hand Gesture Control of a ROS-Car Using Google MediaPipe for Surveillance Use.

Tracked Robot Control with Hand Gesture Based on MediaPipe.
 

The methodology and findings from this study provide crucial insights into the feasibility and practicality of using hand gestures for nuanced vehicle/robot control, thereby contributing valuable knowledge to enhancing human-machine interaction.

### 9.b. Datasets

Gesture Recognition: datasets from the Google Mediapipe development are used.
Wearable: gyro sensor data are also recorded from our testing.

### 9.c. Software

Python for vision processing and C++ for gyro data processing.

## 10. References

Allena, C. D., De Leon, R. C., & Wong, Y. Y. (2022). Easy hand gesture control of a ROS-Car using Google MediaPipe for surveillance use. In *Lecture Notes in Computer Science* (pp. 247–260). [https://doi.org/10.1007/978-3-031-05544-7_19](https://doi.org/10.1007/978-3-031-05544-7_19)

Wameed, M., Alkamachi, A., & Erçelebi, E. (2023). Tracked Robot Control with Hand Gesture Based on MediaPipe. *Al-Khwarizmi Engineering Journal*, 19(3), 56–71. [https://doi.org/10.22153/kej.2023.04.004](https://doi.org/10.22153/kej.2023.04.004)



