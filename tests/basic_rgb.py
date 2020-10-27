# Simple test for NeoPixels on Raspberry Pi
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


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            # pixels[i] = wheel(pixel_index & 255)
            print('index: {}\tpixels[{}] = {}'.format(pixel_index, i, pixels[i]))
        pixels.show()
        time.sleep(wait)

def r_g_b_():
    my_time = 2
    pixels.fill((255, 0, 0))
    print ('fill red')
    pixels.show()
    time.sleep(my_time)
    
    pixels.fill((0, 255, 0))
    print ('fill green')
    pixels.show()
    time.sleep(my_time)
    
    pixels.fill((0, 0, 255))
    print ('fill blue')
    pixels.show()
    time.sleep(my_time)
    
    pixels.fill((0, 0, 0))
    print('down')
    pixels.show()
    time.sleep(my_time / 2)
    
    
if __name__ == '__main__':
    r_g_b_()
    rainbow_cycle(0.5)