class Game_stats():
    '''跟蹤遊戲的統計信息'''
    
    def __init__(self,ai_settings):
        '''初始化統計信息'''
        self.ai_settings = ai_settings
        self.reset_stats()
        '''讓遊戲開始處於非活動狀態'''
        self.game_active = False
    def reset_stats(self):
        '''初始化在遊戲運行期間可能變化的統計信息'''
        self.ships_left = self.ai_settings.ship_limit
        