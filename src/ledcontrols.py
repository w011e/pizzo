brightness = 100

def toggle_led_band():
    print("Toggle LED Band")

def increase_brightness():
    global brightness
    if brightness < 100:
        brightness += 5
        print(f"Increased brightness to {brightness}%")

def decrease_brightness():
    global brightness
    if brightness > 0:
        brightness -= 5
        print(f"Decreased brightness to {brightness}%")

def clear_leds():
    print("Clearing LEDs")