from blinkt import set_brightness, set_pixel, show
import argparse, sys
from time import sleep

blink_sleep = 0.1
red = (255, 0, 0)
yellow = (255, 180, 0)
green = (20, 180, 0)
blue = (30, 0, 255)
num_blinks = 10

parser = argparse.ArgumentParser(description='Reading the timer data from command line.')

parser.add_argument('time', type=int)
parser.add_argument('-b', '--brightness', type=float, default=0.3)
parser.add_argument('-u', '--unit', choices=['sec', 'min'], default='min')

def main(time, brightness, unit):
    if unit == 'min':
        sectime = time * 60
    else:
        sectime = time

    sleeptime = sectime / 16

    set_brightness(brightness)
    
    for x in range(8):
        set_pixel(x, *red)

    show()

    for x in range(8):
        sleep(sleeptime)
        set_pixel(x, *yellow)
        show()

    for x in range(8):
        sleep(sleeptime)
        set_pixel(x, *green)
        show()
    
    sleep(1)

    for x in range(num_blinks):
        for x in range(8):
            set_pixel(x, 0, 0, 0)
        show()
        sleep(blink_sleep)
        for x in range(8):
            set_pixel(x, *blue)
        show()
        sleep(blink_sleep)

if __name__ == '__main__':
    main(**vars(parser.parse_args(sys.argv[1:])))
