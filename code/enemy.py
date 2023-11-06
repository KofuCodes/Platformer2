import pygame
from tiles import AnimatedTile
from random import randint
import math

class Enemy(AnimatedTile):
    def __init__(self,pos,sizex,sizey,sett):
        super().__init__(pos,sizex, sizey,'./graphics/enemy', sett)
        self.deathSound = pygame.mixer.Sound("./audio/sfx/enemyKill.wav")
        self.scoreUp = pygame.mixer.Sound("./audio/sfx/pickupCoin.wav")
        self.rect.y += (sizex * sett.tile_size_mult) - self.image.get_size()[1]
        self.floor = self.rect.y
        self.speed = 0.1
        self.sett = sett

    def move(self):
        if self.frame_index > 1:
            self.rect.x += 2 * math.copysign(1, self.speed)
        else:
            self.rect.x += self.speed

    def reverse_image(self):
        if self.speed < 0:
            self.image = pygame.transform.flip(self.image,True,False)
        
    def reverse(self):
        self.speed *= -1

    def collision(self,player):
        if self.rect.colliderect(player.rect):
            if player.rect.midbottom[1] > self.rect.center[1]:
                self.sett.player_dead = True
                self.kill()
            else:
                self.sett.score += 5
                self.deathSound.play()
                self.scoreUp.play()
                self.kill()

    def update(self,x_shift,y_shift,player):
        self.floor += y_shift
        self.rect.x += x_shift
        self.rect.y += y_shift
        self.animate()
        self.move()
        self.reverse_image()
        self.collision(player)