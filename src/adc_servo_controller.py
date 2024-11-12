from threading import Thread
from hal import hal_adc as adc
from hal import hal_servo as servo
from time import sleep
import RPi.GPIO as GPIO

def control_servo_from_adc():
    adc.init()
    servo.init()
    try:
        while True:
            adc_value = adc.get_adc_value(0)  
            servo_position = (adc_value / 1023) * 180  
            print("ADC Value: {}, Servo Position: {}".format(adc_value, servo_position))
            servo.set_servo_position(servo_position)  
            sleep(0.1)  
    except KeyboardInterrupt:
        print("Exiting Program")
    finally:
        GPIO.cleanup()  # Cleanup GPIO on exit

# Run the main function
control_servo_from_adc()