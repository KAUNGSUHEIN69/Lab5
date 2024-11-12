from threading import Thread
from time import sleep
from hal import hal_led as led


global delay
delay = 0  # Initialize delay to 0
running = False 

def led_thread():
    global delay, running
    while True:
        if running and delay > 0:
            print("LED ON") 
            led.set_output(24, 1)
            sleep(delay)
            print("LED OFF")  
            led.set_output(24, 0) 
            sleep(delay)
        else:
            led.set_output(24, 0)  
            sleep(0.1)  

def led_control_init():
    global running
    led.init()  
    running = True  
    t1 = Thread(target=led_thread, daemon=True)
    t1.start()
    print("LED control thread started") 

def set_blinking_mode(blink_delay=1):
    """Set the LED to blinking mode with the specified delay."""
    global delay, running
    delay = blink_delay  
    running = True  
    print(f"LED set to blink mode with delay: {delay} seconds") 

def stop_blinking():
    """Stop the LED from blinking."""
    global running
    running = False 
    led.set_output(24, 0) 
    
