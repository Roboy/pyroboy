import rclpy
from roboy_cognition_msgs.srv import Talk, RecognizeSpeech
from roboy_control_msgs.msg import Emotion

class RosHandlerDefinition:
    def __init__(self, type, name):
        self.type = type
        self.name = name


speech_synthesis_en_srv = RosHandlerDefinition(Talk, '/roboy/cognition/speech/synthesis/talk')
speech_synthesis_de_srv = RosHandlerDefinition(Talk, '/roboy/cognition/speech/synthesis/talk/german')
speech_recognition_srv = RosHandlerDefinition(RecognizeSpeech, '/roboy/cognition/speech/recognition')

emotion_pub = RosHandlerDefinition(Emotion, '/roboy/cognition/face/emotion')
