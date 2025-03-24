import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/raspberrypi/ros_ws/src/vision_rpi_bot/install/vision_rpi_bot'
