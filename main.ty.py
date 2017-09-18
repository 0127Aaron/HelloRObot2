from gopigo import *
import time

class Piggy(object):

    def __init__(self):
        print("I AM ALIVE")

    def cha_cha(self):
        for x in range(5):
            right_rot()
            time.sleep(.5)
            left_rot()
            time.sleep(.5)
            stop()


P = Piggy()
p.cha_cha()