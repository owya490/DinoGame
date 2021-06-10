import Dino_Image_Loader as images
#import DinoGame

class Ground:
    def __init__(self, x):
        self.x_ground = x
        self.y_ground = 250
        self.xVel_ground = -4

    def refresh(self):
        if self.x_ground <= -1200:
            self.x_ground = 1200


    def logic(self):
        self.x_ground = self.x_ground + self.xVel_ground
        self.refresh()

    