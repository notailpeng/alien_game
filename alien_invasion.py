import  pygame
from pygame.sprite import Group
from setting import Settings
from ship import Ship
from game_stats import Game_stats
#from alien import Alien
import game_functions as gf
from button import Button,Author_Name


def run_game():
    #初始化遊戲並創建一個屏幕對象
        pygame.init()
        ai_settings = Settings()
        screen = pygame.display.set_mode ((ai_settings.screen_width,ai_settings.screen_height))
        pygame.display.set_caption('Alien Invasion')
        play_button = Button(ai_settings,screen,'Play')
        name = Author_Name(ai_settings,screen,'Notail_Peng')
        #創建一搜飛船
        stats = Game_stats(ai_settings)
        ship = Ship(ai_settings,screen)
        bullets = Group()
        aliens = Group()
        
        #創建外星人群
        gf.create_fleet(ai_settings,screen,ship,aliens)
        #創建一個外星人
        #alien = Alien(ai_settings,screen)
        #開始遊戲的主循環
        while True:
            
            #監視鍵盤和鼠標事件
            gf.check_events(ai_settings,screen,stats,play_button,ship,aliens,bullets)
            
            if stats.game_active:
                ship.update()
                gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
                gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
            #每次循環時都重繪屏幕讓最近繪製的屏幕可見
            gf.update_screen(ai_settings,screen,stats,ship,aliens,bullets,play_button,name)

run_game()
