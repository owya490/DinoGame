import Dino_Image_Loader as images

class Dino:

    def __init__(self):
        self.x_dino = 50
        self.y_dino = 214
        self.yVel_dino = 0
        self.isJump = False
        self.isDuck = False
        self.check = False
        self.isLeft = True
        self.isDead = False
        self.isUp = False
        self.state = images.dinoWalkLeft
        self.frameCount = 0

    def logic(self):
        self.frameCount += 1

        if self.isDead:
            self.state = images.dinoWalkDead
            return

        if self.y_dino + self.yVel_dino >= 214:
            self.y_dino = 214
            self.yVel_dino = 0
            self.isJump = False
            if self.check:
                self.check = True
        else:
            self.y_dino += self.yVel_dino
        
        if self.check:
            self.state = images.dinoWalkLeft
            self.y_dino = 214
            self.x_dino = 50
            self.check = False

        if self.isDuck:
            self.state = images.dinoDuckFake
            self.y_dino = 227
            self.x_dino = -10


        elif self.isJump:
            self.state = images.dinoJmp
            if self.y_dino <= 100:
                self.isUp = False
            if self.isUp:
                if self.y_dino <= 140:
                    self.yVel_dino = -4
                elif self.y_dino <= 120:
                    self.yVel_dino = -2
                elif self.y_dino <= 103:
                    self.yVel_dino = -1
                else:
                    self.yVel_dino = -8
            
            else:
                if self.y_dino <= 100:
                    self.yVel_dino = 2
                    self.isUp = False
                elif self.y_dino <=110:
                    self.yVel_dino = 4
                
                elif self.y_dino >= 130:
                    self.yVel_dino = 8
                    #self.isUp = False              
                # elif self.y_dino == 214:
                #     self.yVel_dino = 0
                #     self.isJump = False
                #     self.check = True
        else:
            if self.isLeft and self.frameCount >= 12:
                self.state = images.dinoWalkRight
                self.isLeft = False
                self.frameCount = 0
            elif self.frameCount >= 12:
                self.state = images.dinoWalkLeft
                self.isLeft = True
                self.frameCount = 0
            

    
