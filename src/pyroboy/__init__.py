import rospy
import time
from pyroboy.speech_synthesis import TTS
from pyroboy.speech_recognition import STT
from pyroboy.common_definitions import emotion_pub

class Pyroboy():
    def __init__(self):
        self.tts = None
        self.stt = None
        self.emotion_publisher = None


    def init_tts(self):
        self.tts = TTS()

    def init_stt(self):
        self.stt = STT()

    def init_face(self):
        self.emotion_publisher = rospy.Publisher(emotion_pub.name, emotion_pub.type, queue_size=1)



listen_start_timestamp = 0
say_start_timestamp = 0

def say(text, language="en"):
    if pr.tts is None:
        pr.init_tts()
    say_start_timestamp = time.time()
    return pr.tts.generate(text, language)

def listen(discard_on_say=True):
    if pr.stt is None:
        pr.init_stt()
    listen_start_timestamp = time.time()
    result_text = pr.stt.recognize_speech()
    # Discard text that was recorded while speech synthesis was running
    if discard_on_say and say_start_timestamp > listen_start_timestamp:
        result_text = None
    return result_text

def show_emotion(emotion):
    if pr.emotion_publisher is None:
        pr.init_face()
    msg = emotion_pub.type(emotion=emotion)
    return pr.emotion_publisher.publish(msg)

rospy.init_node('pyroboy')
pr = Pyroboy()
