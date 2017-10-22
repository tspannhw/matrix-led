import os
from matrixled import MatrixLed

matrix = MatrixLed()
matrix.connect()

#def get_color():
#    selection = input('Insert color (RGBW value separated by space, e.g. 12 0 125 30)')
#    colors = [int(c) for c in selection]
#    dict = 
#    return colors

def display_title():
    print '*****************************************'
    print '**** MATRIX ONE Everloop LED blinker ****'
    print '*****************************************\n'

choice = ''
while choice != 'q':
    os.system('clear')
    display_title()
    print '[1] Set LED array mode SOLID\n'
    print '[2] Shutdown LED array\n'
    print '[q] Quit program\n'

    choice = raw_input('> ')

    if choice == '1':
        matrix.solid(red=30, green=0, blue=0, white=0)
    elif choice == '2':
        matrix.solid(red=0, green=0, blue=0, white=0)
    elif choice == 'q':
        matrix.disconnect()
        os.system('clear')
        print 'Bye...\n'
