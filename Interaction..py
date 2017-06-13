import pygame
from random import randint

pygame.init()

Interaction = pygame.display.set_mode((480,640))
pygame.display.set_caption('Interaction')

class Sound():
    
    def Evil_Chef_voice_start():
        
        Evil_Chef_sound_start = pygame.mixer.Sound("Evil_Chef_Start.ogg")
        Evil_Chef_sound_start.play()
        Evil_Chef_sound_start.set_volume(0.3)
        
    def Evil_Chef_voice_end():
        
        Evil_Chef_sound_end = pygame.mixer.Sound("Evil_Chef_End.ogg")
        Evil_Chef_sound_end.play()

class Music():
    
    def Evil_Boss_music():
        #fiox
        pass

    
    def MenuMusic():
        
        pygame.mixer.music.load("Interaction_MenuMusic.mp3")
        pygame.mixer.music.play(5)
        pygame.mixer.music.set_volume(1.0)
        

class Instancevariables():
    
    MainMenu = 0.1
    
class TemporaryVariables():
    
    MainMenuTemp = True
    
class shapes():
    
    """Colours and shapes (text) could be created here."""
    
    light_blue = (123,200,208)
    red = (255,0,0)
    white = (255,255,255)
    black = (0,0,0)
    Gray = (146,141,141)
    
    def text(String, Text_x, Text_y, letter_colour,background_colour):
        
        background = pygame.Surface((400, 50))
        background = background.convert()
        background.fill((background_colour))
        font = pygame.font.Font(None, 25)
        text = font.render(String, 1, (letter_colour))
        textpos = text.get_rect()
        textpos.centerx = background.get_rect().centerx
        background.blit(text, textpos)
        Interaction.blit(background, (Text_x, Text_y))
        
    def Player_bullet(x,y):
        
        pygame.draw.polygon(Interaction,(59,100,255),((x,y),(x+30,y),(x+15,y+30)))
        
class NPCs():
    
    """NPCs are created here including the Player."""
    
    def player(x,y):
        
        pygame.draw.rect(Interaction,(255,255,255), ((x,y),(50,60)),0)
        pygame.draw.rect(Interaction,(0,0,0),((x+10,y+5),(10,5)),0)
        pygame.draw.rect(Interaction,(0,0,0),((x+30,y+5),(10,5)),0)                                
        pygame.draw.rect(Interaction,(0,0,0),((x+10,y+15),(10,10)),0)
        pygame.draw.rect(Interaction,(0,0,0),((x+30,y+15),(10,10)),0)
        pygame.draw.rect(Interaction,(0,0,0),((x+20,y+30),(10,10)),0)
        pygame.draw.rect(Interaction,(0,0,0),((x+10,y+45),(30,5)),0)
        
    def Evil_chef_alive(x,y):
        
        pygame.draw.rect(Interaction,(255,0,0),((x,y),(100,20)),0)
        pygame.draw.rect(Interaction,(0,200,0),((x+5, y+5),(20,3)),0)
        pygame.draw.rect(Interaction,(0,200,0),((x+75,y+5),(20,3)),0)
        pygame.draw.rect(Interaction,(0,0,0),((x+25,y+10),(50,2)),0)
        pygame.draw.rect(Interaction,(0,0,0),((x+10,y+15),(80,3)),0)
        
    def Evil_chef_dead(x,y):
        
        pygame.draw.rect(Interaction,(255,0,0),((x,y),(100,20)),0)
        pygame.draw.rect(Interaction,(0,200,0),((x+5, y+5),(20,3)),0)
        pygame.draw.rect(Interaction,(0,200,0),((x+90,y+5),(20,3)),0)
        pygame.draw.rect(Interaction,(0,0,0),((x+7,y+10),(50,5)),0)
        pygame.draw.rect(Interaction,(0,0,0),((x+10,y+15),(80,3)),0)

        
class InteractionGame(shapes,TemporaryVariables, Music, Instancevariables, Sound):
    
    def game_loop(self):
        
        game_status = False
        
        """Creating object to track time ( tick-rate )"""
        
        tick_rate = pygame.time.Clock()
        
        """Game_loop"""
        
        while not game_status:
            
            """Event handling"""
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_status = True
                    
                """Player Movement"""
                
                player_a, player_d, player_w, player_s = 0, 0, 0, 0
                Movement_trigger = False
                Movement_allow = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        player_a = -5
                        Movement_trigger = True
                        Movement = "player_a"
                    if event.key == pygame.K_d:
                        player_d = 5
                        Movement_trigger = True
                        Movement = "player_d"
                    if event.key == pygame.K_w:
                        player_w = -5
                        Movement_trigger = True
                        Movement = "player_w"
                    if event.key == pygame.K_s:
                        player_s = 5
                        Movement_trigger = True
                        Movement = "player_s"
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        player_a = 0
                        Movement_trigger = False
                    if event.key == pygame.K_d:
                        player_d = 0
                        Movement_trigger = False
                    if event.key == pygame.K_w:
                        player_w = 0
                        Movement_trigger = False
                    if event.key == pygame.K_s:
                        player_s = 0
                        Movement_trigger = False
                      
            
            
            
            """   Instances   """
            #Activate the boss when the player experiments with w key
            """MainMenu"""
            
            if self.MainMenu == 0.1:
                
                """Colour for MainMenu"""
                
                Interaction.fill(self.light_blue)
                
                """Pre-defined variables MainMenu"""
                
                if self.MainMenuTemp == True:
                    self.MainMenuTemp = False
                    player_x = 215
                    player_y = 580
                    Evil_Chef_Activate = False
                    Evil_Chef_move_x = 20
                    Evil_Chef_move_y = 20
                    Evil_Chef_trigger_move = 0.25
                    Evil_Chef_condition = 0
                    Evil_Chef_Voice_start = False
                    Music.MenuMusic()
                    
                """Movement Changes for MainMenu"""
                
                if Movement_trigger == True:
                    if Movement == "player_a":
                        player_x -= 5
                    if Movement == "player_d":
                        player_x += 5
                    if Movement == "player_s":
                        Evil_Chef_Activate = True
                        if Evil_Chef_Voice_start == False:
                            Sound.Evil_Chef_voice_start()
                            Evil_Chef_Voice_start = True
                    
                        
                    if Movement_allow == True:
                        if Movement == "player_w":
                            player_y -= 5
                        if Movement == "player_s":
                            player_y += 5
                            
                """Boundaries Main menu"""
                
                if player_x <= 0:
                    player_x = 0
                if player_x >= 430:
                    player_x = 430
                if player_y >= 580:
                    player_y = 580
                if player_y <= 0:
                    player_y = 0
                
                
                """AI movement"""
                
                if Evil_Chef_Activate == True:
                    shapes.text("Try me and you will fail.", 30, 100, self.black,self.light_blue)
                    Evil_Chef_text_x = Evil_Chef_move_x - 150
                    Evil_Chef_text_y = Evil_Chef_move_y - 20
                    shapes.text("5", Evil_Chef_text_x, Evil_Chef_text_y, self.red,self.light_blue)
                    if Evil_Chef_trigger_move == 0.25:
                        Evil_Chef_move_x += 4
                        Evil_Chef_condition = 0
                        if Evil_Chef_move_x >= 360:
                            Evil_Chef_move_x = 360
                            Evil_Chef_trigger_move = 0.5
                    if Evil_Chef_trigger_move == 0.5:
                        Evil_Chef_move_x -= 4
                        if Evil_Chef_condition == 0:
                            while True:
                                Evil_Chef_move_rx1 = randint(200,360)
                                if Evil_Chef_move_rx1 % 10 == 0:
                                    Evil_Chef_move_rx2 = Evil_Chef_move_rx1 - 80
                                    Evil_Chef_condition = 1
                                    break
                        if Evil_Chef_move_x <= Evil_Chef_move_rx1:
                            Evil_Chef_move_x = Evil_Chef_move_rx1
                            Evil_Chef_trigger_move = 0.75
                    if Evil_Chef_trigger_move == 0.75:
                        Evil_Chef_move_x -= 1
                        if Evil_Chef_move_x == Evil_Chef_move_rx2:
                            Evil_Chef_trigger_move= 1
                            Evil_Chef_condition = 0
                    if Evil_Chef_trigger_move == 1:
                        Evil_Chef_move_x -= 4
                        if Evil_Chef_move_x <= 20:
                            Evil_Chef_move_x = 20
                            Evil_Chef_trigger_move = 0.25
                elif Evil_Chef_Activate == False:
                    shapes.text("Press A and D, but what about the W or S?", 30, 100, self.white,self.light_blue)
                
                """Npc creation, prototype MainMenu"""
                
                NPCs.Evil_chef_alive(Evil_Chef_move_x,Evil_Chef_move_y)
                
                NPCs.player(player_x,player_y)
                
                
            pygame.display.update()

            tick_rate.tick(60)
            
Interaction_game = InteractionGame()
Interaction_game.game_loop()
pygame.quit()
quit()
                



