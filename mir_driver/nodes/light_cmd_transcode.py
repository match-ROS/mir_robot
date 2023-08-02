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
        self.light_cmd_srv = rospy.ServiceProxy('/light_srv', LightCommand)
        
        rospy.spin()

    def callback(self,data):

        result= self.light_cmd_srv(data.effect, data.color1, data.color2, data.leds, data.token, data.timeout, data.priority)
        print(result)

if __name__ == '__main__':
    try:
        rospy.init_node('light_cmd_transcode', anonymous=True)
        LightCmdTranscode()
    except rospy.ROSInterruptException:
        pass
