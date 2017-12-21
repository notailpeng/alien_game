import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep



def check_events_keydown(event,ai_settings,screen,ship,bullets):
    '''響應按鍵'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key ==pygame.K_UP:
        ship.moving_up = True
    elif event.key ==pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        #創建一個子彈，並將它加入到編組bullets中
        fire_bullet(event,ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_q:
        sys.exit()
        
def check_events_keyup(event,ship):
    '''響應松開'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key ==pygame.K_UP:
        ship.moving_up = False
    elif event.key ==pygame.K_DOWN:
        ship.moving_down = False


def check_events(ai_settings,screen,stats,play_button,ship,aliens,bullets):
    '''響應按鍵和鼠標事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_events_keydown(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_events_keyup(event,ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,stats,play_button,ship,aliens,bullets,mouse_x,mouse_y)
            
def check_play_button(ai_settings,screen,stats,play_button,ship,aliens,bullets,mouse_x,mouse_y):
    '''玩家單機play按鈕時開始遊戲'''
    if play_button.rect.collidepoint(mouse_x,mouse_y) and not stats.game_active:
        # 隱藏光標
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True
        aliens.empty()
        bullets.empty()
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()  

def update_screen(ai_settings,screen,stats,ship,aliens,bullets,play_button,name):
    '''更新屏幕上的圖像，並切換到新屏幕'''
    #每次循環時都重繪屏幕
    screen.fill(ai_settings.bg_color)
    name.draw_name()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    if not stats.game_active:
        play_button.draw_button()
    #讓最新繪製的屏幕可見
    pygame.display.flip()
    
def update_bullets(ai_settings,screen,ship,aliens,bullets):
    '''更新子彈的位置，並消除已經消失的子彈'''
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    '''檢查是否有子彈擊中外星人'''
    #如果擊中了則刪除外星人和子彈
    check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets)
    
def check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets):
    '''響應外星人和子彈的碰撞'''
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
    if len(aliens) == 0:
        '''刪除現有子彈並新建一批外星人'''
        #bullets.empty()
        create_fleet(ai_settings,screen,ship,aliens)
    
def fire_bullet(event,ai_settings,screen,ship,bullets):
    '''如果還沒有達到限制就發射一個子彈'''
    #創建新子彈，並將其加入到編組bullets中
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings,screen,ship)    
        bullets.add(new_bullet)
            
def get_number_alien_x (ai_settings,alien_width):
    '''計算每行可容納多少外星人'''
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int ( available_space_x / (2 * alien_width) )
    return number_aliens_x

def get_number_rows(ai_settings,ship_height,alien_height):
    '''計算可容納多少行外星人'''
    available_space_y = ai_settings.screen_height - 4 * alien_height - ship_height
    number_aliens_row = int ( available_space_y/ ( 2 * alien_height ) )
    return number_aliens_row
    
def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width *alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 *alien.rect.height * row_number
    aliens.add(alien)
    
def create_fleet(ai_settings,screen,ship,aliens):
    '''創建外星人群'''
    #創建一個外星人，並計算一行能容納多少外星人
    #外星人間距為外星人寬度
    alien = Alien(ai_settings,screen)
    number_aliens_x = get_number_alien_x(ai_settings,alien.rect.width)
    number_aliens_row = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)
    #創建第一行外星人
    for row_number in range (number_aliens_row):
        for alien_number in range(number_aliens_x):
            #創建一個外星人並將其加入當前行
            create_alien(ai_settings,screen,aliens,alien_number,row_number)
  
def update_aliens(ai_settings,stats,screen,ship,aliens,bullets):
    '''更新外星人群中所有外星人的位置'''
    check_fleet_edges(ai_settings,aliens)
    aliens.update()
    '''檢測外星人和飛船的碰撞'''
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
        
def check_fleet_edges(ai_settings,aliens):
    '''外星人到達邊緣時採取響應的措施'''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break
            
def change_fleet_direction(ai_settings,aliens):
    '''將整群外星人向下移，并改變移動的方向'''
    for alien in aliens.sprites():
        alien.rect.y +=ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def ship_hit(ai_settings,stats,screen,ship,aliens,bullets):
    stats.ships_left -= 1
    if stats.ships_left > 0:
        aliens.empty()
        bullets.empty()
    
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()
    
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)