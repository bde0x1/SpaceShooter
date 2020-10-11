import pygame
import os
import Player
import Enemy
import time
import random

pygame.font.init()

Width, Height = 1024, 800

Win = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Star Wars (Space Shooter Game).demo")

# Background
BG = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "bg.gif")), (Width, Height))

def Main():

    lost = False
    lostCount = 0
    run = True
    FPS = 60
    clock = pygame.time.Clock()
    level = 0
    lives = 5
    mainFont = pygame.font.SysFont("comicsans", 50)
    lostFont = pygame.font.SysFont("comicsans", 80)
    playerMovementValue = 10
    laserMovementValue = 10
    enemies = []
    waveLength = 5
    enemyMovementValue = 1

    player = Player.Player(((Width/2) - (125/2)), 600)

    def RedrawWindow():
        Win.blit(BG, (0, 0))

        # draw text
        livesLabel = mainFont.render(f"Lives: {lives}", 1, (255, 255, 255))
        levelLabel = mainFont.render(f"Level: {level}", 1, (255, 255, 255))

        Win.blit(livesLabel, (10, 10))
        Win.blit(levelLabel, (Width - levelLabel.get_width() - 10, 10))

        for enemy in enemies:
            enemy.Draw(Win)

        player.Draw(Win)

        if lost:
            lostLabel = lostFont.render("You Lost!", 1, (255, 255, 255))
            Win.blit(lostLabel, (Width/2 - lostLabel.get_width()/2, 350))

        pygame.display.update()



    while run:
        clock.tick(FPS)
        RedrawWindow()

        if lives <= 0 or player.health <= 0:
            lost = True
            lostCount += 1

        if lost:
            if lostCount > FPS * 3:
                run = False
            else:
                continue

        if len(enemies) == 0:
            level += 1
            waveLength += 10

            for i in range(waveLength):
                enemy = Enemy.Enemy(random.randrange(50, Width - 100), random.randrange(-1500, -100), random.choice(["Easy", "Shooter", "Boss" ]))
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - playerMovementValue + 25 > 0:     # left
            player.x -= playerMovementValue
        if keys[pygame.K_d] and player.x + playerMovementValue + player.GetWidth()-25 < Width:    # right
            player.x += playerMovementValue
        if keys[pygame.K_w] and player.y - playerMovementValue + 25 > 0:     # up
            player.y -= playerMovementValue
        if keys[pygame.K_s] and player.y + playerMovementValue + player.GetHeight()-25 < Height:   # down
            player.y += playerMovementValue
        if keys[pygame.K_SPACE]:
            player.Shoot(25, 132, 0)


        for enemy in enemies:
            enemy.Move(enemyMovementValue)
            enemy.MoveLasers(laserMovementValue, player, Height)

            if random.randrange(0, 2*60) == 1:
                enemy.Shoot(45, 65, 50)

            playerWasShooted = False
            for laser in enemy.Lasers:
                if laser.Collision(player):
                    playerWasShooted = True

            if playerWasShooted:
                player.health -= 30
                enemies.remove(enemy)
            elif enemy.y + enemy.GetHeight() > Height:
                lives -= 1
                enemies.remove(enemy)


        player.MoveLasers(-laserMovementValue, enemies, Height)

def MainMenu():
    titleFont = pygame.font.SysFont("comicsans", 70)
    run = True
    while run:
        Win.blit(BG, (0, 0))
        titleLabel = titleFont.render("Press the mouse to begin..", 1, (255, 255, 255))
        Win.blit(titleLabel, (Width/2-titleLabel.get_width()/2, 350))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                Main()
    pygame.quit()

MainMenu()
