from microbit import *
import radio

def stop():
    pin8.write_analog(1023)
    pin12.write_analog(1023)

def forward(speed):
    pin8.write_analog(speed)
    pin12.write_digital(0)
    display.scroll(speed)

    
speed = 100

radio.on()
while True:
    incoming = radio.receive()
    if incoming == 'Forward':
        display.scroll('FW GO')
        #Cycles = 0
        #while Cycles < 4:
        forward(300)
            #sleep(10)
        forward(185)
        #sleep(10000)
        #Cycles = Cycles +1
    
    if button_b.was_pressed() or incoming == 'Stop':
        display.scroll('FW stop')
        stop()
