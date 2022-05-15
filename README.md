# PicoHourGlass
PicoHourGlass is based on the hourglass-on-pico project (link)

I've added comments to the code, as well as wiring schematics and 3D schematics for the housing

CircuitPython version 7.2.5

Components used:
1. Raspberry Pi Pico
2. ADXL345 accelerometer
3. 2x MAX 7219 based dot matrix displays

Libraries needed on the pico [Download From CircuitPython](https://circuitpython.org/libraries)
1. adafruit_bus_device
2. adafruit_max7219
3. adafruit_adxl34x
4. adafruit_framebuf

Create a folder on the Pico called lib, place all librarys from above inside the lib folder, your pico should have a folder layout similar to this when you are done

```
Pico Root
  * lib
    * adafruit_bus_device
      * i2c_device.py
      * spi_device.py
      * \__init\__.py
    * adafruit_max7219
      * bcddigits.py
      * matrices.py
      * \__init\__.py
    * adafruit_adxl34x.py
    * adafruit_framebuf.py
  * main.py
  * matrixsand.py
```

Original Code Project Forked From: 
 * [Orignial Reddit Post](https://www.reddit.com/r/RASPBERRY_PI_PROJECTS/comments/re3vue/hourglass_using_the_pi_pico_and_circuitpython/)
 * [Pelipooper GitHub](https://github.com/Pelipooper/hourglass-on-pico)

Original 3D Model & Code
  * [Thingiverse](https://www.thingiverse.com/thing:5184837)
  * [Youtube](https://www.youtube.com/watch?v=zHJjEaxN9Wg)
  * [Code](https://drive.google.com/drive/folders/1FmsJe3t4GnKt1Uj1wuZmlCyuoFlpcOao)

Useful Links:
  * [Adafruit Fritzing Library](https://github.com/adafruit/Fritzing-Library)