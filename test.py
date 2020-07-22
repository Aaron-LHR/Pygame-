import sys,pygame,random
class bullet():
    def __init__(self,bulletpos,bulletdirection):
        self.bulletpos = bulletpos
        self.bulletdirection = bulletdirection
def bulletset(direction):
    if direction == 0:return [heroimagerect.left+100,heroimagerect.top+50]
    elif direction == 1:return [heroimagerect.left-12,heroimagerect.top+50]
class insect():
    def __init__(self,insectpos,insectdirection):
        self.insectpos = insectpos
        self.insectdirection = insectdirection
def insectset(direction):
    if direction == 0: return [width-101,ground[0]+39]
    elif direction == 1:return [0, ground[0]+39]
class dragon():
    def __init__(self,dragonpos,dragondirection):
        self.dragonpos = dragonpos
        self.dragondirection = dragondirection
def dragonset(direction):
    if direction == 0:return [width-101,random.randint(0,600)]
    elif direction == 1:return [0, random.randint(0,600)]
class mouse():
    def __init__(self,mousepos,mousedirection):
        self.mousepos = mousepos
        self.mousedirection = mousedirection
def mouseset(direction):
    if direction == 0:return [width-101,random.randint(0,600)]
    elif direction == 1:return [0, random.randint(0,600)]
pygame.init()
size = width,height = 1600,900;ground = [height-235,height-245];screen = pygame.display.set_mode(size) #初始化
pygame.display.set_caption("Kingdom Defender");pygame.mixer_music.load("赤色要塞.mp3");pygame.mixer_music.play()
startbjimage = pygame.image.load("开始游戏.png");startbjimage_1 = pygame.image.load("开始游戏_1.png")
startbjimagelist = [startbjimage,startbjimage_1];smf = 0;game_over = pygame.image.load("游戏结束.png")
global speed;global on_ground;global score;global grade;global direction;global bulletexist         #子弹是否消失
speed = [0,0];on_ground = 1;score = 0;direction = 0;bulletexist = 1;screen.blit(startbjimage,(0,0));
start = 0;chapter = [0,0,0];time = 0;pygame.display.update();fps = 300;fclock = pygame.time.Clock()
font = pygame.font.SysFont('arial',40);font_height = font.get_linesize()
heroleftimage = pygame.image.load("heroleft.png");herorightimage = pygame.image.load("heroright.png")
herolist = [herorightimage,heroleftimage];heroimagerect = heroleftimage.get_rect()
bulletimage=pygame.image.load("子弹.png");bulletlist = []
first_level = pygame.image.load("第一关.png");bgimage_1 = pygame.image.load("第一关背景.png")
shortstage = pygame.image.load("短平台.png");longstage = pygame.image.load("长平台.png")
shortstage_date = [900,1370,210];longstage_date = [170,800,345]      #左，右，高
second_level = pygame.image.load("第二关.png");bgimage_2 = pygame.image.load("第二关背景.png")
balcony_date = [0,415,415];stepdate_1 = [500,700,235];stepdate_2 = [700,825,127];platform_date = [1100,width,130]
third_level = pygame.image.load("第三关.png");bgimage_3 = pygame.image.load("第三关背景.png")
walldate_1 = [0,60,550];walldate_2 = [1540,width,550]
insectleft_1 = pygame.image.load("虫左1.png");insectleft_2 = pygame.image.load("虫左2.png")
insectleft_3 = pygame.image.load("虫左3.png");insectleft_4 = pygame.image.load("虫左4.png")
insectright_1 = pygame.image.load("虫右1.png");insectright_2 = pygame.image.load("虫右2.png")
insectright_3 = pygame.image.load("虫右3.png");insectright_4 = pygame.image.load("虫右4.png")
insectright_dead = pygame.image.load("死虫右.png");insectleft_dead = pygame.image.load("死虫左.png")
insectimage_left = [insectleft_1, insectleft_1, insectleft_1, insectleft_1, insectleft_2, insectleft_2, insectleft_2, insectleft_2, insectleft_3, insectleft_3, insectleft_3, insectleft_3, insectleft_4, insectleft_4, insectleft_4, insectleft_4]
insectimage_right = [insectright_1, insectright_1, insectright_1, insectright_1, insectright_2, insectright_2, insectright_2, insectright_2, insectright_3, insectright_3, insectright_3, insectright_3, insectright_4, insectright_4, insectright_4, insectright_4]
insectlist = [];cmf = 0     #虫子动画
dragonleft_1 = pygame.image.load("龙左1.png");dragonleft_2 = pygame.image.load("龙左2.png")
dragonleft_3 = pygame.image.load("龙左3.png");dragonright_1 = pygame.image.load("龙右1.png")
dragonright_2 = pygame.image.load("龙右2.png");dragonright_3 = pygame.image.load("龙右3.png")
dragonright_right = pygame.image.load("死龙右.png");dragonright_left = pygame.image.load("死龙左.png")
dragonimage_left = [dragonleft_1,dragonleft_1,dragonleft_1,dragonleft_1,dragonleft_2,dragonleft_2,dragonleft_2,dragonleft_2,dragonleft_3,dragonleft_3,dragonleft_3,dragonleft_3]
dragonimage_right = [dragonright_1,dragonright_1,dragonright_1,dragonright_1,dragonright_2,dragonright_2,dragonright_2,dragonright_2,dragonright_3,dragonright_3,dragonright_3,dragonright_3]
dragonlist = [];dmf = 0     #龙动画
mouseleft_1 = pygame.image.load("老鼠左1.png");mouseleft_2 = pygame.image.load("老鼠左2.png")
mouseleft_3 = pygame.image.load("老鼠左3.png");mouseright_1 = pygame.image.load("老鼠右1.png")
mouseright_2 = pygame.image.load("老鼠右2.png");mouseright_3 = pygame.image.load("老鼠右3.png")
mouseimage_left = [mouseleft_1,mouseleft_1,mouseleft_1,mouseleft_1,mouseleft_2,mouseleft_2,mouseleft_2,mouseleft_2,mouseleft_3,mouseleft_3,mouseleft_3,mouseleft_3]
mouseimage_right = [mouseright_1,mouseright_1,mouseright_1,mouseright_1,mouseright_2,mouseright_2,mouseright_2,mouseright_2,mouseright_3,mouseright_3,mouseright_3,mouseright_3]
mouselist = [];mmf = 0     #老鼠动画
def bull():
    global score;    global bulletexist
    for i in bulletlist:
        bulletexist = 1;        screen.blit(bulletimage, i.bulletpos)
        if i.bulletdirection == 0:
            i.bulletpos[0] += 20
            if i.bulletpos[0] > width + 50: bulletlist.remove(i)
        elif i.bulletdirection == 1:
            i.bulletpos[0] -= 20
            if i.bulletpos[0] < -50:bulletlist.remove(i)         # 子弹移动
        for j in insectlist:
            if i.bulletpos[0] >= j.insectpos[0] and i.bulletpos[0] + 20 <= j.insectpos[0] + 116 and i.bulletpos[1] >= \
                    j.insectpos[1] and i.bulletpos[1] + 20 <= j.insectpos[1] + 68:
                screen.blit(insectright_dead, (i.bulletpos[0], i.bulletpos[1] - 15));pygame.display.update()
                insectlist.remove(j);bulletlist.remove(i);break  # 判定虫子死亡
        if bulletexist != 0:
            for j in dragonlist:
                if i.bulletpos[0] >= j.dragonpos[0] and i.bulletpos[0] + 20 <= j.dragonpos[0] + 158 and i.bulletpos[
                    1] >= j.dragonpos[1] and i.bulletpos[1] + 20 <= j.dragonpos[1] + 129:
                    dragonlist.remove(j);bulletlist.remove(i);bulletexist = 0;score += 25;break # 判定龙死亡
        if bulletexist != 0:
            for j in mouselist:
                if i.bulletpos[0] >= j.mousepos[0] and i.bulletpos[0] + 20 <= j.mousepos[0] + 158 and i.bulletpos[1] >= \
                        j.mousepos[1] and i.bulletpos[1] + 20 <= j.mousepos[1] + 129:
                    bulletlist.remove(i);mouselist.remove(j);bulletexist = 0;score += 25;break   # 判定老鼠死亡
def key_board():
    global speed;global on_ground;global direction
    for event in pygame.event.get():
        if event.type == pygame.QUIT:sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: speed[0] = -10;direction = 1
            elif event.key == pygame.K_RIGHT:speed[0] = 10;direction = 0
            elif event.key == pygame.K_UP:
                if start == 1:
                    if on_ground == 1:speed[1] = -21;on_ground = 0
                elif start == 2:
                    if on_ground == 1:speed[1] = -22;on_ground = 0          #读取键盘输入
                elif start == 3:
                    if on_ground == 1:speed[1] = -35;on_ground = 0
            elif event.key == pygame.K_DOWN:
                if on_ground == 0 and start == 3:speed[1] += 5
            elif event.key == pygame.K_x:bulletlist.append(bullet(bulletset(direction), direction))
            elif event.key == pygame.K_ESCAPE:sys.exit()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:speed[0] = 0
            elif event.key == pygame.K_RIGHT:speed[0] = 0
def monster():
    if start == 1 or start == 3:
        for i in insectlist:
            if i.insectdirection == 0:
                i.insectpos[0] -= 10
                if i.insectpos[0] > width + 50:insectlist.remove(i)
                screen.blit(insectimage_left[cmf % 16], i.insectpos)  # 虫子移动
            elif i.insectdirection == 1:
                i.insectpos[0] += 10
                if i.insectpos[0] < -50:insectlist.remove(i)
                screen.blit(insectimage_right[cmf % 16], i.insectpos)
        insect_direction = random.randint(0, 1)  # 虫子方向
        if random.randint(1, 19) % 10 == 0:insectlist.append(insect(insectset(insect_direction), insect_direction))  # 随机出虫子
    if start == 1 or start == 2 or start == 3:
        for i in dragonlist:
            if i.dragondirection == 0:
                i.dragonpos[0] -= 5;i.dragonpos[1] += random.randint(-7, 7)
                if i.dragonpos[0] > width + 50:
                    dragonlist.remove(i)
                screen.blit(dragonimage_left[cmf % 12], i.dragonpos)  # 龙移动
            elif i.dragondirection == 1:
                i.dragonpos[0] += 5;i.dragonpos[1] += random.randint(-7, 7)
                if i.dragonpos[0] < -50:
                    dragonlist.remove(i)
                screen.blit(dragonimage_right[cmf % 12], i.dragonpos)
            if i.dragonpos[1] > height or i.dragonpos[1] < -100:
                dragonlist.remove(i)
        dragon_direction = random.randint(0, 1)
        if random.randint(1, 19) % 10 == 0:  # 随机出龙
            dragonlist.append(dragon(dragonset(dragon_direction), dragon_direction))
    if start == 2 or start == 3:
        for i in mouselist:
            if i.mousedirection == 0:
                i.mousepos[0] -= 5;i.mousepos[1] += random.randint(-7, 7)
                if i.mousepos[0] > width + 50:
                    mouselist.remove(i)
                screen.blit(mouseimage_left[cmf % 12], i.mousepos)  # 老鼠移动
            elif i.mousedirection == 1:
                i.mousepos[0] += 5;i.mousepos[1] += random.randint(-7, 7)
                if i.mousepos[0] < -50:mouselist.remove(i)
                screen.blit(mouseimage_right[cmf % 12], i.mousepos)
            if i.mousepos[1] > height or i.mousepos[1] < -100:mouselist.remove(i)
        mouse_direction = random.randint(0, 1)
        if random.randint(1, 19) % 10 == 0: mouselist.append(mouse(mouseset(mouse_direction), mouse_direction)) # 随机出老鼠
def collide():      #判定碰撞
    global start;global speed;global grade
    for i in insectlist:
        if (heroimagerect.left - i.insectpos[0] <= 115 and i.insectpos[
            0] - heroimagerect.left <= 101 and heroimagerect.top - i.insectpos[1] <= 70 and i.insectpos[
            1] - heroimagerect.top <= 104):
            while True:  # 撞虫子
                end_score = font.render(grade, True, (255, 255, 255))
                screen.blit(game_over, (0, 0));screen.blit(end_score, (750, 450));pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE: sys.exit()
                        elif event.key == pygame.K_SPACE:start = 0
                if start == 0:speed = [0, 0];insectlist.clear();dragonlist.clear();bulletlist.clear();break
    for i in dragonlist:
        if (heroimagerect.left - i.dragonpos[0] <= 149 and i.dragonpos[
            0] - heroimagerect.left <= 101 and heroimagerect.top - i.dragonpos[1] <= 97 and i.dragonpos[
            1] - heroimagerect.top <= 104):# 撞龙
            while True:
                end_score = font.render(grade, True, (255, 255, 255));screen.blit(game_over, (0, 0))
                screen.blit(end_score, (750, 450));pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:sys.exit()
                        elif event.key == pygame.K_SPACE:start = 0
                if start == 0:speed = [0, 0];insectlist.clear();dragonlist.clear();bulletlist.clear();break
    for i in mouselist:
        if (heroimagerect.left - i.mousepos[0] <= 133 and i.mousepos[
            0] - heroimagerect.left <= 101 and heroimagerect.top - i.mousepos[1] <= 150 and i.mousepos[
            1] - heroimagerect.top <= 104):
            while True:  # 撞老鼠
                end_score = font.render(grade, True, (255, 255, 255));screen.blit(game_over, (0, 0))
                screen.blit(end_score, (750, 450));pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:sys.exit()
                        elif event.key == pygame.K_SPACE:start = 0
                if start == 0:speed = [0, 0];insectlist.clear();dragonlist.clear();bulletlist.clear();break
while True:
    smf += 1;mmf += 1
    if start == 0:
        insectlist.clear();dragonlist.clear();bulletlist.clear();mouselist.clear();score = 0;time = 0
        screen.blit(startbjimagelist[smf%2], (0, 0)); pygame.display.update();pygame.time.delay(500)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start = 1;screen.blit(first_level,(0,0));pygame.display.update();pygame.time.delay(1500)
                elif event.key == pygame.K_ESCAPE:sys.exit()
    elif start == 1:
        if chapter[0] == 0:
            heroimagerect = heroimagerect.move(800, ground[0]);screen.blit(herorightimage, heroimagerect)
            insectrect = [width-101,ground[0]+39];chapter[0] = 1
        screen.blit(bgimage_1,(0,0));key_board();bull();monster()
        if heroimagerect.left <= 0 :speed[0] = 0;heroimagerect = heroimagerect.move(1, 0)                     #判断边界
        elif heroimagerect.left >= width-101:speed[0] = 0; heroimagerect = heroimagerect.move(-1,0)
        dmf+=1;cmf+=1;time += 1;heroimagerect = heroimagerect.move(speed[0],speed[1])               #完成一帧
        screen.blit(herolist[direction], heroimagerect);grade = "score:{:>3}".format(score)
        rest_time = "time:{:>3}".format(1000 - time);text_time = font.render(rest_time,True,(0,0,0))
        text = font.render(grade, True, (0, 0, 0));screen.blit(text,(350,50));screen.blit(text_time,(800,50))
        pygame.display.update()
        if abs(heroimagerect.top - ground[0]) < 20: speed[1] = 0;heroimagerect.top = ground[0];on_ground = 1#判断跳跃
        elif abs(heroimagerect.top - ground[0]+shortstage_date[2]) < 16 and heroimagerect[0] > shortstage_date[0] and heroimagerect[0] < shortstage_date[1] and speed[1] >= 0:
            speed[1] = 0;heroimagerect.top = ground[0]-shortstage_date[2]; on_ground = 1
        elif abs(heroimagerect.top - ground[0]+longstage_date[2]) < 10 and heroimagerect[0] > longstage_date[0] and heroimagerect[0] < longstage_date[1] and speed[1] >= 0:
            speed[1] = 0;heroimagerect.top = ground[0]-longstage_date[2];on_ground = 1
        elif heroimagerect.top < ground[0]:speed[1]+=1
        collide()
        if time >=1:
            time = 0;start = 2;insectlist.clear();dragonlist.clear();bulletlist.clear()
            screen.blit(second_level,(0,0));pygame.display.update();pygame.time.delay(2500)
    elif start == 2:
        if chapter[1] == 0:
            heroimagerect = heroimagerect.move(0, -200);screen.blit(herorightimage, heroimagerect);chapter[1] = 1
        screen.blit(bgimage_2,(0,0));key_board();bull();monster()
        if heroimagerect.left < 0 :speed[0] = 0;heroimagerect = heroimagerect.move(-heroimagerect.left, 0)    #判断边界
        elif heroimagerect.left > width-101:speed[0] = 0; heroimagerect = heroimagerect.move(width-101-heroimagerect.left,0)
        elif heroimagerect.left > stepdate_1[0] - 15 and heroimagerect.left < (stepdate_1[1]+stepdate_1[0])/2 and  heroimagerect.top > ground[1] - stepdate_1[2]:
            speed[0] = 0; heroimagerect = heroimagerect.move(stepdate_1[0] - 15 - heroimagerect.left,0)
        elif heroimagerect.left < stepdate_1[1] and heroimagerect.left > (stepdate_1[1]+stepdate_1[0])/2 and heroimagerect.top > ground[1] - stepdate_1[2]:
            speed[0] = 0;heroimagerect = heroimagerect.move(stepdate_1[1] - heroimagerect.left,0)
        elif heroimagerect.left < stepdate_2[1] + 27 and heroimagerect.left > (stepdate_2[1]+stepdate_2[0])/2 and heroimagerect.top > ground[1] - stepdate_2[2]:
            speed[0] = 0;heroimagerect = heroimagerect.move(stepdate_2[1] + 27 - heroimagerect.left,0)
        elif heroimagerect.left > platform_date[0] and heroimagerect.left < (platform_date[1]+platform_date[0])/2 and  heroimagerect.top > ground[1] - platform_date[2]:
            speed[0] = 0; heroimagerect = heroimagerect.move(platform_date[0] - heroimagerect.left,0)
        dmf+=1;cmf+=1;time += 1;heroimagerect = heroimagerect.move(speed[0],speed[1])               #完成一帧
        screen.blit(herolist[direction], heroimagerect);rest_time = "time:{:>3}".format(1000 - time)
        text_time = font.render(rest_time, True, (255, 255, 255));screen.blit(text_time, (800, 50))
        grade = "score:{:>3}".format(score);text = font.render(grade, True, (255, 255, 255))
        screen.blit(text,(350,50));pygame.display.update()
        if abs(heroimagerect.top - ground[1]) < 20:speed[1] = 0;heroimagerect.top = ground[1];on_ground = 1#判断跳跃
        elif abs(heroimagerect.top - ground[1]+stepdate_1[2]) < 16 and heroimagerect[0] >= stepdate_1[0] and heroimagerect[0] <= stepdate_1[1] and speed[1] >= 0:
            speed[1] = 0;heroimagerect.top = ground[1]-stepdate_1[2];on_ground = 1
        elif abs(heroimagerect.top - ground[1]+stepdate_2[2]) < 16 and heroimagerect[0] >= stepdate_2[0] and heroimagerect[0] <= stepdate_2[1] and speed[1] >= 0:
            speed[1] = 0;heroimagerect.top = ground[1]-stepdate_2[2];on_ground = 1
        elif abs(heroimagerect.top - ground[1]+balcony_date[2]) < 10 and heroimagerect[0] >= balcony_date[0] and heroimagerect[0] <= balcony_date[1] and speed[1] >= 0:
            speed[1] = 0;heroimagerect.top = ground[1]-balcony_date[2];on_ground = 1
        elif abs(heroimagerect.top - ground[1]+platform_date[2]) < 10 and heroimagerect[0] >= platform_date[0] and heroimagerect[0] <= platform_date[1] and speed[1] >= 0:
            speed[1] = 0;heroimagerect.top = ground[1]-platform_date[2];on_ground = 1
        elif heroimagerect.top < ground[1]:speed[1]+=1
        collide()
        if time >= 1:
            time = 0;start = 3;insectlist.clear();dragonlist.clear();bulletlist.clear();screen.blit(third_level,(0,0))
            pygame.display.update(); pygame.time.delay(2500)
    elif start == 3:
        if chapter[2] == 0:
            insectlist.clear();dragonlist.clear();bulletlist.clear();mouselist.clear()
            heroimagerect = heroimagerect.move(0, -200);screen.blit(herorightimage, heroimagerect);chapter[2] = 1
        screen.blit(bgimage_3,(0,0));key_board();bull();monster()
        if heroimagerect.left < 0 :speed[0] = 0; heroimagerect = heroimagerect.move(-heroimagerect.left, 0)#判断边界
        elif heroimagerect.left > width-101: speed[0] = 0;heroimagerect = heroimagerect.move(width-101-heroimagerect.left,0)
        elif heroimagerect.left > walldate_1[0] and heroimagerect.left < walldate_1[1] and  heroimagerect.top < walldate_1[2]:
            speed[0] = 0;heroimagerect = heroimagerect.move(walldate_1[1] - heroimagerect.left,0)
        elif heroimagerect.left + 85 > walldate_2[0] and heroimagerect.top < walldate_2[2]:
            speed[0] = 0;heroimagerect = heroimagerect.move(walldate_2[0] - heroimagerect.left - 85,0)
        dmf+=1;cmf+=1;heroimagerect = heroimagerect.move(speed[0],speed[1])                     #完成一帧
        screen.blit(herolist[direction], heroimagerect);grade = "score:{:>3}".format(score)
        text = font.render(grade, True, (255, 255, 255));screen.blit(text,(700,50));pygame.display.update()
        if abs(heroimagerect.top - ground[1]) < 20:speed[1] = 0;heroimagerect.top = ground[1];on_ground = 1#判断跳跃
        elif heroimagerect.top < walldate_1[2] and heroimagerect.top > walldate_1[2]-15 and heroimagerect.left < walldate_1[1]:
            speed[1] = 0;heroimagerect = heroimagerect.move(0,walldate_1[2] - heroimagerect.top)
        elif heroimagerect.top < walldate_2[2] and heroimagerect.top > walldate_2[2]-15 and heroimagerect.left + 85 > walldate_2[0]:
            speed[1] = 0;heroimagerect = heroimagerect.move(0,walldate_2[2] - heroimagerect.top)
        elif heroimagerect.top < ground[1]:speed[1]+=1
        collide()
