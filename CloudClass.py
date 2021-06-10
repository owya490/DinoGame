import Dino_Image_Loader as images
import random

class Cloud:
    def __init__(self, xVel):
        self.x_cloud = random.randrange(0, 501)
        self.y_cloud = random.randrange(10, 150)
        self.xVel_cloud = xVel
    
    def logic(self):
        self.x_cloud += self.xVel_cloud
        if self.x_cloud <= -47:
            self.xVel_cloud = random.randrange(1, 6)
            if self.xVel_cloud <= 4:
                self.xVel_cloud = 1
            else:
                self.xVel_cloud = 2
            
            self.xVel_cloud *= -1
            self.y_cloud = random.randrange(10, 150)
            self.x_cloud = random.randrange(501, 550)
    