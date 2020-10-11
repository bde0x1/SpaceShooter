import Ship
import pygame
import os

PlayerShip = pygame.image.load(os.path.join("Assets", "player_ship.png"))
LaserBulletBlue = pygame.image.load(os.path.join("Assets", "laser_bullet_blue.png"))

class Player(Ship.Ship):

    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ShipImage = PlayerShip
        self.LaserImage = LaserBulletBlue
        self.Mask = pygame.mask.from_surface(self.ShipImage)
        self.MaxHealth = health

    def MoveLasers(self, movementValue, objects, height):
        self.CoolDown()
        for laser in self.Lasers:
            laser.Move(movementValue)
            if laser.OffScreen(height):
                self.Lasers.remove(laser)
            else:
                for obj in objects:
                    if laser.Collision(obj):
                        objects.remove(obj)
                        self.Lasers.remove(laser)

    def Draw(self, window):
        super().Draw(window)
        self.HealthBar(window)

    def HealthBar(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y + self.ShipImage.get_height() + 10, self.ShipImage.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (self.x, self.y + self.ShipImage.get_height() + 10, self.ShipImage.get_width() * (self.health/self.MaxHealth), 10))
        healthFont = pygame.font.SysFont("comicsans", 15)
        healthLabel = healthFont.render(f"health: {self.health}", 1, (0, 0, 0))
        window.blit(healthLabel, (self.x, self.y + self.ShipImage.get_height() + 10, self.ShipImage.get_width()/2 - healthLabel.get_width()/2, 10))