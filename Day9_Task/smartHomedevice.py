# Smart Home Devices (Multiple Inheritance) 

class WifiDevice:
    def wifi(self):
        print("Wifi Connectivity Available")

class VoiceAssistant:
    def voice(self):
        print("Voice Control Available")

class SmartSpeaker(WifiDevice, VoiceAssistant):
    def display(self):
        print("Smart Speaker Features")

s = SmartSpeaker()

s.display()
s.wifi()
s.voice()