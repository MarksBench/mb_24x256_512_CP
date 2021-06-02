"""
mb_24x256_512_CP_example.py

Example CircuitPython script for Microchip 24x256 and 24x512 I2C EEPROMs.

Tested with Raspberry Pi Pico (RP2040), should work with other CP-capable microcontrollers
with software or hardware I2C

Author: mark@marksbench.com

Version: 0.1, 2021-06-01

**NOTE(1): There is no guarantee that this software will work in the way you expect (or at all).
**Use at your own risk.

**NOTE(2): You must call i2c.try_lock() and i2c.unlock() each time you call this driver.
**Make sure no other devices have the I2C bus locked when using the 24x256/512.

**NOTE(3): This driver is intended to be as simple as possible to use. As a result it
**does byte writes instead of page writes. That means that each time you write a byte,
**the entire page is re-written in the EEPROM. This can/will wear the EEPROM significantly
**faster than doing a page write. Other options are sequential writes or saving data in RAM
**and writing them 128 bytes at a time.

**NOTE(4): Thanks to KJRC on the Adafruit forums for testing and providing ideas and feedback!


To use:
- Upload the mb_24x256_512_CP.py file to the lib folder on your board (or whichever location
  you usually store libraries/drivers.
- Suggested connection for testing with Pi Pico (check your device for proper pinout):

24x256/512  |   Pi Pico
1 A0        |   Vss (38)
2 A1        |   Vss (38)
3 A2        |   Vss (38)
4 Vss       |   Vss (38)
5 SDA       |   GP0 (1)
6 SCL       |   GP1 (2)
7 WP        |   Vss (38)
8 Vcc       |   Vcc (36)

- Let the driver use the I2C address found by i2c.scan() or set i2c_address yourself.
- Uncomment the appropriate EEPROM_DEVICE line for the device you're using
- To write a value: memory.write_byte(address, value)
- To read a value: value = memory.read_byte(address)
- You should get an error if the address or value is out of range.

"""

import bitbangio
import busio
from board import *
import digitalio
import time
import mb_24x256_512_CP


# Set up I2C (using SCL=GP1 and SDA=GP0 on Raspberry Pi Pico (RP2040))
i2c = busio.I2C(GP1, GP0, frequency=100000)

time.sleep(.01)
i2c.try_lock()
time.sleep(.01)
i2c_address = i2c.scan()
print(i2c_address)

# If you know the 7-bit address of the device then you don't need to do a scan and can
# uncomment the following line and set it manually (don't forget to tie the 24x Ax pins
# to either Vcc or Vss!):
#i2c_address = 7_bit_address_of_your_device

# Now, set up the 24x256/512 driver. Uncomment the line in the following list that
# matches your device
#EEPROM_DEVICE = "24x256"
#EEPROM_DEVICE = "24x512"

# And between that and the I2C address above, should be good to go:
memory = mb_24x256_512_CP.mb_24x256_512_CP(i2c, i2c_address, EEPROM_DEVICE)


# Write an int of value 101 to address 12345
memory.write_byte(12345, 101)

# Now read it back and print it
read_value = memory.read_byte(12345)

print(read_value)
i2c.unlock() # Don't forget to unlock when you're done with it
# That's all there is to it

