import rclpy
from  pyroboy.speech_synthesis import TTS
from pyroboy.speech_recognition import STT

class Pyroboy():
    def __init__(self, node):
        self.node = node
        self.tts = None
        self.stt = None

    def init_tts(self):
        self.tts = TTS(self.node)

    def init_stt(self):
        self.stt = STT(self.node)

def say(text, language="en"):
    if pr.tts is None:
        pr.init_tts()
    return pr.tts.generate(text, language)

def listen():
    if pr.stt is None:
        pr.init_stt()
    return pr.stt.recognize_speech()

rclpy.init()
node = rclpy.create_node('pyroboy')
pr = Pyroboy(node)
