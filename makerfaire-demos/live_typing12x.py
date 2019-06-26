#'''
#Live typing demo for Maker Faire Berlin 2018

#This class enables visitors to type on a USB-Keyboard connected to the 
#control laptop and have the typed text appear on the 30x30 
#WS2812-LED-Display immediately (5 letters per line with three lines).

#This demo was programmed during the exhibition.

#By using pygame, it also provides a live view of the current display 
#for the operator - after all, we had a lot of kids on the faire and 
#needed to make sure they didn't type anything 'spicy' ;-)

#Also, it was kinda cool to be able to see what's being displayed right 
#now as opposed to having to walk around to see the front of the 
#display. It allowed for some 'fake artificial intelligence' chatting 
#with visitors ;)

#@author Thomas Hoffmann
#@date 27-05-2018

#'''

import pygame, time
import pygame.display
from random import randint

from neopixel import *
from PIL import ImageDraw, ImageFont, Image


#### set up the LED strip
LED_COUNT      = 128      # Number of LED pixels.
LED_PIN        = 21      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transi
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
strip.begin()

print ('Press Ctrl-C to quit.')

#### set up pygame
pygame.init()
pygame.display.init()
screen = pygame.display.set_mode((8,8)) # create a 50x50 px window

## list of bad words to immediately remove from the display after being typed
badwords = ["AMK", "lots of bad words"]

# use this font to render text
fnt = ImageFont.truetype('/usr/share/fonts/truetype/led_8x6/led_8x6.ttf', 8)

# other variables
str1 = ""
str2 = ""
str3 = ""
cnt = 0
letter = ""
idle = 0
redraw = False

def displayGIF(strip, imageName, wait_ms=500):
#	'''
#	Helper function to render GIF files for the display
#	requires the GIFs to have the same dimensions as the display
#	'''
    im = Image.open(imageName)
    width = im.size[0]
    height = im.size[1]
    
    try:
        while 1:
            buf = im.convert('RGB')
            i = 0
            for y in range(0, height):
                for x in range(0, width):
                  if y%2 != 0:
                      r,g,b = buf.getpixel((x,y))
                  else:
                      r,g,b = buf.getpixel((x,y))
        
                  strip.setPixelColor(i, Color(r, g, b))
                  i += 1
            strip.show()
            im.seek(im.tell()+1)
			
			## this part converts the display contents for the preview window
            imgString = buf.tobytes()
            pygame_surface = pygame.image.fromstring(imgString, (0,0), 'RGB')
            screen.blit(pygame_surface, (0,0))
            pygame.display.flip()
            ## end of part
            
            time.sleep(im.info["duration"]/1000.0)
    except EOFError:
      pass # end of sequence

def reset_screen():
#	''' reset strings to empty '''
    global str1
    str1 = ""
#    str2 = ""
#    str3 = ""

def print_screen():
#	''' take current image data and display it on the LED strip '''
    global im
    i = 0
    for y in range(0, 8):
        for x in range(0, 16):
            if y%2 != 0:
                r,g,b = im.getpixel((x,y))
            else:
                r,g,b = im.getpixel((x,y))
            strip.setPixelColor(i, Color(r,g,b))
            i += 1
    imgString = im.tobytes()
    pygame_surface = pygame.image.fromstring(imgString, (8,16), 'RGB')
    pygame_surface = pygame.transform.rotate(pygame_surface, -90)
    screen.blit(pygame_surface, (0,0))
    pygame.display.flip()
    strip.show()


while True:
	# create new image every iteration
    im = Image.new('RGB', (8, 16), color = (0,0,0))
    d = ImageDraw.Draw(im)
    
    # does the screen need to be reprinted? (relevant for profanity filter)
    if redraw:
        redraw = False
        pygame.time.wait(500)
        print_screen()
    
    for event in pygame.event.get():
		# capture keypress events
        if (event.type == pygame.KEYDOWN):
            idle = 0
            if (event.key == pygame.K_a):
                letter = "A"
            if (event.key == pygame.K_b):
                letter = "B"
            if (event.key == pygame.K_c):
                letter = "C"
            if (event.key == pygame.K_d):
                letter = "D"
            if (event.key == pygame.K_e):
                letter = "E"
            if (event.key == pygame.K_f):
                letter = "F"
            if (event.key == pygame.K_g):
                letter = "G"
            if (event.key == pygame.K_h):
                letter = "H"
            if (event.key == pygame.K_i):
                letter = "I"
            if (event.key == pygame.K_j):
                letter = "J"
            if (event.key == pygame.K_k):
                letter = "K"
            if (event.key == pygame.K_l):
                letter = "L"
            if (event.key == pygame.K_m):
                letter = "M"
            if (event.key == pygame.K_n):
                letter = "N"
            if (event.key == pygame.K_o):
                letter = "O"
            if (event.key == pygame.K_p):
                letter = "P"
            if (event.key == pygame.K_q):
                letter = "Q"
            if (event.key == pygame.K_r):
                letter = "R"
            if (event.key == pygame.K_s):
                letter = "S"
            if (event.key == pygame.K_t):
                letter = "T"
            if (event.key == pygame.K_u):
                letter = "U"
            if (event.key == pygame.K_v):
                letter = "V"
            if (event.key == pygame.K_w):
                letter = "W"
            if (event.key == pygame.K_x):
                letter = "X"
            if (event.key == pygame.K_y):
                letter = "Z"
            if (event.key == pygame.K_z):
                letter = "Y"
            if (event.key == pygame.K_0):
                letter = "0"
            if (event.key == pygame.K_1):
                letter = "1"
            if (event.key == pygame.K_2):
                letter = "2"
            if (event.key == pygame.K_3):
                letter = "3"
            if (event.key == pygame.K_4):
                letter = "4"
            if (event.key == pygame.K_5):
                letter = "5"
            if (event.key == pygame.K_6):
                letter = "6"
            if (event.key == pygame.K_7):
                letter = "7"
            if (event.key == pygame.K_8):
                letter = "8"
            if (event.key == pygame.K_9):
                letter = "9"
            if (event.key == pygame.K_SPACE):
                letter = " "
            if (event.key == pygame.K_BACKSPACE):
                print("backspace")
                reset_screen()
                print_screen()
                cnt = 0
                break
            if (event.key == pygame.K_RETURN):
                if (cnt < 2):
                    cnt = 0
#                if (cnt > 5 and cnt < 10):
#                    cnt = 9
                if (cnt > 0 and cnt <= 2):
                    cnt = -1
                    str1 = str2 = str3 = ""
                    letter = ""
                    break
            if (event.key != pygame.K_RETURN and letter == ""):
                break

            if (cnt >= 1):
                cnt = 0
                str1 = ""
#                str2 = ""
#                str3 = ""
                
            cnt += 1
            
            if (cnt > 1):
                cnt = 0
                str1 = ""
                str2 = ""
                str3 = ""
                
            if (event.key == pygame.K_RETURN):
                continue
                
            if (cnt <= 2):
                str1 = "{}{}".format(str1, letter)
                print("Adding letter {} to line 1".format(letter))
#            if (cnt > 5 and cnt <= 10):
#                str2 = "{}{}".format(str2, letter)
#                print("Adding letter {} to line 2".format(letter))
#            if (cnt > 10 and cnt <= 15):
#                str3 = "{}{}".format(str3, letter)
#                print("Adding letter {} to line 3".format(letter))
                
            letter = ""
            d.text((0,0), str1, font=fnt, fill=(255,255,255))
#            d.text((0,10), str2, font=fnt, fill=(255,255,255))
#            d.text((0,20), str3, font=fnt, fill=(255,255,255))
            print("Line 1: {}".format(str1))
#            print("Line 2: {}".format(str2))
#            print("Line 3: {}".format(str3))
            print(" ")
            
            profanity = "{}{}{}".format(str1,str2,str3)
            
            for word in badwords:
                if (word in profanity):
                    print ("Found a naughty word - resetting! - {}".format(profanity))
                    reset_screen()
                    cnt = 0
                    im.paste((255,0,0), [0,0,30,30])
                    redraw = True

			# have a couple of easter eggs to surprise visitors if they type this word (abusing the profanity-filter functionality)
            if ("PONG" in profanity):
                print("Pong animation")
                displayGIF(strip, "pong.gif")
                reset_screen()
                cnt = 0
                print("EOA")

            if ("BADAPPLE" in profanity):
                print("Bad Apple Animation")
                strip.setBrightness(100)
                displayGIF(strip, "badapple.gif")
                strip.setBrightness(LED_BRIGHTNESS)
                reset_screen()
                cnt = 0
                print("EOA")
            
            if ("MAKERFAIRE" in profanity):
                print("MakerFaire Animation") 
                displayGIF(strip, "makerfaire.gif")
                reset_screen()
                cnt = 0
                print("EOA")  
                
            if ("BREADBOARD" in profanity):
                print("Breadboarder Animation")
                displayGIF(strip, "breadboarder_top.gif")
                reset_screen()
                cnt = 0
                print("EOA")
                
            print_screen()
            
    # have an idle animation to attract visitors when nothing's been typed for a while
    if (idle > 5000):
        displayGIF(strip, "gifs/breadboarder_top.gif")
        displayGIF(strip, "gifs/breadboarder_bottom.gif")
        displayGIF(strip, "pong.gif")
        pygame.time.wait(300)
        displayGIF(strip, "gifs/type.gif")
        idle = -5000
        str1 = "TYPE"
        str2 = "HERE"
        str3 = " NOW"
        im = Image.new('RGB', (30, 30), color = (0,0,0))
        d = ImageDraw.Draw(im)
        d.text((0,0), str1, font=fnt, fill=(255,255,255))
        d.text((0,10), str2, font=fnt, fill=(255,255,255))
        d.text((0,20), str3, font=fnt, fill=(255,255,255))
        print_screen()
        reset_screen()
        cnt = 0
        
    idle += 1
    pygame.time.wait(10)
