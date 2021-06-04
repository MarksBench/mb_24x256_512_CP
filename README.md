# mb_24x256_512_CP
Very simple CircuitPython module/driver for Microchip 24x256 and 24x512 I2C EEPROM devices. Works with RP2040 (tested on Raspberry Pi Pico), should run on other microcontrollers that have hardware or software I2C and run CircuitPython 6.2.

This module is intended to make using the 24x256/512 as simple as possible. It has the following functions:
- Write a value (range 0-255) to an EEPROM address (range 0-32767 for the 24x256, 0-65535 for the 24x512)
- Read a value from an EEPROM address, values are returned as integers (range 0-255)
- And that's it.

Author: mark@marksbench.com

Version: 0.1, 2021-06-01

**NOTE(1): There is no guarantee that this software will work in the way you expect (or at all). Use at your own risk.

**NOTE(2): You must call i2c.try_lock() and i2c.unlock() each time you call this driver. Make sure no other devices have the I2C bus locked when using the 24x256/512.

**NOTE(3): This driver is intended to be as simple as possible to use. As a result it does byte writes instead of page writes. *That means that each time you write a byte, the entire page is re-written in the EEPROM. This can/will wear the EEPROM significantly faster than doing a page write.* Other options are sequential writes or page writes, but they are not part of this driver.

**NOTE(4): Thanks to KJRC on the Adafruit forums for testing and providing feedback and ideas!

Prerequisites:
- RP2040 silicon (tested with Raspberry Pi Pico), should work with other MCUs with HW or SW I2C
- CircuitPython 6.2
- 24x256/512 connected to hardware I2C port 0 or port 1 pins, should also work with SW I2C


Usage:
- Set up I2C (software or hardware)
- Create constructor:
thisMemoryChipDeviceName = mb_24x256_512_CP.mb_24x256_512_CP(i2c, i2c_address, EEPROM_DEVICE)
where i2c_address is a base-10 value that corresponds to the 7-bit i2c address of the EEPROM, and where EEPROM_DEVICE is either "24x256" or "24x512"
- To write a single byte to an address:
  thisMemoryChipDeviceName.write_byte(address, value)
- To read a single byte from an address:
  thisMemoryChipDeviceName.read_byte(address)
  
For a simple example of setup and use, see mb_24x256_512_CP_example.py
  
For more information, consult the Raspberry Pi Pico Micropython SDK documentation at:
  https://datasheets.raspberrypi.org/pico/raspberry-pi-pico-python-sdk.pdf
  
and the CircuitPython documentation at:
  https://learn.adafruit.com/welcome-to-circuitpython
  
and the Microchip 24x256/512 datasheets at:
  https://www.microchip.com
