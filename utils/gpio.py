from pad4pi import rpi_gpio
import time


# Setup Keypad
KEYPAD = [
        ["3","2","1","A"],
        ["6","5","4","B"],
        ["9","8","7","C"],
        ["0",".","X","D"]
]

# same as calling: factory.create_4_by_4_keypad, still we put here fyi:
ROW_PINS = [16, 20, 21, 5] # BCM numbering; Board numbering is: 7,8,10,11 (see pinout.xyz/)
COL_PINS = [6, 13, 19, 26] # BCM numbering; Board numbering is: 12,13,15,16 (see pinout.xyz/)

factory = rpi_gpio.KeypadFactory()

# Try keypad = factory.create_4_by_3_keypad() or 
# Try keypad = factory.create_4_by_4_keypad() #for reasonable defaults
# or define your own:
keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)

def printkey(key):
	print(key)
	
	'''if(key=="1"):
		print("number")

	elif(key=="A"):
		print("letter")'''
		
		
keypad.registerKeyPressHandler(printkey)

try:
    while(True):
        time.sleep(0.2)
except:
    keypad.cleanup()


'''from time import sleep
#import RPi.GPIO as GPIO

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

print GPIO.RPI_INFO['P1_REVISION']




# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)

# set up GPIO output channel
GPIO.setup(16, GPIO.OUT)
#GPIO.setup(20, GPIO.OUT)
#GPIO.setup(21, GPIO.OUT)

while 1:
	sleep(1)
	GPIO.output(16, GPIO.HIGH)
	print "pause"
	sleep(1)


while 1:
    print GPIO.input()
    sleep(1)
    GPIO.output(40, GPIO.HIGH)
    sleep(1)

    GPIO.output(15, GPIO.LOW)
    sleep(1)
    GPIO.output(15, GPIO.HIGH)
    sleep(1)

    GPIO.output(16, GPIO.LOW)
    sleep(1)
    GPIO.output(16, GPIO.HIGH)
    sleep(1)
'''
