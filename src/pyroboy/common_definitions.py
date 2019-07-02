import rospy
from roboy_cognition_msgs.srv import Talk, TalkRequest, RecognizeSpeech, RecognizeSpeechRequest
from roboy_control_msgs.msg import Emotion

class RosHandlerDefinition:
    def __init__(self, type, request, name):
        self.type = type
        self.request = request
        self.name = name


speech_synthesis_en_srv = RosHandlerDefinition(Talk, TalkRequest, '/roboy/cognition/speech/synthesis/talk')
speech_synthesis_de_srv = RosHandlerDefinition(Talk, TalkRequest, '/roboy/cognition/speech/synthesis/talk/german')
speech_recognition_srv = RosHandlerDefinition(RecognizeSpeech, RecognizeSpeechRequest, '/roboy/cognition/speech/recognition')

emotion_pub = RosHandlerDefinition(Emotion, None, '/roboy/cognition/face/emotion')
