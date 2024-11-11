from hal import hal_adc as adc  
from hal import hal_servo
from time import sleep

# Map ADC value to servo angle (0-180 degrees)
def adc_to_servo_angle(adc_value):
    # Assuming adc_value ranges from 0 to 1023
    angle = (adc_value * 180) / 1023
    return angle

def main():
    hal_servo.init()  # Initialize the servo GPIO
    adc.init()  # Initialize the ADC

    while True:
            adc_value = adc.get_adc_value(1)
            servo_angle = adc_to_servo_angle(adc_value)
            hal_servo.set_servo_position(servo_angle)  # Set servo position based on angle
            print(f"ADC Value: {adc_value}, Servo Angle: {servo_angle}")
            sleep(0.1)
    
# Main entry point
if __name__ == "__main__":
    main()
