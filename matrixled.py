import os
import time
import zmq
import sys
import threading
from matrix_io.proto.malos.v1 import driver_pb2
from matrix_io.proto.malos.v1 import io_pb2

# MATRIX Everloop LED array port
PORT = 20021
LED_COUNT = 35

class MatrixLed:
    def __init__(self, matrix_ip='127.0.0.1'):
        context = zmq.Context()
        self.address = 'tcp://{0}:{1}'.format(matrix_ip, PORT)
        self.socket = context.socket(zmq.PUSH)

    def __show(self, leds):
        config = driver_pb2.DriverConfig()
        config.image.led.extend(leds)
        self.socket.send(config.SerializeToString())
    
    def __getColor(self, **args):
        ledValue = io_pb2.LedValue()
        ledValue.red = args.get('red', 0)
        ledValue.green = args.get('green', 0)
        ledValue.blue = args.get('blue', 0)
        ledValue.white = args.get('white', 0)
        return ledValue

    def connect(self):
        self.socket.connect(self.address)

    def disconnect(self):
        self.socket.disconnect(self.address)

    def solid(self, **colors):
        leds = []
        for led in range(LED_COUNT):
            leds.append(self.__getColor(**colors))
        self.__show(leds)

    def loading_bar(self, **colors):
        if all(val == 0 for key,val in colors.iteritems()):
            self.disconnect()
            sys.exit('Cannot run loading bar if all LED values are 0')
        color = self.__getColor(**colors)
        dark = self.__getColor(red=0, green=0, blue=0, white=0)
        count = 0
        while count < LED_COUNT:
            count += 1
            lit_leds = [color for led in range(count)]
            dark_leds = [dark for led in range(LED_COUNT - count)]
            leds = lit_leds + dark_leds
            self.__show(leds)
            time.sleep(0.01)
