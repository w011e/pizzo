import RPi.GPIO as GPIO
import time

BUTTON_1_PIN = 17  # Show time
BUTTON_2_PIN = 27  # Show alarm time
BUTTON_3_PIN = 22  # Toggle LED Ring

def setup_buttons():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_1_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BUTTON_2_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BUTTON_3_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def check_buttons():
    if GPIO.input(BUTTON_1_PIN) == GPIO.LOW:
        print("Button 1 pressed: Show time")
        # Add functionality to display the current time on the OLED
    if GPIO.input(BUTTON_2_PIN) == GPIO.LOW:
        print("Button 2 pressed: Show alarm time")
        # Add functionality to display the alarm time on the OLED
    if GPIO.input(BUTTON_3_PIN) == GPIO.LOW:
        print("Button 3 pressed: Toggle LED Ring")
        # Add functionality to toggle the RGB LED Ring

if __name__ == "__main__":
    setup_buttons()
    try:
        while True:
            check_buttons()
            time.sleep(0.1)  # Small delay to debounce
    except KeyboardInterrupt:
        print("Exiting...")
        GPIO.cleanup()
