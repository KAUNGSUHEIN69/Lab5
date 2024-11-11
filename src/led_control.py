from hal import hal_led as led
from threading import Thread
from time import sleep

from hal import hal_keypad as keypad

led.init()

def led_thread():
    global delay
    delay = 0
    while(True):
        if delay != 0:
            led.set_output(20, 1)
            sleep(delay)
            led.set_output(20, 0)
            sleep(delay)

def led_control_init():
    global delay
    t1 = Thread(target=led_thread)
    t1.start()
    #Set initial LED blinking every 1 second after Thread starts
    delay = 1

