import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/pc22/Desktop/MicrocontrollersTheConstruct/ros_ws/install/pong_reply_node'
