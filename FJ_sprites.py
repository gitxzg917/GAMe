import random
import pygame
# 屏幕大小常量
SCREEN_RECT = pygame.Rect(0, 0, 432, 768)
# 刷新帧率常量
FRAME_PER_SEC = 60
# 创建敌机定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 创建子弹定时器常量
HERO_FIRE_EVENT = pygame.USEREVENT + 1

class GameSprites(pygame.sprite.Sprite):
    # """飞机大战游戏精灵"""
    def __init__(self, image_name, speed=1):
        # 调用父类初始化方法
         super().__init__()
        # 定义对象属性
         self.image = pygame.image.load(image_name)
         self.rect = self.image.get_rect()
         self.speed = speed
    def update(self):
        # 在屏幕上垂直移动
         self.rect.y += self.speed

class Background(GameSprites):
    def __init__(self, is_alt=False):
        # 调用父类实现精灵创建
         super().__init__("./images/bj1.png")
        # 判断是否交替图像
         if is_alt:
             self.rect.y = -self.rect.height

    def update(self):
        # 调用父类方法实现
          super().update()
        # 判断是否移出屏幕
          if self.rect.y >= SCREEN_RECT.height:
             self.rect.y = -self.rect.height

class Enemy(GameSprites):
    def __init__(self):
        # 调用父类方法
        super().__init__("./images/dj.png")
        # 指定敌机初始随机速度
        self.speed = random.randint(1,3)
        # 指定敌机随机初始位置
        self.rect.bottom = 0
        max_x =SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        # 调用父类 保持垂直飞行
        super().update()
        # 判断是否飞出屏幕
        if self.rect.y >= SCREEN_RECT.height:
            # kill 方法将精灵从组中删除
            self.kill()

    def __del__(self):
           pass

class Hero(GameSprites):
    def __init__(self):
        # 调用父类方法设置图像，速度
        super().__init__("./images/FJ.png", 0)
        # 飞机中心=窗口中心 x轴
        self.rect.centerx = SCREEN_RECT.centerx
        # 飞机Y轴离边界距离
        self.rect.bottom = SCREEN_RECT.bottom - 120
        # 子弹精灵添加到组
        self.bullet = pygame.sprite.Group()

    def update(self):
        # 水平方向
        self.rect.x += self.speed
        # 控制英雄不能离开窗口
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        for i in (0, 1):
            # 创建子弹精灵
            bullets = Bullet()
            # 设置精灵位置
            bullets.rect.bottom = self.rect.y - i * 59
            bullets.rect.centerx = self.rect.centerx
            bullets1 = Bullet()
            # 设置精灵位置
            bullets1.rect.bottom = self.rect.y - i * 59 + 65
            bullets1.rect.centerx = self.rect.centerx - 40
            bullets2 = Bullet()
            # 设置精灵位置
            bullets2.rect.bottom = self.rect.y - i * 59 + 65
            bullets2.rect.centerx = self.rect.centerx + 40
            self.bullet.add(bullets, bullets1, bullets2)

class Bullet(GameSprites):
    def __init__(self):
        super().__init__("./images/zd.png", -2)

    def update(self):
        super().update()
        # 判断是否飞出屏幕
        if self.rect.bottom < 0:
            # kill 方法将精灵从组中删除
            self.kill()

    def __del__(self):
        pass

class Explode(GameSprites):
    def __init__(self):
        super().__init__("./images/yuan.png")
        self.read_to_change = 0

    def update(self):
        self.read_to_change += 1
        if self.read_to_change % 4 == 0:
            self.kill()


