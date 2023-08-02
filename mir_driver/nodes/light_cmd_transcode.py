#!/usr/bin/env python3

# this node subsribes to /light_cmd and creates a service call to /light_cmd_srv
# this is done becuase the mir_bridge will not pass service calls

import rospy
from mir_srvs.srv import LightCommand

#from mir_msgs.msg import LightCommand
import mir_msgs.msg

class LightCmdTranscode():
    def __init__(self):
        rospy.Subscriber('/new_light_cmd', mir_msgs.msg.LightCmd, self.callback)
        self.light_cmd_srv = rospy.ServiceProxy('/light_cmd_srv', LightCommand)
        
        rospy.spin()




    def callback(self,data):
        print(data)
        light_cmd_req = LightCommand()
        light_cmd_req.command = data.effect
        light_cmd_req.color = data.color1
        light_cmd_req.color2 = data.color2
        light_cmd_req.leds = data.leds
        light_cmd_req.token = data.token
        light_cmd_req.timeout = data.timeout
        light_cmd_req.priority = data.priority

        print(light_cmd_req)
        self.light_cmd_srv(data.effect, data.color1, data.color2, data.leds, data.token, data.timeout, data.priority)

if __name__ == '__main__':
    try:
        rospy.init_node('light_cmd_transcode', anonymous=True)
        LightCmdTranscode()
    except rospy.ROSInterruptException:
        pass
