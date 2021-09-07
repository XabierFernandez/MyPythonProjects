from pyfirmata import Arduino, util
import time

board = Arduino('COM4')
while True:
    time.sleep(0.025)
    board.digital[11].write(1)
    time.sleep(0.025)
    board.digital[11].write(0)
