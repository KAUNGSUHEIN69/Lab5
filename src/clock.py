import time
import threading
from hal import hal_lcd as LCD

# Initialize LCD
lcd = LCD.lcd()

# Function to update the time on the LCD
def update_time():
    while True:
        # Get current time
        local_time = time.localtime()
        time_string = time.strftime("%H:%M:%S", local_time)
        date_string = time.strftime("%d:%m:%Y", local_time)

        # Display time and date on LCD
        lcd.lcd_clear()
        lcd.lcd_display_string(time_string, 1)
        lcd.lcd_display_string(date_string, 2)
        
        # Blink the colons
        time.sleep(0.5)
        lcd.lcd_display_string(time_string.replace(":", " "), 1)
        time.sleep(0.5)

# Main function to start the clock thread
def main():
    # Start a new thread to update the time on the LCD
    clock_thread = threading.Thread(target=update_time)
    clock_thread.daemon = True
    clock_thread.start()
    
    # Keep the main program running to allow the thread to continue
    while True:
        time.sleep(1)

# Main entry point
if __name__ == "__main__":
    main()
