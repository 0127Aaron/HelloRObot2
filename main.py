from gopigo import *
import time

class Piggy(object):

    def __init__(self):
        print("I AM ALIVE")


    def pulse(self):
        """check for obstacles, drive fixed amount forward"""
        look = us_dist(15) #store the distance reading
        if look > 80:
            fwd.sleep(1)
            stop

    def cruise(self):
        """drive fwd, stop if sensor detects obstacle"""
        fwd()
        while(True):
            if us_dist(15) < 30:
                stop()
            time.sleep(.2)

    def servo_sweep(self):
        """loop in a 20 degree arc and move servo"""
        for ang in range(20, 160, 2):
            servo(ang)
            time.sleep(.2)


    def cha_cha(self):
        for x in range(5):
            right_rot()
            time.sleep(.5)
            left_rot()
            time.sleep(.5)
            stop()


p = Piggy()