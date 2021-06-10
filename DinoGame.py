import pygame
import Dino_Image_Loader as image
import GroundClass
import DinoClass
import CactusClass
import CloudClass

pygame.init()

gameDisplay = pygame.display.set_mode((500, 300))

pygame.display.set_caption("Dino Game")
font = pygame.font.Font('freesansbold.ttf', 22)
white = (255, 255, 255)
black = (0, 0, 0)


clock = pygame.time.Clock()

crashed = False

ground1 = GroundClass.Ground(0)
ground2 = GroundClass.Ground(1200)
dino = DinoClass.Dino()
cactus = CactusClass.Cactus()
cloud1 = CloudClass.Cloud(-1)
cloud2 = CloudClass.Cloud(-2)
cloud3 = CloudClass.Cloud(-1)
laser = False
laser_counter = 0
score = 0
def draw():
    global ground1
    global ground2
    global dino

    gameDisplay.blit(image.ground, (ground1.x_ground, ground1.y_ground))
    gameDisplay.blit(image.ground, (ground2.x_ground, ground2.y_ground))
    gameDisplay.blit(image.cloud, (cloud1.x_cloud, cloud1.y_cloud))
    gameDisplay.blit(image.cloud, (cloud2.x_cloud, cloud2.y_cloud))
    gameDisplay.blit(image.cloud, (cloud3.x_cloud, cloud3.y_cloud))

    gameDisplay.blit(cactus.state, (cactus.x_cactus, cactus.y_cactus))
    gameDisplay.blit(dino.state, (dino.x_dino, dino.y_dino))
    #gameDisplay.blit(image.dinoDuckFake, (50, 227))

def collide(x_dino, y_dino, x_cactus, y_cactus, x_width, y_height):
    global dino
    global cactus
    global ground1
    global ground2
    global cloud1
    global cloud2
    global cloud3
    x_dino_left = x_dino + 15
    x_dino_right = x_dino + 42
    y_dino_top = y_dino
    y_dino_bottom = y_dino + 43

    x_cactus_left = x_cactus
    x_cactus_right = x_cactus + x_width
    y_cactus_top = y_cactus
    y_cactus_bottom = y_cactus + y_height


    if (x_dino_right >= x_cactus_left) and (x_dino_right <= x_cactus_right):
        if (y_dino_bottom >= y_cactus_top):
            dino.isDead = True
            ground1.xVel_ground = 0
            ground2.xVel_ground = 0
            cactus.xVel_cactus = 0
            cloud1.xVel_cloud = 0
            cloud2.xVel_cloud = 0
            cloud3.xVel_cloud = 0
    elif (x_dino_left >= x_cactus_left) and (x_dino_left <= x_cactus_right):
        if (y_dino_bottom >= y_cactus_top):
            dino.isDead = True
            ground1.xVel_ground = 0
            ground2.xVel_ground = 0
            cactus.xVel_cactus = 0
            cloud1.xVel_cloud = 0
            cloud2.xVel_cloud = 0
            cloud3.xVel_cloud = 0
    elif (x_dino_left + 21 >= x_cactus_left) and (x_dino_left + 21 <= x_cactus_right):
        if (y_dino_bottom >= y_cactus_top):
            dino.isDead = True
            ground1.xVel_ground = 0
            ground2.xVel_ground = 0
            cactus.xVel_cactus = 0
            cloud1.xVel_cloud = 0
            cloud2.xVel_cloud = 0
            cloud3.xVel_cloud = 0
    

            


while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if dino.isDead:
                    ground1 = GroundClass.Ground(0)
                    ground2 = GroundClass.Ground(1200)
                    dino = DinoClass.Dino()
                    cactus = CactusClass.Cactus()
                    cloud1 = CloudClass.Cloud(-1)
                    cloud2 = CloudClass.Cloud(-2)
                    cloud3 = CloudClass.Cloud(-1)
                elif not dino.isJump:
                    dino.isJump = True
                    dino.isUp = True
                    dino.y_dino -= 10
            elif event.key == pygame.K_DOWN:
                if not dino.isJump:
                    dino.isDuck = True
            elif event.key == pygame.K_SPACE:
                if dino.isDead:
                    ground1 = GroundClass.Ground(0)
                    ground2 = GroundClass.Ground(1200)
                    dino = DinoClass.Dino()
                    cactus = CactusClass.Cactus()
                    cloud1 = CloudClass.Cloud(-1)
                    cloud2 = CloudClass.Cloud(-2)
                    cloud3 = CloudClass.Cloud(-1)
                    score = 0
                elif not dino.isJump:
                    dino.isJump = True
                    dino.isUp = True
                    dino.y_dino -= 10
            elif event.key == pygame.K_RIGHT:

                laser = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                if dino.isDuck:
                    dino.isDuck = False
                    dino.check = True
        if event.type == pygame.QUIT:
            crashed = True
    
    gameDisplay.fill(white)
    #pygame.draw.line(gameDisplay, black, (0, 300), (600, 300), 1)
    collide(dino.x_dino, dino.y_dino, cactus.x_cactus, cactus.y_cactus, cactus.x_width, cactus.y_height)
    ground1.logic()
    ground2.logic()
    cloud1.logic()
    cloud2.logic()
    cloud3.logic()
    cactus.logic()
    dino.logic()

    draw()
    #s = "" + score
    text = font.render(str(score), True, (0, 0, 0))
    if (not dino.isDead):
        score += 1
    gameDisplay.blit(text, (430, 30))
    # if laser:
    #     pygame.draw.line(gameDisplay, (255, 0, 0), (77, 219), (500, 219), 3)
    #     laser_counter += 1
    #     if laser_counter == 5:
    #         laser = False
    #         laser_counter = 0

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()


