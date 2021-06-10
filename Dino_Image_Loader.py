import pygame

#Dino
dinoJmp = pygame.image.load('images/dino/dino_jmp.png')
dinoWalkLeft = pygame.image.load('images/dino/dino_walkLeft.png')
dinoWalkRight = pygame.image.load('images/dino/dino_walkRight.png')
dinoWalkDead = pygame.image.load('images/dino/dino_dead.png')
dinoDuckFake = pygame.image.load('images/dino/dino_duck_fake.png')

dinoJmp = pygame.transform.smoothscale(dinoJmp, (44, 47))
dinoWalkLeft = pygame.transform.smoothscale(dinoWalkLeft, (44, 47))
dinoWalkRight = pygame.transform.smoothscale(dinoWalkRight, (44, 47))
dinoWalkDead = pygame.transform.smoothscale(dinoWalkDead, (44, 47))
dinoDuckFake = pygame.transform.smoothscale(dinoDuckFake, (150, 70))


#Cactus
cacti_group = pygame.image.load('images/cacti/cacti_group.png')
cacti_large_1 = pygame.image.load('images/cacti/cacti_large_1.png')
cacti_large_2 = pygame.image.load('images/cacti/cacti_large_2.png')
cacti_small_1 = pygame.image.load('images/cacti/cacti_small_1.png')
cacti_small_2 = pygame.image.load('images/cacti/cacti_small_2.png')
cacti_small_3 = pygame.image.load('images/cacti/cacti_small_3.png')

cacti_group = pygame.transform.smoothscale(cacti_group, (52, 50))
cacti_large_1 = pygame.transform.smoothscale(cacti_large_1, (25, 50))
cacti_large_2 = pygame.transform.smoothscale(cacti_large_2, (49, 50))
cacti_small_1 = pygame.transform.smoothscale(cacti_small_1, (17, 35))
cacti_small_2 = pygame.transform.smoothscale(cacti_small_2, (34, 35))
cacti_small_3 = pygame.transform.smoothscale(cacti_small_3, (51, 35))

#Misc
cloud = pygame.image.load('images/cloud.png')
ground = pygame.image.load('images/ground.png')

cloud = pygame.transform.smoothscale(cloud, (46, 13))
ground = pygame.transform.smoothscale(ground, (1200, 12))

