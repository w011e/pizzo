import display
import ledcontrols
import buttonsetup
import time, os

def stop_audio():
    # Stop shairport-sync (AirPlay)
    os.system("sudo systemctl stop shairport-sync")

    # You may need to add commands to stop Bluetooth audio if playing
    # Example: You can use `pactl` commands to control audio playback

# Function to start/resume AirPlay and Bluetooth audio
def start_audio():
    # Start shairport-sync (AirPlay)
    os.system("sudo systemctl start shairport-sync")

    # You may need to add commands to resume Bluetooth audio if needed

def main():
    setup_buttons()
    print("Buttons are Ready!")  
    
    try:
        while True:
            buttons.check_buttons()
            time.sleep(0.1)  
    except KeyboardInterrupt:
        print("Shutting down...")
        buttons.GPIO.cleanup()
        clear_leds()

if __name__ == "__main__":
    main()
