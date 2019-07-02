import rospy
from pyroboy.common_definitions import speech_synthesis_en_srv, speech_synthesis_de_srv
from time import sleep

class TTS:

    def __init__(self):
        self.client_en = rospy.ServiceProxy(speech_synthesis_en_srv.name,
                                    speech_synthesis_en_srv.type)
        self.client_de = rospy.ServiceProxy(speech_synthesis_de_srv.name,
                                    speech_synthesis_de_srv.type)


    def generate(self, text, language="en"):
        if language == "en":
            client = self.client_en
            srv = speech_synthesis_en_srv
        elif language == "de":
            client = self.client_de
            srv = speech_synthesis_de_srv
        else:
            rospy.loginfo("Unknown language. Available: \"en\" and \"de\"")

        req = srv.request()
        req.text = text
        try:
            client.wait_for_service(timeout=1.0)
        except Exception as e:
            rospy.logerr(str(e))
            return

        res = client(req)
#         while not res.done():
#             sleep(.2)

        if res is None:
             rospy.loginfo('TTS service call failed')
             return False

        return res.success
