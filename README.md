# Vision RPi Bot

## Overview
Vision RPi Bot is a Raspberry Pi-based robotic system designed for autonomous navigation and surveillance using computer vision and ROS2. The project includes functionalities such as line following, image publishing, and command-to-PWM conversion for motor control.

## Folder Structure
```
vision_rpi_bot/
│── cmd_to_pwm_driver.py        # Converts command inputs to PWM signals for motor control
│── image_publisher_gray.py     # Publishes grayscale images from the camera
│── surveillance_bot.py         # Controls the robot for surveillance operations
│── subscriber.py               # ROS2 subscriber node for handling messages
│── publisher.py                # ROS2 publisher node for sending messages
│── line_following_real.py      # Line following algorithm for real-world execution
│── line_following_sim.py       # Line following algorithm for simulation environment
│── __init__.py                 # Package initialization file
```

## Requirements
- Raspberry Pi 4 (or compatible hardware)
- Python 3.x
- ROS2 (Humble or later)
- OpenCV
- NumPy
- Motor driver (L298N or similar)
- Camera module (Pi Camera or USB Webcam)

## Installation
1. Clone the repository:
   ```sh
   git clone <repo_url>
   cd vision_rpi_bot
   ```
2. Install dependencies:
   ```sh
   pip install opencv-python numpy rclpy
   ```
3. Source ROS2 environment:
   ```sh
   source /opt/ros/humble/setup.bash
   ```

## Usage
### 1. Running the Line Following Bot
For real-world execution:
```sh
python3 line_following_real.py
```
For simulation:
```sh
python3 line_following_sim.py
```

### 2. Running the Surveillance Bot
```sh
python3 surveillance_bot.py
```

### 3. Running ROS2 Nodes
Start the publisher:
```sh
python3 publisher.py
```
Start the subscriber:
```sh
python3 subscriber.py
```

## Contribution
Feel free to fork and submit pull requests for improvements or feature additions.


