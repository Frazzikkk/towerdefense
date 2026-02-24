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


window = pygame.Window("towerdefense", window_size)
surface = window.get_surface()
clock = pygame.Clock()
player_image = pygame.Surface([50,50])
player = sprite(
    [window_size[0]/2, window_size[1]/2],
    player_image,
)

runing = True

while runing:
    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            runing = False
    
    surface.fill("blue")
    
    player.render(surface)

    window.flip()

    clock.tick(FPS)


