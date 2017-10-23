import os
import threading
import time
from matrixled import MatrixLed
from ledrunner import LedRunner

matrix = MatrixLed()
runner = LedRunner()
matrix.connect()

def get_color():
    selection = raw_input('Insert color (RGBW value separated by space, e.g. 12 0 125 30): ')
    colors = [int(c) for c in selection.split()]
    red = colors[0] if len(colors) > 0 else 0
    green = colors[1] if len(colors) > 1 else 0
    blue = colors[2] if len(colors) > 2 else 0
    white = colors[3] if len(colors) > 3 else 0
    return { 'red': red, 'green': green, 'blue': blue, 'white': white }

def display_title():
    print '*****************************************'
    print '**** MATRIX ONE Everloop LED blinker ****'
    print '*****************************************\n'

def repeat(func, color):
    while (running_task is not None):
        func(**color)

choice = ''
while choice != 'q':
    os.system('clear')
    display_title()
    print '[1] Set LED array mode SOLID\n'
    print '[2] Set LED array mode LOADING\n'
    print '[3] Shutdown LED array\n'
    print '[q] Quit program\n'

    choice = raw_input('> ')
    running_task = None

    if choice == '1':
        color = get_color()
        runner.once(matrix.solid, **color)
    elif choice == '2':
        color = get_color()
        runner.start(matrix.loading_bar, **color)
    elif choice == '3':
        runner.once(matrix.solid, **{'red': 0, 'green': 0, 'blue': 0, 'white': 0})
    elif choice == 'q':
        matrix.disconnect()
        os.system('clear')
        print 'Bye...\n'
