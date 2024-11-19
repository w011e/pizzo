import RPi.GPIO as GPIO
import time
import ledcontrols, display

BUTTON_1_PIN = 25       # Show time
BUTTON_2_PIN = 22       # Show alarm time
LEVER_SWITCH_PIN = 27   # Toggle LED Band
BUTTON_4_PIN = 17       # Increase brightness
BUTTON_5_PIN = 4        # Decrease brightness

def setup_buttons():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_1_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BUTTON_2_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(LEVER_SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BUTTON_4_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BUTTON_5_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def check_buttons():
    if GPIO.input(BUTTON_1_PIN) == GPIO.LOW:
        display.print_time()
    if GPIO.input(BUTTON_2_PIN) == GPIO.LOW:
        display.show_alarm_time()
    if GPIO.input(LEVER_SWITCH_PIN) == GPIO.LOW:
        ledcontrols.toggle_led_band()
    if GPIO.input(BUTTON_4_PIN) == GPIO.LOW:
        ledcontrols.increase_brightness()
    if GPIO.input(BUTTON_5_PIN) == GPIO.LOW:
        ledcontrols.decrease_brightness()
        
if __name__ == "__main__":
    setup_buttons()
    try:
        while True:
            check_buttons()
            time.sleep(0.1)  
    except KeyboardInterrupt:
        print("Exiting...")
        GPIO.cleanup()
