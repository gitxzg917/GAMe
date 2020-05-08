import time
import pygame
from FJ_sprites import *
class FjGame(object):

    def __init__(self):
        # print("游戏初始化")
        pygame.mixer.init()
        # 创建窗口
        self.wind = pygame.display.set_mode(SCREEN_RECT.size)
        # 创建时钟
        self.clock = pygame.time.Clock()
        # 调用私有方法
        self.__create_sprites()

        # 设置定时器事件
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        # 设置子弹定时器
        pygame.time.set_timer(HERO_FIRE_EVENT,500)
        # 添加背景音乐
        pygame.mixer.music.load("./images/bgm.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1, 0)

    def __create_sprites(self):
        # 创建背景精灵
        BJ1 = Background()
        BJ2 = Background(True)
        self.back_group = pygame.sprite.Group(BJ1, BJ2)
        # 创建敌机精灵族
        self.enemy_group = pygame.sprite.Group()
        # 创建英雄飞机
        self.hero = Hero()
        self.hero_group =pygame.sprite.Group(self.hero)
        # 创建爆炸精灵
        self.boom_group = pygame.sprite.Group()

    def start_game(self):
        print("游戏开始。。。")
        while True:
           # 设置刷新帧率
           self.clock.tick(FRAME_PER_SEC)
           # 事件监听
           self.__even_handler()
           # 碰撞检测
           self.__check_collide()
           # 更新绘制精灵
           self.__update_sprites()
           # 更新显示
           pygame.display.update()

    def __even_handler(self):
        for event in pygame.event.get():
            # 判断是否退出
            if event.type == pygame.QUIT:
                FjGame.__game_over()
            # 判断敌机事件
            elif event.type == CREATE_ENEMY_EVENT:
                # print("敌机出厂。。")
                # 创建敌机精灵
                enemy = Enemy()
                # 讲精灵添加到组
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #    print("向右")
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 2

        elif  keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -2

        else:
            self.hero.speed = 0

    def __check_collide(self):
        # 子弹摧毁敌机
        collision = pygame.sprite.groupcollide(self.hero.bullet, self.enemy_group, True, True)
        for enem in collision.keys():
            self.boom = Explode()
            self.boom.rect = enem.rect
            self.boom_group.add(self.boom)
            sound = pygame.mixer.Sound("./images/di.mp3")
            sound.play()
        uu = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        print(uu)
        if len(uu) > 0:
            self.hero.kill()
            FjGame.__game_over()

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.wind)
        self.enemy_group.update()
        self.enemy_group.draw(self.wind)
        self.hero_group.update()
        self.hero_group.draw(self.wind)
        self.hero.bullet.update()
        self.hero.bullet.draw(self.wind)
        self.boom_group.update()
        self.boom_group.draw(self.wind)
    def __game_over(self):
        print("游戏结束")
        pygame.quit()
        exit()
if __name__ == "__main__":
    # 创建游戏对象
    game = FjGame()
    # 启动游戏
    game.start_game()

