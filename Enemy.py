import Ship
import pygame
import os

class Enemy(Ship.Ship):

    LaserBulletRed = pygame.image.load(os.path.join("Assets", "laser_bullet_red.png"))
    Level1Ship = pygame.image.load(os.path.join("Assets", "level_1_ship.png"))
    Level2Ship = pygame.image.load(os.path.join("Assets", "level_1_ship.png"))
    Level3Ship = pygame.image.load(os.path.join("Assets", "level_1_ship.png"))

    EnemyTypeMap = {
        "Easy": (Level1Ship, LaserBulletRed),
        "Shooter": (Level2Ship, LaserBulletRed),
        "Boss": (Level3Ship, LaserBulletRed)
    }


    def __init__(self, x, y, enemyType, health=100):
        super().__init__(x, y, health)
        self.ShipImage, self.LaserImage = self.EnemyTypeMap[enemyType]
        self.Mask = pygame.mask.from_surface(self.ShipImage)

    def Move(self, movementValue):
        self.y += movementValue
