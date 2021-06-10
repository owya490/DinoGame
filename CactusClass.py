import Dino_Image_Loader as images
import random

#y == 242

class Cactus:

    def __init__(self):
        self.y_cactus = 213
        self.x_cactus = 601
        self.xVel_cactus = -4
        self.state = images.cacti_large_1

        self.x_width = 25
        self.y_height = 50

    def logic(self):
        self.x_cactus += self.xVel_cactus
        if self.x_cactus <= -55:
            tmp = random.randrange(1, 7)
            if tmp == 1:
                self.state = images.cacti_group #52
                self.y_cactus = 212
                self.x_cactus = 601
                self.x_width = 52
                self.y_height = 50
            elif tmp == 2:
                self.state = images.cacti_large_1 #25
                self.y_cactus = 212
                self.x_cactus = 601
                self.x_width = 25
                self.y_height = 50
            elif tmp == 3:
                self.state = images.cacti_large_2 #49
                self.y_cactus = 212
                self.x_cactus = 601
                self.x_width = 49
                self.y_height = 50
            elif tmp == 4:
                self.state = images.cacti_small_1 #17
                self.y_cactus = 225
                self.x_cactus = 601
                self.x_width = 17
                self.y_height = 35
            elif tmp == 5:
                self.state = images.cacti_small_2 #34
                self.y_cactus = 225
                self.x_cactus = 601
                self.x_width = 34
                self.y_height = 35
            elif tmp == 6:
                self.state = images.cacti_small_3 #51
                self.y_cactus = 225
                self.x_cactus = 601
                self.x_width = 51
                self.y_height = 35
        pass
