import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''表示單個外星人的類'''
    
    def __init__(self,ai_settings,screen):
        '''初始化外星人，並設置其起始位置'''
        super(Alien,self).__init__()
        self.screen = screen
        self.ai_settings =ai_settings
        
        #加載外星人圖像，並設置其rect屬性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        
        #每個外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
    def blitme(self):
        '''在指定的位置繪製外星人'''
        self.screen.blit(self.image,self.rect)
        
    def update(self):
        '''向左或向右移動外星人'''
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x
        
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True