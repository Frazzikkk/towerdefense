from random import randint
import pygame


FPS = 60
window_size = (800, 600)




class sprite:
    def __init__(self,center,image):
        self.image = image
        self.rect = image.get_frect()
        self.rect.center = center

    def render(self,surface):
        surface.blit(self.image, self.rect)
class movesprite(sprite):
    def __init__(self,center,image, speed, direction):
        super().__init__(center,image)

        self.speed = speed
        self.direction = direction

    def update(self):
        vector = self.direction * self.speed
        self.rect.move_ip(vector)

pygame.init()

window = pygame.Window("towerdefense", window_size)
surface = window.get_surface()
clock = pygame.Clock()
font = pygame.Font(None, 32)

player_image = pygame.Surface([50,50])
player = sprite([window_size[0]/2, window_size[1]/2],player_image,)

bullets = []
enemies = []


runing = True
score = 0

while runing:
    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            runing = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            center = pygame.Vector2(player.rect.center)
            pos  = pygame.Vector2(pygame.mouse.get_pos())
            vector = (pos - center).normalize()
            img = pygame.Surface([10,10])
            img.fill("red")
            bullet = movesprite(center, img, 7, vector)
            bullets.append(bullet)

    if randint(0,100) <= 5:
        r = randint(1,4)
        if r == 1:
            pos = pygame.Vector2(
                randint(0, window_size[0]), -100,
            )
        if r == 2:
            pos = pygame.Vector2(
                window_size[0] + 100,
                randint(0, window_size[1])

            )
        if r == 3:
            pos = pygame.Vector2(
                randint(0, window_size[0]),
                window_size[1] + 100,
            )
        if r == 4:
            pos = pygame.Vector2(
                -100, 
                randint(0, window_size[1])
            )
        center = pygame.Vector2(player.rect.center)
        
        vector = (center - pos).normalize()
        img = pygame.Surface([50,50])
        img.fill("yellow")
        speed = randint(200 ,600) / 100
        enemy = movesprite(pos, img, speed, vector)
        enemies.append(enemy)

    for bullet in bullets:
        bullet.update()
    for enemy in enemies:
        enemy.update()

    for enemy in enemies:
        for bullet in bullets:
            if bullet.rect.colliderect(enemy.rect):
                score += 1
                enemies.remove(enemy)
                bullets.remove(bullet)
                break
    for enemy in enemies:
        if player.rect.colliderect(enemy.rect):
            score = 0
            enemies.clear()
            bullets.clear()
            break

    surface.fill("blue")
    
    player.render(surface) 
    for bullet in bullets:
        bullet.render(surface)
    for enemy in enemies:
        enemy.render(surface)
    player.render(surface) 

    text = "БАллы: " + str(score)
    image = font.render(text, True, "black")
    surface.blit(image, [10, 10])

    window.flip()
    clock.tick(FPS)

