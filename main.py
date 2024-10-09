"""
TODO
GUI
display when playing: wrote test lines in display_frequency (rename func) need to replace with code that shows what note is 
extra buzzers
potentiometer input
"""

import time
from pimoroni import Buzzer
from pimoroni import Button
from picographics import PicoGraphics, DISPLAY_PICO_EXPLORER, PEN_P4
display = PicoGraphics(display=DISPLAY_PICO_EXPLORER, pen_type=PEN_P4)
import sys

BLACK = display.create_pen(0, 0, 0)
WHITE = display.create_pen(255, 255, 255)
BUZZER = Buzzer(0)
#bps = 0.1 # beats per second
notei = 0

button_a = Button(12)
button_b = Button(13)
button_x = Button(14)
button_y = Button(15)

string6 = {"0" : 82,
           "1" : 87,
           "2" : 92,
           "3" : 98,
           "4" : 104,
           "5" : 110,
           "6" : 117,
           "7" : 123,
           "8" : 131,
           "9" : 139,
           "10" : 147,
           "11" : 156,
           "12" : 165,
           "13" : 175,
           "14" : 185,
           "15" : 196,
           "16" : 208,
           "17" : 220,
           "18" : 233,
           "19" : 247,
           "20" : 262,
           "p" : -1}
    

string5 = {"0" : 110,
           "1" : 117,
           "2" : 123,
           "3" : 131,
           "4" : 139,
           "5" : 147,
           "6" : 156,
           "7" : 165,
           "8" : 175,
           "9" : 185,
           "10" : 196,
           "11" : 208,
           "12" : 220,
           "13" : 233,
           "14" : 247,
           "15" : 262,
           "16" : 277,
           "17" : 294,
           "18" : 311,
           "19" : 330,
           "20" : 34,
           "p" : -1}

string4 = {"0" : 147,
           "1" : 156,
           "2" : 165,
           "3" : 175,
           "4" : 185,
           "5" : 196,
           "6" : 208,
           "7" : 220,
           "8" : 233,
           "9" : 247,
           "10" : 262,
           "11" : 277,
           "12" : 294,
           "13" : 311,
           "14" : 330,
           "15" : 349,
           "16" : 370,
           "17" : 392,
           "18" : 415,
           "19" : 440,
           "20" : 466,
           "p" : -1}

string3 = {"0" : 196,
           "1" : 208,
           "2" : 220,
           "3" : 233,
           "4" : 247,
           "5" : 262,
           "6" : 277,
           "7" : 294,
           "8" : 311,
           "9" : 330,
           "10" : 349,
           "11" : 370,
           "12" : 392,
           "13" : 415,
           "14" : 440,
           "15" : 466,
           "16" : 494,
           "17" : 523,
           "18" : 554,
           "19" : 587,
           "20" : 622,
           "p" : -1}

string2 = {"0" : 247,
           "1" : 262,
           "2" : 277,
           "3" : 294,
           "4" : 311,
           "5" : 330,
           "6" : 349,
           "7" : 370,
           "8" : 392,
           "9" : 415,
           "10" : 440,
           "11" : 466,
           "12" : 494,
           "13" : 523,
           "14" : 554,
           "15" : 587,
           "16" : 622,
           "17" : 659,
           "18" : 698,
           "19" : 740,
           "20" : 784,
           "p" : -1}

string1 = {"0" : 330,
           "1" : 349,
           "2" : 370,
           "3" : 392,
           "4" : 415,
           "5" : 440,
           "6" : 466,
           "7" : 494,
           "8" : 523,
           "9" : 554,
           "10" : 587,
           "11" : 622,
           "12" : 659,
           "13" : 698,
           "14" : 740,
           "15" : 784,
           "16" : 831,
           "17" : 880,
           "18" : 932,
           "19" : 988,
           "20" : 1047,
           "p" : -1}


song1 = ["p", "p", "p", "p", "p", "p", "p", "p",  "p",  "p", "p", "p", "p", "p", "p", "p", "p", "p","p", "p", "p", "p", "5", "5", "p", "p",  "p",  "p", "5", "p", "p", "p", "p", "p", "p", "p"]
song2 = ["7", "p", "p", "7", "7", "9", "9", "10", "10", "9", "9", "7", "7", "9", "9", "5", "p", "p","5", "5", "7", "7", "p", "p", "7", "7",  "5",  "5", "p", "5", "p", "p", "p", "p", "p", "p"]
song3 = ["p", "7", "7", "p", "p", "p", "p", "p",  "p",  "p", "p", "p", "p", "p", "p", "p", "5", "5","p", "p", "p", "p", "p", "p", "p", "p",  "p",  "p", "p", "p", "p", "p", "p", "p", "p", "p"]
song4 = ["p", "p", "p", "p", "p", "p", "p", "p",  "p",  "p", "p", "p", "p", "p", "p", "p", "p", "p","p", "p", "p", "p", "p", "p", "p", "p",  "p",  "p", "p", "p", "7", "7", "p", "p", "7", "7"]
song5 = ["p", "p", "p", "p", "p", "p", "p", "p",  "p",  "p", "p", "p", "p", "p", "p", "p", "p", "p","p", "p", "p", "p", "p", "p", "p", "p",  "p",  "p", "p", "p", "p", "p", "7", "7", "p", "p"]
song6 = ["p", "p", "p", "p", "p", "p", "p", "p",  "p",  "p", "p", "p", "p", "p", "p", "p", "p", "p","p", "p", "p", "p", "p", "p", "p", "p",  "p",  "p", "p", "p", "p", "p", "p", "p", "p", "p"]


display.set_font("bitmap8")



def clear():
    display.set_pen(BLACK)
    display.clear()
    display.update()
    

def display_frequency(frequency):
    display.text(str(frequency),10, 10, 240, 3) #prints current frequency on screen
    display.update()
    

def play_tone(frequency):			#sets the buzzer frequency
    #print(frequency)  #only uncomment this line to troubleshoot
    if frequency != -1:
        display_frequency(frequency)
        BUZZER.set_tone(frequency)


def display_strings(string1, string2, string3, string4, string5, string6): #this does not feel like the right way to do this but not got a better one right now
    clear()
    display.set_pen(WHITE) 
    display.text(f"{string1}",10,40,240,3)
    display.text(f"{string2}",10,70,240,3)
    display.text(f"{string3}",10,100,240,3)
    display.text(f"{string4}",10,130,240,3)
    display.text(f"{string5}",10,160,240,3)
    display.text(f"{string6}",10,190,240,3)
   # notei = notei + 1
   
   
def bequiet():                     # this function make quiet
    BUZZER.set_tone(-1)
    

def gui():
    while True:
        if button_a.read():
            print('a')
            main()
        elif button_b.read():
            print('b')
        elif button_x.read():
            print('x')
        elif button_y.read():
            print('y')
        pot = machine.ADC(26)
        bps = pot.read_u16()/10000
        print(bps)
        time.sleep(0.5)
        display.set_pen(WHITE)
        display.clear
        display.text(f"{string1}",10,40,240,3)
        display.text(f"{string2}",10,70,240,3)
        display.text(f"{string3}",10,100,240,3)
        display.text(f"{string4}",10,130,240,3)
        display.text(f"{string5}",10,160,240,3)
        display.text(f"{string6}",10,190,240,3)
        display.update
    


def main():
    for i in range(len(song2)):
        display_strings((song1[i]), (song2[i]), (song3[i]), (song4[i]), (song5[i]), (song6[i]), )#sets text for string played, screen update called within show frequency within play_tone
        play_tone(string1[song1[i-1]])
        play_tone(string2[song2[i-1]])
        play_tone(string3[song3[i-1]])
        play_tone(string4[song4[i-1]])
        play_tone(string5[song5[i-1]])
        play_tone(string6[song6[i-1]])
        time.sleep(bps)
        bequiet()
        #time.sleep(bps/2)
        
gui()



