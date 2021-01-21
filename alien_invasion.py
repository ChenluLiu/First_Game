import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    '管理游戏资源和行为的类'
    
    def __init__(self):
        '初始化并创建资源'
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) # 全屏运行游戏
        #self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))  # 以指定窗口尺寸运行游戏
        self.settings.screen_width = self.screen.get_rect().width       # 根据屏幕的宽度决定窗口的宽度
        self.settings.screen_height = self.screen.get_rect().height     # 根据屏幕的高度决定窗口的高度
        pygame.display.set_caption('Alien Invasion')

        self.ship = Ship(self)

        # 设置背景色，已在settings中设置
        # self.bg_color = (230, 230, 230)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
                #if event.key == pygame.K_RIGHT:
                #    self.ship.moving_right = True
                #elif event.key == pygame.K_LEFT:
                #    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                #if event.key == pygame.K_RIGHT:
                #    self.ship.moving_right = False
                #if event.key == pygame.K_LEFT:
                #    self.ship.moving_left = False

    def _check_keydown_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()

    def run_game(self):
        '开始游戏的主循环'
        while True:
            self._check_events()
            #'监视键盘和鼠标事件',用上一条辅助方法实现
            #for event in pygame.event.get():
            #    if event.type == pygame.QUIT:
            #        sys.exit()

            # 更新飞船的位置
            self.ship.update()

            self._update_screen()
            # 每次循环都重绘屏幕，并切换到新屏幕，用上一条方法实现
            #self.screen.fill(self.settings.bg_color)
            #self.ship.blitme()
            #'让最近绘制的屏幕可见'
            #pygame.display.flip()



if __name__ == '__main__':
    #'创建游戏实例并运行'
    ai = AlienInvasion()
    ai.run_game()

            