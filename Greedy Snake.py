#导入
import pygame, keyboard, random, threading, time, pickledb

#显示规则
print()
print('方向键控制方向')
print('\'esc\'退出')
print('\'alt\'暂停')
print('\'space\'继续')
print('每吃掉一个莓果，蛇身长长一格')
print('撞到蛇身或窗口边缘即为死亡')
print('死亡后\'esc\'退出，\'enter\'再来一局')

#初始化
pygame.init()

#设定窗口
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Greedy Snake')

#设定蛇身
body = pygame.Surface((20, 20))
body.fill('yellow')

#设定莓果
berries = pygame.Surface((20, 20))
berries.fill('red')

#设定数字方块(用于显示数字)
block = pygame.Surface((4, 4))

#设定变量
T = 0
db = pickledb.load('Mark.db', False)
HI = db.get('HiMark')
B = False

#数字方块坐标(用于显示数字)
zero = ((3, 0), (4, 0), (5, 0),
        (2, 1), (5, 1), (6, 1),
        (1, 2), (2, 2), (6, 2), (7, 2),
        (1, 3), (2, 3), (6, 3), (7, 3),
        (1, 4), (2, 4), (6, 4), (7, 4),
        (2, 5), (3, 5), (6, 5),
        (3, 6), (4, 6), (5, 6))

one = ((4, 0), (5, 0),
       (3, 1), (4, 1), (5, 1),
       (4, 2), (5, 2),
       (4, 3), (5, 3),
       (4, 4), (5, 4),
       (4, 5), (5, 5),
       (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6))

two = ((2, 0), (3, 0), (4, 0), (5, 0), (6, 0),
       (1, 1), (2, 1), (6, 1), (7, 1),
       (5, 2), (6, 2), (7, 2),
       (3, 3), (4, 3), (5, 3), (6, 3),
       (2, 4), (3, 4), (4, 4), (5, 4),
       (1, 5), (2, 5), (3, 5),
       (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6))

three = ((2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
         (5, 1), (6, 1),
         (4, 2), (5, 2),
         (3, 3), (4, 3), (5, 3), (6, 3),
         (6, 4), (7, 4),
         (1, 5), (2, 5), (6, 5), (7, 5),
         (2, 6), (3, 6), (4, 6), (5, 6), (6, 6))

four = ((4, 0), (5, 0), (6, 0),
        (3, 1), (4, 1), (5, 1), (6, 1),
        (2, 2), (3, 2), (5, 2), (6, 2),
        (1, 3), (2, 3), (5, 3), (6, 3),
        (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4),
        (5, 5), (6, 5),
        (5, 6), (6, 6))

five = ((1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0),
        (1, 1), (2, 1),
        (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2),
        (6, 3), (7, 3),
        (6, 4), (7, 4),
        (1, 5), (2, 5), (6, 5), (7, 5),
        (2, 6), (3, 6), (4, 6), (5, 6), (6, 6))

six = ((3, 0), (4, 0), (5, 0), (6, 0),
       (2, 1), (3, 1),
       (1, 2), (2, 2),
       (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3),
       (1, 4), (2, 4), (6, 4), (7, 4),
       (1, 5), (2, 5), (6, 5), (7, 5),
       (2, 6), (3, 6), (4, 6), (5, 6), (6, 6))

seven = ((1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
         (1, 1), (2, 1), (6, 1), (7, 1),
         (5, 2), (6, 2),
         (4, 3), (5, 3),
         (3, 4), (4, 4),
         (3, 5), (4, 5),
         (3, 6), (4, 6))

eight = ((2, 0), (3, 0), (4, 0), (5, 0),
         (1, 1), (2, 1), (6, 1),
         (1, 2), (2, 2), (3, 2), (6, 2),
         (2, 3), (3, 3), (4, 3), (5, 3),
         (1, 4), (4, 4), (5, 4), (6, 4), (7, 4),
         (1, 5), (6, 5), (7, 5),
         (2, 6), (3, 6), (4, 6), (5, 6), (6, 6))

nine = ((2, 0), (3, 0), (4, 0), (5, 0), (6, 0),
        (1, 1), (2, 1), (6, 1), (7, 1),
        (1, 2), (2, 2), (6, 2), (7, 2),
        (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3),
        (6, 4), (7, 4),
        (5, 5), (6, 5),
        (2, 6), (3, 6), (4, 6), (5, 6))

number = (zero, one, two, three, four, five, six, seven, eight, nine)

def keyname(key) :
    #键盘捕获
    global KEY
    KEY = key.name
keyboard.on_press(keyname)

def snake() :
    #显示蛇身
    global path
    for xy in path :
        screen.blit(body, xy)

def food() :
    #显示食物
    global fx, fy
    screen.blit(berries, (fx, fy))

def eat() :
    #检测是否吃掉食物
    if (x, y) == (fx, fy) :
        return True
    else :
        return False

def crash() :
    #检测是否碰撞
    if path.count((x, y)) != 0 :
        return True
    elif x < 0 or x > 480 or y < 0 or y > 480 :
        return True
    else :
        return False

def count() :
    #计时线程函数
    global T
    while True :
        if B :
            time.sleep(1)
            T += 1

def timer() :
    #显示时间
    global T, number
    a = T // 100
    b = T % 100 // 10
    c = T % 10
    a = number[a]
    b = number[b]
    c = number[c]
    X, Y = 6, 10
    block.fill('white')
    for n in (a, b, c) :
        for xy in n :
            x = X + xy[0] * 4
            y = Y + xy[1] * 4
            screen.blit(block, (x, y))
        X += 32

def mark() :
    #显示分数
    global M, number
    a = M // 100
    b = M % 100 // 10
    c = M % 10
    a = number[a]
    b = number[b]
    c = number[c]
    X, Y = 395, 10
    block.fill('white')
    for n in (a, b, c) :
        for xy in n :
            x = X + xy[0] * 4
            y = Y + xy[1] * 4
            screen.blit(block, (x, y))
        X += 32

def hi() :
    #显示最高纪录
    global HI, number
    a = HI // 100
    b = HI % 100 // 10
    c = HI % 10
    a = number[a]
    b = number[b]
    c = number[c]
    X, Y = 263, 10
    block.fill('grey')
    for n in (a, b, c) :
        for xy in n :
            x = X + xy[0] * 4
            y = Y + xy[1] * 4
            screen.blit(block, (x, y))
        X += 32

#启动计时线程
time_count_thread = threading.Thread(target = count)
time_count_thread.start()

while True :
    #变量初始化
    KEY = 'up'
    lKEY = KEY
    x, y = 240, 240
    path = []
    path.append((x, y))
    fx, fy = random.randrange(20, 460, 20), random.randrange(20, 460, 20)
    while path.count((fx, fy)) != 0 :
        fx, fy = random.randrange(20, 460, 20), random.randrange(20, 460, 20)
    T = 0
    M = 0
    B = True

    while True :
        time.sleep(0.1)

        #检测是否按下退出按钮
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                exit()
        
        #检测键盘按键
        if (KEY == 'up' and lKEY != 'down') or (KEY == 'w' and lKEY != 's') :
            y -= 20
            lKEY = KEY
        elif (KEY == 'down' and lKEY != 'up') or (KEY == 's' and lKEY != 'w')  :
            y += 20
            lKEY = KEY
        elif (KEY == 'left' and lKEY != 'right') or (KEY == 'a' and lKEY != 'd')  :
            x -= 20
            lKEY = KEY
        elif (KEY == 'right' and lKEY != 'left') or (KEY == 'd' and lKEY != 'a')  :
            x += 20
            lKEY = KEY
        elif KEY == 'alt' or KEY == 'right alt' :
            B = False
            while True :
                pygame.event.wait()
                if KEY == 'space' :
                    KEY = lKEY
                    B = True
                    break
                elif KEY == 'esc' :
                    pygame.quit()
                    if M > HI :
                        HI = M
                        db.set('HiMark', HI)
                        db.dump()
                    exit()
            continue
        elif KEY == 'esc' :
            pygame.quit()
            if M > HI :
                HI = M
                db.set('HiMark', HI)
                db.dump()
            exit()
        else :
            KEY = lKEY
            continue

        #检测是否碰撞或吃掉食物
        if crash() :
            break
        if eat() :
            M += 1
            fx, fy = random.randrange(20, 460, 20), random.randrange(20, 460, 20)
            while path.count((fx, fy)) != 0 :
                fx, fy = random.randrange(20, 460, 20), random.randrange(20, 460, 20)
        else :
            del path[0]
        
        #更新屏幕内容
        path.append((x, y))
        screen.fill('black')
        snake()
        food()
        timer()
        mark()
        hi()
        pygame.display.flip()

    #保存最高纪录
    if M > HI :
        HI = M
        db.set('HiMark', HI)
        db.dump()
    
    B = False

    #检测是否退出或再来一局
    while True :
        event = pygame.event.wait()
        if event.type == pygame.QUIT :
            pygame.quit()
            exit()
        elif KEY == 'esc' :
            pygame.quit()
            exit()
        elif KEY == 'return' or KEY == 'enter' :
            break
