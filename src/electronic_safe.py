import time
from hal.hal_lcd import lcd  # Importing the LCD class from hal_lcd
from hal.hal_keypad import init as keypad_init, get_key  # Importing keypad functions
import RPi.GPIO as GPIO

# Constants
CORRECT_PIN = "1234"
MAX_ATTEMPTS = 3
BUZZER_PIN = 18  # GPIO pin for the buzzer

# State variables
input_pin = ""
attempts = 0
lcd_display = lcd()

def display_message(line1, line2=""):
    """
    Display a message on the LCD.
    """
    lcd_display.lcd_clear()
    lcd_display.lcd_display_string(line1, line=1)
    lcd_display.lcd_display_string(line2, line=2)

def activate_buzzer():
    """
    Activate the buzzer for 1 second to indicate a wrong PIN entry.
    """
    GPIO.output(BUZZER_PIN, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(BUZZER_PIN, GPIO.LOW)

def handle_keypress(key):
    """
    Callback function to handle keypad input.
    """
    global input_pin, attempts
    
    # Check if the safe is disabled (REQ-05)
    if attempts >= MAX_ATTEMPTS:
        display_message("Safe Disabled", "")
        return

    # Handle numeric key input (0-9) (REQ-02)
    if isinstance(key, int) or key == 0:
        input_pin += str(key)
        display_message("Safe Lock", "Enter PIN: " + "*" * len(input_pin))

    # Check PIN if '#' is pressed (REQ-03 and REQ-04)
    elif key == "#":
        if input_pin == CORRECT_PIN:
            # Correct PIN entered; display "Safe Unlocked" (REQ-03)
            display_message("Safe Unlocked", "")
            input_pin = ""  # Reset input after unlocking
            attempts = 0    # Reset attempts on successful unlock
        else:
            # Incorrect PIN entered; show "Wrong PIN" and activate buzzer (REQ-04)
            attempts += 1
            if attempts >= MAX_ATTEMPTS:
                display_message("Safe Disabled", "")  # REQ-05
            else:
                display_message("Wrong PIN", "")  # REQ-04
                activate_buzzer()
            input_pin = ""  # Reset input after incorrect attempt

    # Clear input if '*' is pressed (REQ-02 for clearing input)
    elif key == "*":
        input_pin = ""
        display_message("Safe Lock", "Enter PIN: ")

def main():
    """
    Main function to initialize the keypad, LCD, and buzzer, and start listening for input.
    """
    # Initialize GPIO for the buzzer
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUZZER_PIN, GPIO.OUT)
    GPIO.output(BUZZER_PIN, GPIO.LOW)  # Ensure the buzzer is initially off

    # Display the initial message as per REQ-01
    display_message("Safe Lock", "Enter PIN: ")

    # Initialize the keypad with handle_keypress as the callback function
    keypad_init(handle_keypress)

    # Run the keypad scanning function continuously
    try:
        get_key()  # This will keep the program running to handle keypad input
    except KeyboardInterrupt:
        print("Exiting Program")
    finally:
        GPIO.cleanup()  # Clean up GPIO on exit

if __name__ == "__main__":
    main()
