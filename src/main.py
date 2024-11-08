import time
from buttons import setup_buttons, check_buttons
from display import show_message
from audio import play_audio
from led_ring import set_color, clear_leds
import RPi.GPIO as GPIO

def main():
    setup_buttons()
    show_message("Ready!")
    
    try:
        while True:
            check_buttons()
            time.sleep(0.1)  # Main loop delay
    except KeyboardInterrupt:
        print("Shutting down...")
        GPIO.cleanup()
        clear_leds()

if __name__ == "__main__":
    main()
