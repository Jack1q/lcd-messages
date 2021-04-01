""" 
This is the script that will be run on the Pi to fetch the message being displayed.
"""
import requests
import time
from lcd_display import lcd

my_lcd = lcd()
my_lcd.backlight(0)

def update_lcd():
    """
    Updates lcd screen to show most recently submitted message from web app.
        * Remember to change the URL after web app goes live. *
    """
    while True:
        message = requests.get('http://127.0.0.1:5000/message').text
        my_lcd.lcd_display_string(message, 2)
        time.sleep(3)


if __name__ == '__main__':
    update_lcd()