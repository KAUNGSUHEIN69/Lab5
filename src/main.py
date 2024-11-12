from threading import Thread
from hal import hal_keypad as keypad
from hal import hal_lcd as LCD
import led_control
from time import sleep

# Initialize the LCD
lcd = LCD.lcd()
lcd.lcd_clear()
current_mode = None

def key_pressed(key):
    global current_mode
    if key == 1:  
        current_mode = "Blink"
        lcd.lcd_clear()
        lcd.lcd_display_string("LED Control", 1)
        lcd.lcd_display_string("Blink LED", 2)
        led_control.set_blinking_mode() 

    elif key == 0:  
        current_mode = "Off"
        lcd.lcd_clear()
        lcd.lcd_display_string("LED Control", 1)
        lcd.lcd_display_string("OFF LED", 2)
        led_control.stop_blinking()  

def main():
    # Display the initial text on the LCD as per REQ-01
    lcd.lcd_display_string("LED Control", 1)
    lcd.lcd_display_string("0:Off 1:Blink", 2)
    keypad.init(key_pressed)
    keypad_thread = Thread(target=keypad.get_key)
    keypad_thread.start()

    led_control.led_control_init()

  

# Main entry point
if __name__ == "__main__":  
    main()
