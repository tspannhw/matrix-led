import os
import time
import zmq
import sys
from matrix_io.proto.malos.v1 import driver_pb2
from matrix_io.proto.malos.v1 import io_pb2

# MATRIX Everloop LED array port
PORT = 20021

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
        for led in range(35):
            leds.append(self.__getColor(**colors))
        self.__show(leds)
