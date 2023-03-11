from pygame import mixer
def buzz():
 mixer.init() 
 sound=mixer.Sound("buzzer-or-wrong-answer-20582.mp3")
 sound.play()