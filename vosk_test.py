import time
from googletrans import Translator
import pyttsx3
import pyaudio
from vosk import Model,KaldiRecognizer
from tools import Tools
from arabic_chat import Chat
import send_data

eng = pyttsx3.init()

english_model = r"D:\cours_II2\S2\PCD\chatbot\venv\models\vosk-model-small-en-us-0.15\vosk-model-small-en-us-0.15"
french_model = r"D:\cours_II2\S2\PCD\chatbot\venv\models\vosk-model-small-fr-0.22\vosk-model-small-fr-0.22"


class test():
    def __init__(self):
        self.text = None
        self.language = "en"

        self.english_model_path = english_model
        self.french_model_path = french_model
        self.count_silence = 0

        self.model_english = Model(self.english_model_path)
        self.recognizer_english = KaldiRecognizer(self.model_english, 16000)
        print("english model set successfully")


        # Initialize PyAudio instance and stream
        self.mic = pyaudio.PyAudio()
        self.stream = self.mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
        self.stream.start_stream()


    def speak(self,string):
        self.isSpeaking = True
        eng.say(string)
        eng.runAndWait()
        self.isSpeaking = False



    def get_command_en(self):
        listening = True
        while listening:
            data = self.stream.read(10240)
            try:
                if self.recognizer_english.AcceptWaveform(data):
                    result = self.recognizer_english.Result()
                    response = result[14:-3]
                    listening = False
                    if("open" in response):
                        self.speak("let's open and show our memories")
                        send_data.send_command("open")

                    if("close" in response):
                        self.speak("let's close our gallerie")
                        send_data.send_command("close")


                    return response
            except OSError:
                pass
            time.sleep(0.2)
        return ""


chat = test()
while 1 :
    print(chat.get_command_en())