import Laser

class Ship:

    coolDown = 10

    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ShipImage = None
        self.LaserImage = None
        self.Lasers = []
        self.CoolDownCounter = 0

    def Draw(self, window):
        window.blit(self.ShipImage, (self.x, self.y))
        for laser in self.Lasers:
            laser.Draw(window)

    def MoveLasers(self, movementValue, object1, height):
        self.CoolDown()
        for laser in self.Lasers:
            laser.Move(movementValue)
            if laser.OffScreen(height):
                self.Lasers.remove(laser)
            elif laser.Collision(object1):
                object1.health -= 10
                self.Lasers.remove(laser)

    def CoolDown(self):
        if self.CoolDownCounter >= self.coolDown:
            self.CoolDownCounter = 0
        elif self.CoolDownCounter > 0:
            self.CoolDownCounter += 1

    def Shoot(self, offSetX1, offSetX2, offSetY):
        if self.CoolDownCounter == 0:
            laser = Laser.Laser(self.x + offSetX1, self.y+offSetY, self.LaserImage)
            laser1 = Laser.Laser(self.x + offSetX2, self.y+offSetY, self.LaserImage)
            self.Lasers.append(laser)
            self.Lasers.append(laser1)
            self.CoolDownCounter = 1

    def GetWidth(self):
        return self.ShipImage.get_width()

    def GetHeight(self):
        return self.ShipImage.get_height()
