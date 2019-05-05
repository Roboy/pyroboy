import rclpy
from pyroboy.common_definitions import speech_synthesis_en_srv, speech_synthesis_de_srv
from time import sleep

class TTS:

    def __init__(self, node):
        self.node = node
        self.client_en = self.node.create_client(speech_synthesis_en_srv.type,
                                    speech_synthesis_en_srv.name)
        self.client_de = self.node.create_client(speech_synthesis_de_srv.type,
                                    speech_synthesis_de_srv.name)


    def generate(self, text, language="en"):
        if language == "en":
            client = self.client_en
            srv = speech_synthesis_en_srv
        elif language == "de":
            client = self.client_de
            srv = speech_synthesis_de_srv
        else:
            self.node.get_logger().info("Unknown language. Available: \"en\" and \"de\"")

        req = srv.type.Request()
        req.text = text
        if not client.wait_for_service(timeout_sec=1.0):
            self.node.get_logger().info("Service {} is not available."
                                    .format(speech_synthesis_en_srv.name))
            return

        res = client.call_async(req)
        rclpy.spin_until_future_complete(self.node, res)
#         while not res.done():
#             sleep(.2)

        if res.result() is None:
             self.node.get_logger().info('Service call failed %r' % (res.exception(),))
             return False

        return res.result().success
