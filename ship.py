import pygame

class Ship:
    '管理飞船的类'

    def __init__(self, ai_game):
        '初始化飞船并设置初始位置'
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # 加载图像并获取外接矩形
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()

        # 每艘新的船都放在屏幕底部的中央
        self.rect.midbottom = self.screen_rect.midbottom

        # 在Ship.x中存储速度
        self.x = float(self.rect.x)

        # 移动的标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # 根据移动的标志调整飞船位置
        # 更新飞船的速度值
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # 根据self.x更新rect
        self.rect.x = self.x

    def blitme(self):
        '在指定位置绘制飞船'
        self.screen.blit(self.image, self.rect)