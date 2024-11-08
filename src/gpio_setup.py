import RPi.GPIO as GPIO

def setup_gpio():
    # Set the GPIO mode to BCM
    GPIO.setmode(GPIO.BCM)
    
    GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Button 1
    GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Button 2
    GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Button 3
    GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Switch for LED band

    print("GPIO setup complete.")