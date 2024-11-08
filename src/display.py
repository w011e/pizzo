import board
import busio
from adafruit_ssd1306 import SSD1306_I2C
from PIL import Image, ImageDraw, ImageFont

i2c = busio.I2C(board.SCL, board.SDA)
display = SSD1306_I2C(128, 32, i2c)  # Adjust dimensions if needed

def clear_display():
    display.fill(0)
    display.show()

def show_message(message):
    clear_display()
    image = Image.new("1", (display.width, display.height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    draw.text((0, 0), message, font=font, fill=255)
    display.image(image)
    display.show()

if __name__ == "__main__":
    show_message("Hello, Pi Zero!")
