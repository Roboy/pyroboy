import rclpy
from pyroboy.common_definitions import speech_recognition_srv
from time import sleep

class STT:

    def __init__(self, node):
        self.node = node
        self.client = self.node.create_client(speech_recognition_srv.type,
                                    speech_recognition_srv.name)


    def recognize_speech(self):
        req = speech_recognition_srv.type.Request()
        if not self.client.wait_for_service(timeout_sec=1.0):
            self.node.get_logger().info("Service {} is not available."
                                    .format(speech_recognition_srv.name))
            return

        res = self.client.call_async(req)
        rclpy.spin_until_future_complete(self.node, res)
#         while not res.done():
#             sleep(.2)

        if res.result() is None:
             self.node.get_logger().info('Service call failed %r' % (res.exception(),))
             return

        return res.result().text
