import time
import board
import matrixsand
import busio
import adafruit_adxl34x
import digitalio
from adafruit_max7219 import matrices

# DIN Pin Matrix #1
MOSI = board.GP11
# DIN Pin Matrix #2
MOSI2 = board.GP19

# CLK Pin Matrix #1
clk = board.GP10
# CLK Pin Matrix #2
clk2 = board.GP18

# CS Pin Maxtrix #1
cs1 = digitalio.DigitalInOut(board.GP15)
# CS Pin Maxtrix #2
cs2 = digitalio.DigitalInOut(board.GP14)

# Setup SPI buses
spi1=busio.SPI(clk,MOSI=MOSI)
spi2=busio.SPI(clk2,MOSI=MOSI2)

DELAY = 0.00

# Setup I2C for the Accelo and define the accelo
i2c = busio.I2C(scl=board.GP1, sda=board.GP0)
accelo = adafruit_adxl34x.ADXL345(i2c)

# the matrix
# using different buses here, same bus would cause the bottom display glitch out sometimes
matrix1 = matrices.Matrix8x8(spi1, cs1)
matrix2 = matrices.Matrix8x8(spi2, cs2)

# the sand
sand1 = matrixsand.MatrixSand(8, 8)
sand2 = matrixsand.MatrixSand(8, 8)

# global brightness adjustment
matrix1.brightness(3)
matrix2.brightness(3)

# matrix updater
def update_matrix1():
    for x in range(8):
        for y in range(8):
            matrix1.pixel(x,y,sand1[x,y])
    matrix1.show()

def update_matrix2():
    for x in range(8):
        for y in range(8):
            matrix2.pixel(x,y,sand2[x,y])
    matrix2.show()

# fill up some initial sand
for sx in range(8):
    for sy in range(8):
        sand1[sx, sy] = True
sand1[0,0] = sand1[0,1] = sand1[1,0] = False
sand1[0,2] = sand1[1,1] = sand1[2,0] = False
update_matrix1()
update_matrix2()

updated1 = updated2 = False
# loop forever
while True:
    # read accelo
    ax, ay, az = accelo.acceleration
    # rotate coords
    # you might need to change the sign of ax and ay depending on the orientation of the sensor
    xx = ax - ay
    yy = ax + ay
    zz = az

    # move grain of sand from upper to lower?
    if yy > 0 and sand1[7,7] and not sand2[0,0] and not updated2:
        sand1[7,7] = False
        sand2[0,0] = True
        updated1 = updated2 = True
    # move grain of sand from lower to upper?
    elif yy <= 0 and sand2[0,0] and not sand1[7,7] and not updated1:
        sand2[0,0] = False
        sand1[7,7] = True
        updated1 = updated2 = True
    # nope, just a regular update
    else:
        updated1 = sand1.iterate((xx, yy, zz))
        updated2 = sand2.iterate((xx, yy, zz))

    # update matrices if needed
    if updated1:
        update_matrix1()
    if updated2:
        update_matrix2()

    time.sleep(DELAY)
