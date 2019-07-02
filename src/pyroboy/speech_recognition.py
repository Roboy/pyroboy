import rospy
from pyroboy.common_definitions import speech_recognition_srv
from time import sleep

class STT:

    def __init__(self):
        self.client = rospy.ServiceProxy(speech_recognition_srv.name, speech_recognition_srv.type)


    def recognize_speech(self):
        req = speech_recognition_srv.request()
        try:
            self.client.wait_for_service(timeout=1.0)
        except Exception as e:
            rospy.logerr(str(e))
            return

        res = self.client(req)

        if res is None:
             rospy.loginfo('STT service call failed.')
             return

        return res.text
