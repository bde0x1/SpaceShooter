import pygame


class Laser:
    def __init__(self, x, y, laserImage):
        self.x = x
        self.y = y
        self.LaserImage = laserImage
        self.Mask = pygame.mask.from_surface(self.LaserImage)

    def Draw(self, window):
        window.blit(self.LaserImage, (self.x, self.y))

    def Move(self, movementValue):
        self.y += movementValue

    def OffScreen(self, height):
        return not(self.y <= height and self.y >= 0)

    def Collision(self, object1):
        return Collide(self, object1)

def Collide(object1, object2):
        offSetX = object2.x - object1.x
        offSetY = object2.y - object1.y
        return object1.Mask.overlap(object2.Mask, (int(offSetX), int(offSetY))) != None

