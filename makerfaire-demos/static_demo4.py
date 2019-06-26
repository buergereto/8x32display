# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.

# Extended by custom animations for Maker Faire Berlin 2018

import time

from neopixel import *
from PIL import Image, ImageDraw, ImageFont
import signal
import sys

def signal_handler(signal, frame):
		for i in range(0,900):
			strip.setPixelColor(i, Color(0,0,0))

		strip.show()
		print("Canceled Animations")
		sys.exit(0)

# LED strip configuration:
LED_COUNT      = 256     # Number of LED pixels.
LED_PIN        = 21      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering

def displayGIF(strip, imageName, wait_ms=500):
	''' Display a GIF identified by imageName frame by frame  '''

	im = Image.open(imageName)
	width = im.size[0]
	height = im.size[1]

	# To iterate through the entire gif
	try:
		while 1:
			buf = im.convert('RGB')
			i = 0

			for y in range(0, height):
				for x in range(0, width):
					if y%2 != 0:
						r,g,b = buf.getpixel((x,y))
					else:
						r,g,b = buf.getpixel((7-x,y))

					strip.setPixelColor(i, Color(r, g, b))
					i += 1
			strip.show()
			im.seek(im.tell()+1)
			time.sleep(im.info["duration"]/1000.0)
	except EOFError:
		pass # end of sequence

#displayJpeg(strip, imName, wait_ms=500):
#	''' Display a JPEG file given by imName '''
#	img = Image.open(imName)
#	size = img.size
#
#	buf = img.load()
#	i = 0
#	print("{},{}".format(size[0],size[1]))
#	print("{}".format(buf[0,0][0]))
#	for y in range(0, size[1]):
#		for x in range(0, size[0]):
#			if y%2 != 0:
#				strip.setPixelColor(i, Color(buf[7-x,y][0], buf[7-x,y][1], buf[7-x,y][2]))
#			else:
#				strip.setPixelColor(i, Color(buf[x,y][0], buf[x,y][1], buf[x,y][2]))
#			i += 1
#	strip.show()
#	time.sleep(5);

def pixelTest(strip):
	''' Flash the three base colors to quickly assess LED functionality '''
	
	strip.setBrightness(128) # we had to adjust brightness due to an underpowered power supply
	
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, Color(255,0,0))
	strip.show()
	time.sleep(1)
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, Color(0,255,0))
	strip.show()
	time.sleep(1)
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, Color(0,0,255))
	strip.show()
	time.sleep(1)
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, Color(0,0,0))
	strip.show()
	time.sleep(1)
	
	strip.setBrightness(LED_BRIGHTNESS) # restore LED_BRIGHTNESS setting
		


def theaterChase(strip, color, wait_ms=25, iterations=10):
	''' This function was predefined as part of the official python wrapper demo '''
	"""Movie theater light style chaser animation."""
	for j in range(iterations):
		for q in range(3):
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, color)
			strip.show()
			time.sleep(wait_ms/1000.0)
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, 0)
				

def wheel(pos):
	''' This function was predefined as part of the official python wrapper demo '''
	"""Generate rainbow colors across 0-255 positions."""
	if pos < 85:
		return Color(pos * 3, 255 - pos * 3, 0)
	elif pos < 170:
		pos -= 85
		return Color(255 - pos * 3, 0, pos * 3)
	else:
		pos -= 170
		return Color(0, pos * 3, 255 - pos * 3)


def rainbowCycle(strip, wait_ms=20, iterations=5):
	''' This function was predefined as part of the official python wrapper demo '''
	"""Draw rainbow that uniformly distributes itself across all pixels."""
	for j in range(256*iterations):
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
		strip.show()
		time.sleep(wait_ms/1000.0)
		
		

def dynamic(strip):
	''' This was my first attempt at rendering raw text on the display '''
	
	im = Image.new('RGB', (30, 30), color = (0,0,0))
	fnt = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf', 10)
	d = ImageDraw.Draw(im)
	d.text((0,0), "abcde", font=fnt, fill=(255,255,255))
	d.text((0,10), "fgehi", font=fnt, fill=(255,255,250))
	d.text((0,20), "jklmn", font=fnt, fill=(255,250,250))
	i = 0

	for y in range(0, 8):
		for x in range(0, 32):
			if y%2 != 0:
				r,g,b = im.getpixel((31-x,y))
			else:
				r,g,b = im.getpixel((x,y))
			strip.setPixelColor(i, Color(r,g,b))
			i += 1
	strip.show()
	time.sleep(5);


# Main program logic follows:
if __name__ == '__main__':

	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)

	# Intialize the library (must be called once before other functions).
	strip.begin()

	print ('Press Ctrl-C to quit.')

	while True:
		print ('Pixel Test')
		pixelTest(strip)

		print ('Breadb top')
		displayGIF(strip, "gifs/breadboarder_top.gif")
		strip.setBrightness(128)

		print ('White Theater')
		theaterChase(strip, Color(127, 127, 127), 60)  # White theater chase
		strip.setBrightness(LED_BRIGHTNESS)

		print ('Makerfaire')
		displayGIF(strip, "gifs/breadboarder_top.gif")


		print ('Red theater')
		strip.setBrightness(128)
		theaterChase(strip, Color(127,   0,   0), 60)  # Red theater chase
		strip.setBrightness(LED_BRIGHTNESS)

		print ('Makerfaire Rainbow')
		displayGIF(strip, "gifs/breadboarder_top.gif")


		print ('Blue Theater')
		strip.setBrightness(128)
		theaterChase(strip, Color(  0,   0, 127), 60)  # Blue theater chase
		strip.setBrightness(LED_BRIGHTNESS)

		print ('Breadboarder bottom')
		displayGIF(strip, "gifs/breadboarder_top.gif")


		print ('Rainbowcycle')
		strip.setBrightness(128)
		rainbowCycle(strip, 1, 1)
		strip.setBrightness(LED_BRIGHTNESS)

		print ('Breadboarder rainbow')
		displayGIF(strip, "gifs/breadboarder_top.gif")

		print ('Color wheel')
		for i in range(0,3):
			displayGIF(strip, "gifs/breadboarder_top.gif")

		displayGIF(strip, "gifs/breadboarder_top.gif")
