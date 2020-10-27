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

# colors
red = (255, 0, 0)
orange = (255, 165, 0)
yellow = (250, 250, 55)
green = (0, 255, 0)
blue = (0, 0, 255)
indigo = (75, 0, 130)
violet = (143, 1, 255)
white = (255, 255, 255)

line_1 = []
line_2 = []
line_3 = []
line_4 = []
line_5 = []
line_6 = []
line_7 = []
line_8 = []

def init_lines():
    temp = 0.01
    tmp = 0
    tmp_final = tmp + 8
    print('____ line 1 ____')
    for i in range(tmp, tmp_final):
        line_1.append(i)
        pixels[i] = red
        print('i: {}\t tmp: {}'.format(i, tmp))
        time.sleep(temp)
    
    tmp = tmp_final
    tmp_final = tmp + 8
    print('____ line 2 ____')
    for i in range(tmp, tmp_final):
        line_2.append(i)
        pixels[i] = orange
        print('i: {}\t tmp: {}'.format(i, tmp))
        time.sleep(temp)
    
    tmp = tmp_final
    tmp_final = tmp + 8
    print('____ line 3 ____')
    for i in range(tmp, tmp_final):
        line_3.append(i)
        pixels[i] = yellow
        print('i: {}\t tmp: {}'.format(i, tmp))
        time.sleep(temp)
    
    tmp = tmp_final
    tmp_final = tmp + 8
    print('____ line 4 ____')
    for i in range(tmp, tmp_final):
        line_4.append(i)
        pixels[i] = green
        print('i: {}\t tmp: {}'.format(i, tmp))
        time.sleep(temp)
    
    tmp = tmp_final
    tmp_final = tmp + 8
    print('____ line 5 ____')
    for i in range(tmp, tmp_final):
        line_5.append(i)
        pixels[i] = blue
        print('i: {}\t tmp: {}'.format(i, tmp))
        time.sleep(temp)
    
    tmp = tmp_final
    tmp_final = tmp + 8
    print('____ line 6 ____')
    for i in range(tmp, tmp_final):
        line_6.append(i)
        pixels[i] = indigo
        print('i: {}\t tmp: {}'.format(i, tmp))
        time.sleep(temp)
    
    tmp = tmp_final
    tmp_final = tmp + 8
    print('____ line 7 ____')
    for i in range(tmp, tmp_final):
        line_7.append(i)
        pixels[i] = violet
        print('i: {}\t tmp: {}'.format(i, tmp))
        time.sleep(temp)
    
    tmp = tmp_final
    tmp_final = tmp + 8
    print('____ line 8 ____')
    for i in range(tmp, tmp_final):
        line_8.append(i)
        pixels[i] = white
        print('i: {}\t tmp: {}'.format(i, tmp))
        time.sleep(temp)
    
    print('line 1: ', line_1)
    print('line 2: ', line_2)
    print('line 3: ', line_3)
    print('line 4: ', line_4)
    print('line 5: ', line_5)
    print('line 6: ', line_6)
    print('line 7: ', line_7)
    print('line 8: ', line_8)
    
    pixels.show()

    
if __name__ == '__main__':
    init_lines()
    