import pygame
import time
from random import randint
pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Balls')

Randomcolour = (randint(1, 255),randint(1, 255),randint(1, 255))

black = (0,0,0)
white = (255,255,255)
blue = ( 0, 0, 255)
blue1 = ( 59, 185, 227)
Red = ( 255, 0, 0)
olive = ( 128, 128, 0)
Brown = ( 150, 85, 32)
Brownish = ( 91, 9, 121)
Gray = ( 146, 141, 141)
Green = ( 2, 74, 41)
Gay = pygame.mixer.Sound('C:/PygameMusic/Voice/PygameGay.ogg')
ProjectileImg = pygame.image.load('C:/PygamePics/Projectile.png')
ballsImg = pygame.image.load('C:/PygamePics/seriouslyfuckthispicture.png')
bossImg = pygame.image.load('C:/PygamePics/Bosspicture.png')
skeletonImg = pygame.image.load('C:/PygamePics/Body.png')
#instance 0
def entrance():
    entrance = pygame.draw.rect(gameDisplay,(Brown),((750,450),(50, 80)) ,0)
    knob = pygame.draw.rect(gameDisplay,(0,0,0), ((780,470),(10,10)), 0)     
    
def gap(x, y):
    entrance = pygame.draw.rect(gameDisplay,(white), ((x, y), (50, 80)), 0)
    pygame.display.update()
#Instance 1
def Door(): 
    door = pygame.draw.rect(gameDisplay,(Brown),((0, 450), (50,80)), 0)
    knob = pygame.draw.rect(gameDisplay,(black), ((0,470),(10,10)), 0)
    pass
def skeleton(x, y):
    gameDisplay.blit(skeletonImg, (x, y))
def barrier(x, y, Colour1, Colour2, Colour3):
    barrier1 = pygame.draw.rect(gameDisplay,(Colour1),((100 ,0 ),(20 ,400 )), 0)
    barrier2 = pygame.draw.rect(gameDisplay,(Colour2),((100 ,400 ),(x , y)), 0)
    barrier3 = pygame.draw.rect(gameDisplay,(Colour3),((700 ,0),(20 ,400 )), 0)
    
def Spawnline():
    spawnline = pygame.draw.rect(gameDisplay,(blue),((120,0),(580 ,10)), 0)
def Projectile(x,y):
    gameDisplay.blit(ProjectileImg, (x,y))
def Progressbar(Progress):
    Bar = pygame.draw.rect(gameDisplay, (Brownish), ((120 , 450  ), (580 ,100 )), 0 )
    Progress = pygame.draw.rect(gameDisplay, (white),((140, 470 ), (Progress ,60 )) , 0 )
    Goal = pygame.draw.rect(gameDisplay, (black), ((680 ,470 ), (10 ,60 )), 0 )
def text(String, Text_x, Text_y):
    background = pygame.Surface((400, 50))
    background = background.convert()
    background.fill((Gray))
    font = pygame.font.Font(None, 25)
    text = font.render(String, 1, (black))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)
    gameDisplay.blit(background, (Text_x, Text_y))
def EndPortal():
    Health = pygame.draw.rect(gameDisplay,(Brownish),((650, 100),(100,500)), 0)
    Bar = pygame.draw.rect(gameDisplay,(Red), ((675, 125), (50 ,400 )), 0)
def HealthBar(x):
    Bar = pygame.draw.rect(gameDisplay,(Green),((100,5), (x,10)) , 0)


#boss
def boss(x, y):
    boss = gameDisplay.blit(bossImg, (x,y))

#Player
def balls(x, y):
    Barrier1 = gameDisplay.blit(ballsImg, (x,y))  
def MiniClip(x, y):
    Attachment = pygame.draw.rect(gameDisplay,(blue1), ((x,y), (25,15)), 0)
#tick rate
clock = pygame.time.Clock()

def rectobj():
    co1, co2, co3, lo = 100, 100, 100, (10, 50)
    for item in list(range(7)):
        
        Random_colour = (randint(1, 255), randint(1, 255), randint(1, 255))
        pygame.draw.rect(gameDisplay, Random_colour, ((co1, 100), (lo)),0)
        if co1 >= 500:
            co1 = 500
        co1 += 100
        
    for item in list(range(7)):
        
        Random_colour = (randint(1, 255), randint(1, 255), randint(1, 255))
        pygame.draw.rect(gameDisplay, Random_colour, ((co2, 300), (lo)), 0)
        if co2 >= 500:
            co2 = 500
        co2 += 100
        
    for item in list(range(7)):
        
        Random_colour = (randint(1, 255), randint(1, 255), randint(1, 255))
        pygame.draw.rect(gameDisplay, Random_colour, ((co3, 500), (lo)), 0)
        if co3 >= 500:
            co3 = 500
        co3 += 100
#Music
def onemusic():
    pygame.mixer.music.stop()
    Background_music = pygame.mixer.music.load('C:/PygameMusic/Music/Pygame/Puzzle_music_final.ogg')
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1, 0.0)
def twomusic():
    pygame.mixer.music.stop()
    Projectile_music = pygame.mixer.music.load('C:/PygameMusic/Music/Pygame/Puzzle_music_instance#2.ogg')
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1, 0.0)
def threemusic():
    pygame.mixer.music.stop()
    boss_music = pygame.mixer.music.load('C:/PygameMusic/Music/Pygame/Puzzle_music_instance#3.ogg')
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1, 0.0)
def bossmusic():
    pygame.mixer.music.stop()
    boss_music = pygame.mixer.music.load('C:/PygameMusic/Music/Pygame/Puzzle_music_boss.ogg')
    pygame.mixer.music.set_volume(0.6)
    pygame.mixer.music.play(-1, 0.0)
def GayVoice():
    pygame.mixer.music.stop()
    boss_music = pygame.mixer.music.load('C:/PygameMusic/Voice/Semen.ogg')
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(1, 0.0)
    
def gameloop():
    boss_battle_list = [0.2, 0.4, 0.6, 0.8]
    boss_battle_movement = 0
    start = 1
    instance = 0
    x = (50)
    y = (50)
    x_right = 0
    x_left = 0
    y_up = 0
    y_down = 0
    car_speed = 0
    boss_battle = 1
    Projectile_x = 120
    Projectile_y = 20
    Projectile_switch = 1
    boss_x = 360
    boss_y = 50
    Health_bar = 570
    Progress_bar = 0
    Bar_length = 20
    Spot_on = 1
    Spawn = 1
    Spawncatch = 1
    Allow = 1
    crashed = False
    fucker = True
    strat = 1
    tracker = 0
    Fagoat = 1
    musiclist = [onemusic, twomusic, threemusic]
    onemusic()
    right = 1
    left = 0
    Push_left = 0
    Push_right = 0
    Origggin  = 0
    Origggin1 = 0
    Origgin2 = 0
    Dogmarsh = y - 40
    #gameDisplay.blit(ProjectileImg, (x,y))
    while not crashed:
        if instance == 3:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crashed = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        x_left = -10
                    elif event.key == pygame.K_d:
                        x_right = 10
                    elif event.key == pygame.K_w:
                        y_up = -10
                    elif event.key == pygame.K_s:
                        y_down = 10
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        x_left = 0
                    elif event.key == pygame.K_d:
                        x_right = 0
                    elif event.key == pygame.K_w:
                        y_up = 0
                    elif event.key == pygame.K_s:
                        y_down = 0
        if instance == 0 or boss_battle == 1 :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crashed = True
                ###############   
                #keyboard input handling
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        x_left = -5
                    elif event.key == pygame.K_d:
                        x_right = 5
                    elif event.key == pygame.K_w:
                        y_up = -5
                    elif event.key == pygame.K_s:
                        y_down = 5
                    elif event.key == pygame.K_q:
                        y_up = -5
                        x_left = -5
                    elif event.key == pygame.K_e:
                        y_up = -5
                        x_left = 5
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        x_left = 0
                    elif event.key == pygame.K_d:
                        x_right = 0
                    elif event.key == pygame.K_w:
                        y_up = 0
                    elif event.key == pygame.K_s:
                        y_down = 0
                    elif event.key == pygame.K_q:
                        y_up = 0
                        x_left = 0
                    elif event.key == pygame.K_e:
                        y_up = 0
                        x_left = 0
            ######################
        




            #Screen boundaries
        if x < 0:
            x_left = 0           
        if y < 0:
            y_up = 0            
        if y > 550:
            y_down = 0        
        if x > 750:
            x_right = 0
        ######
        #Door Collision.
        if instance == 0:
            if y == 400 and x >= 700:
                y_down = 0
            if x == 700 and y >= 400 and y < 531:
                x_right = 0
                gap(750, 450)
                time.sleep(0.3)
                if boss_battle == 2:
                    instance = 2
                    Spawncatch = 0
                else:
                    #originally 0.5
                    instance = 3
                Spawncatch = 0
            if y == 530 and x >= 700:
                y_up = 0
        ######
        #Barrier collision.
        #No boss battle ( power grab )
        if instance == 1 and boss_battle == 1:
            #Door collision POWER GRAB
            if x == 45 and y >= 401 and y <=531:
                x_left = 0
                gap(0, 450)
                time.sleep(0.3)
                instance = 0
                Spawn = 0
            if y == 530 and x <= 50:
                y_up = 0
            if y == 400 and x <=50:
                y_down = 0
            ###
            if x == 50 and y >= 0 and y <= 399:
                x_right = 0
            if x == 120 and y >= 0 and y <= 399:
                x_left = 0 
            if x == 720 and y >= 0 and y <= 399:
                x_left = 0
            if x == 650 and y >= 0 and y <= 399:
                x_right = 0
            if y == 400 and x <= 119:
                y_up = 0
            if y == 400 and x >= 649 and x <= 720:
                y_up = 0
            if y == 380 and x >= 120 and x <= 699:
                boss_battle = 0.25
                y = 350
                x = 380
                y_up = 0
                y_down = 0
                x_right = 0
                x_left = 0
                
                
        ######    
        if boss_battle == 0 :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crashed = True
                ###############   
                #Upgraded movement for mini-game (catch & grab game)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        x_left = -10
                    elif event.key == pygame.K_d:
                        x_right = 10
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        x_left = 0
                    elif event.key == pygame.K_d:
                        x_right = 0
        if instance == 2 :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crashed = True
                ###############   
                #Upgraded movement for mini-game (catch & grab game)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        x_left = -10
                    elif event.key == pygame.K_d:
                        x_right = 10
                    elif event.key == pygame.K_w:
                        y_up = -10
                    elif event.key == pygame.K_s:
                        y_down = 10
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        x_left = 0
                    elif event.key == pygame.K_d:
                        x_right = 0
                    elif event.key == pygame.K_w:
                        y_up = 0
                    elif event.key == pygame.K_s:
                        y_down = 0
        
        #Power grab barrier boundaries.
        if instance == 1 and boss_battle == 0:
            if x <= 120 and y >= 0 and y <= 600:
                x_left = 0 
            if x >= 650 and y >= 0 and y <= 600:
                x_right = 0
            if y >= 350 and x >= 0 and x <= 800:
                y_down = 0
            if y <= 10 and x >=0 and x <= 699:
                y_up = 0
        if instance == 2 and boss_battle == 2:
            #fixed ;)
            if x + x_right >= 750:
                x = 750
                x_right = 0
            if y+ y_down >= 550:
                y = 550
                y_down = 0
            if x + x_left <= 0:
                x = 0
                x_left = 0
            if y + y_up <= 0:
                y = 0
                y_up = 0
            #fixed ;)
            if x <= 45 and y >= 401 and y <=531:
                x_left = 0
                gap(0, 450)
                time.sleep(0.3)
                instance = 0
                Spawn = 0
            if y == 530 and x <= 50:
                y_up = 0
            if y == 400 and x <=50:
                y_down = 0
            #Door2
            if y == 400 and x >= 700:
                y_down = 0
            if x >= 701 and y >= 400 and y < 531:
                x_right = 0
                instance = 3
                Fagoat = 1
            if y == 530 and x >= 700:
                y_up = 0
        if instance == 3:
            if x + x_right >= 750:
                x = 750
                x_right = 0
            if y+ y_down >= 550:
                y = 550
                y_down = 0
            if x + x_left <= 0:
                x = 0
                x_left = 0
            if y + y_up <= 0:
                y = 0
                y_up = 0
            if x <= 60:
                x_left = 0
                x = 60
            if x >= 650:
                x = 650
                x_right = 0
            if y <= 50:
                y_up = 0
                y == 50
            
            
        ##########
        x += x_right
        x += x_left
        y += y_up
        y += y_down
    
        if instance == 0:
            
            gameDisplay.fill(blue)
            
            rectobj()
        
            entrance()
            if Spawn == 0:
                x= 695
                balls(x ,y)
                Spawn = 1
            
            balls(x,y)
                
            
            
            pygame.display.update()
        if instance == 0.5:
            
            instance = 1    
        if instance == 1:
            gameDisplay.fill(Gray)
            Door()
            
            if boss_battle == 1:
                barrier(-620 , -20, olive, Red, Red)
                if Spawncatch == 0:
                    x = 50
                    balls(x ,y)
                    Spawncatch = 1
                balls(x,y)
            if boss_battle == 0.25:
                boss_battle = 0
            if boss_battle == 0:
                if pygame.mixer.music.get_busy() == False:
                    onemusic()
                if Allow == 1:
                    GayVoice()
                    Allow = 0
                
                Faggotry = False
                    
                barrier(620 , 20, Brownish, Red, Red)
                #####Progress system
                Origin = x
                for item in list(range(50)):
                    if x >= Projectile_x and x <= Projectile_x + 20 and y == Projectile_y + 40:
                        Spot_on = 1
                        break
                    x += 1
                x = Origin
                
                if Spot_on == 1:
                    ProjectileImg.fill(Gray)
                    Progress_bar += 1
                    if Progress_bar <= 26:
                        Bar_length += 20    
                    elif Progress_bar >= 28 and Progress_bar < 30:
                        Bar_length = 560
                        Progress_bar = 29
                    
                Spot_on = 0
                
                    
                Progressbar(Bar_length-20)
                ####Text (copied understand jackshit)
                text('Fill the bar by collecting Semen', 120, 550)
                ########Projectile system
                
                if Projectile_switch == 1:
                    gameDisplay.blit(ProjectileImg, (Projectile_x,Projectile_y))
                Projectile_y += 5
                
                if Projectile_y >= 350 :
                    Projectile_x = randint(120, 670)
                    Projectile_y = 20
                    ProjectileImg.fill(white)
                    
                
                #######    
                balls(x,y)
            Spawnline()
            pygame.display.update()
            if start == 1:
                x = 50
                y = 450
                start = 0
            if Progress_bar == 29:
                instance = 2
                boss_battle = 2
                BongCock = 1
                print(instance)
                Progress_bar = 30
        if instance == 2:
            if Spawncatch == 0:
                    x = 50
                    balls(x ,y)
                    print('IS SPAWNCATCHER RUNNING?!')
                    Spawncatch = 1
            gameDisplay.fill(Gray)
            Door()
            entrance()
            barrier(570 , 20, Brownish, Brownish, Brownish)
            text('YOU ARE FREE!', 120, 670)
            balls(x,y)
            pygame.display.update()
        if instance == 3:
            gameDisplay.fill(black)
             
            if Fagoat == 1:
                x = 50
                balls(x,y)
                bossmusic()
                Faggot = 0
            rectobj()
            boss(boss_x, boss_y)
            if right == 1:
                    boss_x -= 5
                    if boss_x == 120:
                        right = 0
                        left = 1
            if left == 1:
                    boss_x += 5
                    if boss_x == 600:
                        left = 0
                        right = 1
            #boss does projectile
            ##gameDisplay.blit(ProjectileImg, (Projectile_x,Projectile_y))
            ##if Projectile_y >= 350 :
                    ##Projectile_x = randint(120, 670)
                    ##Projectile_y = 20
                    ##ProjectileImg.fill(white)
            balls(x,y)
            pygame.display.update()
            
            
        clock.tick(60)

gameloop()

pygame.quit()
quit()
''' Have the "boss does projectile" section complete with the end result
being a portal leading to the end game screen.'''
