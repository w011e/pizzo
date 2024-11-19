from datetime import datetime
import time, board, busio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont

# Setup the display
WIDTH = 128
HEIGHT = 32  
BORDER = 5
i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)

# Clear the display
oled.fill(0)
oled.show()

# Create a blank image for drawing
image = Image.new("1", (WIDTH, HEIGHT))

# Get drawing object to draw on the image
draw = ImageDraw.Draw(image)

# Load a default font
font = ImageFont.load_default()

# Load a TrueType font and specify the size
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" 
font_size = 33
font = ImageFont.truetype(font_path, font_size)

def show_message(message):
    draw.rectangle((0, 0, WIDTH, HEIGHT), outline=0, fill=0)
    draw.text((11, 1), message, font=font, fill=255)
    oled.image(image)
    oled.show()
    time.sleep(15)  
    oled.fill(0)  
    oled.show()

def print_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    show_message(current_time)

def show_alarm_time():
    print("Alarm: 06:00")
