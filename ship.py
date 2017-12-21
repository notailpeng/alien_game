import pygame


class Ship():
    def __init__(self,ai_settings,screen):
        '''初始化飛船，並設定其位置'''
        self.screen = screen
        self.ai_settings = ai_settings
        #移動標誌
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        #加載飛船圖像並獲取其外接矩形
        self.image = pygame.image.load ('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #將每艘飛船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        

    def blitme(self):
        '''在指定的位置繪製飛船'''
        self.screen.blit(self.image,self.rect)
    
    def update(self):
        '''根據移動標誌調整飛船的位置'''
        #更新飛船的center值，而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom <self.screen_rect.bottom:
            self.rect.centery += self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.rect.centery -= self.ai_settings.ship_speed_factor

    def center_ship(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom