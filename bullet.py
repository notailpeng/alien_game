import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''一個對飛船發射的子彈進行管理的類'''
    
    def __init__(self,ai_settings,screen,ship):
        '''在飛船所處的位置創建一個子彈對象'''
        super(Bullet,self).__init__()
        self.screen = screen
        
        #在(0,0)處創建一個表示子彈的矩形，再設置正確的位置
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        #存儲用小數表示的子彈位置
        #self.y = float(self.rect.y)
        
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
        
    def update(self):
        '''向上移動子彈'''
        self.rect.centery -=self.speed_factor
        
    def draw_bullet(self):
        '''在屏幕上繪製子彈'''
        pygame.draw.rect(self.screen,self.color,self.rect)
        