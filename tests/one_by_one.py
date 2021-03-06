import sys
import time
import board
import neopixel
 
 
# Choose an open pin connected to the Data In of the NeoPixel strip
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D21
 
# The number of NeoPixels: 8x8=64
num_pixels = 64
 
# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB
 
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.01, auto_write=False, pixel_order=ORDER
)

if __name__ == '__main__':
    # take 1 pixel per time
    for i in range(num_pixels):
        pixels.fill((0, 0, 0))
        pixels[i] = (255, 255, 255)
        pixels.show()
        print('i: ', i)
        time.sleep(0.5)

    print('Stop sleep!')
    pixels.fill((0, 0, 0))
    pixels.deinit()
    sys.exit()