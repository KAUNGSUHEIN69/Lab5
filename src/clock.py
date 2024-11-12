import time
from threading import Thread
from hal.hal_lcd import lcd  

# Initialize the LCD
lcd_display = lcd()

def update_display():
    """
    Update the LCD with the current time and date every second.
    The colons in the time display will blink every second.
    """
    colon_visible = True  # Toggle variable for blinking the colons

    while True:
        # Get the current local time and date
        local_time = time.localtime()
        time_string = time.strftime("%H:%M:%S", local_time)
        date_string = time.strftime("%d:%m:%Y", local_time)

        # Blink the colons every second
        if colon_visible:
            display_time = time_string
        else:
            display_time = time_string.replace(":", " ")  

        # Display the time and date on the LCD
        lcd_display.lcd_display_string(display_time, line=1)
        lcd_display.lcd_display_string(date_string, line=2)
        
        # Toggle the colon visibility
        colon_visible = not colon_visible
        
        # Wait for 1 second before updating
        time.sleep(1)

def main():
    """
    Main function to start the clock display on the LCD.
    """
    # Start the display update in a separate thread
    clock_thread = Thread(target=update_display)
    clock_thread.start()
    
    # Keep the main thread alive
    clock_thread.join()

if __name__ == "__main__":
    main()
