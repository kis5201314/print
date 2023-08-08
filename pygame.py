import pygame

# 初始化游戏
pygame.init()

# 设置窗口大小
screen = pygame.display.set_mode((800, 600))

# 加载玛丽图片
mario_img = pygame.image.load("mario.png")
mario_x = 50
mario_y = 50

# 游戏主循环
running = True
while running:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 更新玛丽位置
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        mario_x -= 5
    if keys[pygame.K_RIGHT]:
        mario_x += 5
    if keys[pygame.K_UP]:
        mario_y -= 5
    if keys[pygame.K_DOWN]:
        mario_y += 5

    # 绘制背景
    screen.fill((0, 0, 0))

    # 绘制玛丽
    screen.blit(mario_img, (mario_x, mario_y))

    # 更新屏幕显示
    pygame.display.flip()

# 退出游戏
pygame.quit()
