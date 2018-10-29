#remote
from microbit import *
import radio


radio.on()
while True:
    

    if button_a.was_pressed():
        radio.send('Forward')
        display.scroll('F')
        
    
    if button_b.was_pressed():
        radio.send('Stop')
        display.scroll('S')
