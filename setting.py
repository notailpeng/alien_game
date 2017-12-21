class Settings():
    #存儲《外星人入侵》中所有的設置
    
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230,230,230)
        self.ship_speed_factor = 6
        self.bullet_speed_factor = 8
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color =60,60,60
        self.bullet_allowed = 30
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # self.fleet_direction為1表示向右，為-1表示向左移
        self.fleet_direction = 1
        self.ship_limit = 3