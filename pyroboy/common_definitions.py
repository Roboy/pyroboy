import rclpy
from roboy_cognition_msgs.srv import Talk, RecognizeSpeech

class ServiceClientDefinition:
    def __init__(self, type, name):
        self.type = type
        self.name = name

speech_synthesis_en_srv = ServiceClientDefinition(Talk, '/roboy/cognition/speech/synthesis/talk')
speech_synthesis_de_srv = ServiceClientDefinition(Talk, '/roboy/cognition/speech/synthesis/talk/german')
speech_recognition_srv = ServiceClientDefinition(RecognizeSpeech, '/roboy/cognition/speech/recognition')
