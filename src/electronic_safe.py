from time import sleep
from threading import Thread
from hal import hal_keypad as keypad
from hal import hal_lcd as LCD
from hal import hal_buzzer as buzzer

lcd = LCD.lcd()
correct_pin = "1234"
entered_pin = ""
attempts = 0

def display_safe_lock():
    lcd.lcd_clear()
    lcd.lcd_display_string("Safe Lock", 1)
    lcd.lcd_display_string("Enter PIN: ", 2)

def display_wrong_pin():
    lcd.lcd_clear()
    lcd.lcd_display_string("Wrong PIN", 1)
    buzzer.turn_on_with_timer(1)

def display_safe_unlocked():
    lcd.lcd_clear()
    lcd.lcd_display_string("Safe Unlocked", 1)

def display_safe_disabled():
    lcd.lcd_clear()
    lcd.lcd_display_string("Safe Disabled", 1)

def key_pressed(key):
    global entered_pin, attempts

    key = str(key)
    print(f"Key pressed: '{key}'")

    # Add key to entered PIN and display asterisk after "Enter PIN: "
    if len(entered_pin) < 4:
        entered_pin += key
        lcd.lcd_display_string("Enter PIN: ", 2)  # Display prompt on line 2
        lcd.lcd_display_string("*" * len(entered_pin), 2, pos=10)  # Display asterisks starting at position 10

    # Check if the PIN is complete
    if len(entered_pin) == 4:
        if entered_pin == correct_pin:
            display_safe_unlocked()
            entered_pin = ""
        else:
            attempts += 1
            entered_pin = ""
            if attempts >= 3:
                display_safe_disabled()
            else:
                display_wrong_pin()
                display_safe_lock()

def main():
    display_safe_lock()
    keypad.init(key_pressed)
    buzzer.init()

    keypad_thread = Thread(target=keypad.get_key)
    keypad_thread.start()

    try:
        while True:
            sleep(1)
    except KeyboardInterrupt:
        print("Program exited cleanly.")

if __name__ == "__main__":
    main()
