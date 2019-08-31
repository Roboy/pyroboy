import rospy
import time
from pyroboy.speech_synthesis import TTS
from pyroboy.speech_recognition import STT
from pyroboy.common_definitions import emotion_pub, leds_pub

class Pyroboy():
    def __init__(self):
        self.tts = None
        self.stt = None
        self.emotion_publisher = None
        self.leds_publisher = None


    def init_tts(self):
        self.tts = TTS()

    def init_stt(self):
        self.stt = STT()

    def init_face(self):
        self.emotion_publisher = rospy.Publisher(emotion_pub.name, emotion_pub.type, queue_size=1)

    def init_matrix(self):
        self.leds_publisher = rospy.Publisher(leds_pub.name, leds_pub.type, queue_size=1)



listen_start_timestamp = 0
say_end_timestamp = 0

def say(text, language="en"):
    rospy.set_param('talking', True)
    if pr.tts is None:
        pr.init_tts()
    result = pr.tts.generate(text, language)
    rospy.set_param('talking', False)
    return result

def listen(discard_on_say=False):
    if pr.stt is None:
        pr.init_stt()
    global say_end_timestamp
    listen_start_timestamp = time.time()
    result_text = pr.stt.recognize_speech()
    # Discard text that was recorded while speech synthesis was running
    if discard_on_say and say_end_timestamp > listen_start_timestamp:
        print("Discarded: " + str(result_text))
        result_text = None
    return result_text

def show_emotion(emotion):
    if pr.emotion_publisher is None:
        pr.init_face()
    msg = emotion_pub.type(emotion=emotion)
    return pr.emotion_publisher.publish(msg)

def leds(mode="off"):
    if pr.leds_publisher is None:
        pr.init_matrix()
    if mode == "pulse":
        mode_id = 1
    elif mode == "rainbow":
        mode_id = 4
    elif mode == "tail":
        mode_id = 2
    elif mode == "police":
        mode_id = 3
    else:
        mode_id = 0
        print("unknow mode for matrix leds")
    pr.leds_publisher.publish(mode_id)


rospy.init_node('pyroboy')
pr = Pyroboy()
