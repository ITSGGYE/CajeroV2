from pad4pi import rpi_gpio
import time


class KeyPad:
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
				
	keypad.registerKeyPressHandler(printkey)

	try:
		while(True):
			time.sleep(0.2)
	except:
		keypad.cleanup()
