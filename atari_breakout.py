import pygame,sys,time,random
from pygame.locals import *
pygame.init()

clock = pygame.time.Clock()
setDisplay = pygame.display.set_mode((600,400))
pygame.display.set_caption("Atari breakout")
Rect = "da"
RED = (255,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
lead_x_change = 0
lead_x = 300
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #construct the parent component
        selfimage = pygame.image.load("red_ball.png").convert_alpha()
        self.image = pygame.transform.scale(selfimage, (10, 10))
        self.rect = self.image.get_rect() #loads the rect from the image

        #set the position, direction, and speed of the ball
        self.rect.left = random.randrange(0,setDisplay.get_width()-self.rect.width)
        self.rect.top = random.randrange(162,200)
        self.dir_x = random.choice([-1,1])
        self.dir_y = 1
        self.speed = 3


    def update(self, boolean):
        global score
        
        check = self.rect.move(self.speed*self.dir_x,0)
        for rect in rect_group:
            if rect.colliderect(check):
                self.dir_x*=-1
                break

        check2 = self.rect.move(0,self.speed*self.dir_y)
        for rect in rect_group:
            if rect.colliderect(check2):
                self.dir_y*=-1
                break

        check3 = self.rect.move(0,self.speed*self.dir_y)
        for wall in wall_group1:
            if wall.rect.colliderect(check3):
                wall_group1.remove(wall)
                self.dir_y*=-1
                self.speed = 6.2
                score+=1
                pickUpSound.play()
                break
            
        check5 = self.rect.move(0,self.speed*self.dir_y)
        for wall in wall_group2:
            if wall.rect.colliderect(check5):
                wall_group2.remove(wall)
                self.dir_y*=-1
                self.speed = 6
                score+=1
                pickUpSound.play()
                break

        check7 = self.rect.move(0,self.speed*self.dir_y)
        for wall in wall_group3:
            if wall.rect.colliderect(check7):
                wall_group3.remove(wall)
                self.dir_y*=-1
                self.speed = 4
                score+=1
                pickUpSound.play()
                break

        check9 = self.rect.move(0,self.speed*self.dir_y)
        for wall in wall_group4:
            if wall.rect.colliderect(check9):
                wall_group4.remove(wall)
                self.dir_y*=-1
                self.speed = 3
                score+=1
                pickUpSound.play()
                break
                    
        #Handle the walls by changing direction(s)
        if self.rect.left < 0 or self.rect.right >= setDisplay.get_width():
            self.dir_x *= -1
        if self.rect.top < 0:
            self.dir_y *= -1
            
        self.rect.move_ip(self.speed*self.dir_x, self.speed*self.dir_y)

    def checkdefeat(self):
        if self.rect.bottom >= setDisplay.get_height():
            setDisplay.fill(BLACK)
            text2 = Font2.render("GAME OVER",True, WHITE, BLACK)
            text3 = Font.render("Press 'space' to exit",True, WHITE, BLACK)
            text7 = Font.render("Score:"+repr(score),True, WHITE, BLACK)
            textRect2 = text2.get_rect()
            textRect3 = text3.get_rect()
            textRect7 = text7.get_rect()
            textRect2.center = setDisplay.get_rect().center
            textRect3.midbottom = setDisplay.get_rect().midbottom
            textRect7.midtop = setDisplay.get_rect().midtop
            setDisplay.blit(text2,textRect2)
            setDisplay.blit(text3,textRect3)
            setDisplay.blit(text7,textRect7)
            defeated = True
            if musicPlaying:
                pygame.mixer.music.stop()

    def checkvictory(self):
        if len(wall_group1) ==0 and len(wall_group2) == 0 and len(wall_group3)==0 and len(wall_group4) == 0:
            text5 = Font2.render("CONGRATS! YOU WON!",True, WHITE, BLACK)
            text6 = Font.render("Press 'space' to exit",True, WHITE, BLACK)
            textRect5 = text5.get_rect()
            textRect6 = text6.get_rect()
            textRect5.center = setDisplay.get_rect().center
            textRect6.midbottom = setDisplay.get_rect().midbottom
            setDisplay.blit(text5,textRect5)
            setDisplay.blit(text6,textRect6)
            win = True

    def adjust_speed(self, delta):
        self.speed += delta
        
class Wall(pygame.sprite.Sprite):
    def __init__(self, colour, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,20)).convert()
        self.image.fill(colour)
        self.rect = self.image.get_rect()

        #set the position of the block
        self.rect.left = x
        self.rect.top = y
        
ball_group = pygame.sprite.Group()
for i in range(1):
    ball = Ball()
    ball_group.add(ball)
    
Font = pygame.font.SysFont(None, 30)
Font2 = pygame.font.SysFont(None,72)

#Music
pickUpSound = pygame.mixer.Sound('pickup.wav')
pygame.mixer.music.load('background.mp3')
pygame.mixer.music.play(-1, 0.0)
musicPlaying = True

wall_group1 = pygame.sprite.Group()
wall1 = Wall((255, 0, 0), 1, 1)
wall_group1.add(wall1)
wall2 = Wall((255, 0, 0), 61, 1)
wall_group1.add(wall2)
wall3 = Wall((255, 0, 0), 121, 1)
wall_group1.add(wall3)
wall1 = Wall((255, 0, 0), 181, 1)
wall_group1.add(wall1)
wall2 = Wall((255, 0, 0), 241, 1)
wall_group1.add(wall2)
wall3 = Wall((255, 0, 0), 301, 1)
wall_group1.add(wall3)
wall1 = Wall((255, 0, 0), 361, 1)
wall_group1.add(wall1)
wall2 = Wall((255, 0, 0), 421, 1)
wall_group1.add(wall2)
wall3 = Wall((255, 0, 0), 481, 1)
wall_group1.add(wall3)
wall1 = Wall((255, 0, 0), 541, 1)
wall_group1.add(wall1)

wall_group2 = pygame.sprite.Group()
wall1 = Wall((255, 255, 0), 31, 40)
wall_group2.add(wall1)
wall2 = Wall((255, 255, 0), 91, 40)
wall_group2.add(wall2)
wall3 = Wall((255, 255, 0), 151, 40)
wall_group2.add(wall3)
wall1 = Wall((255, 255, 0), 211, 40)
wall_group2.add(wall1)
wall2 = Wall((255, 255, 0), 271, 40)
wall_group2.add(wall2)
wall3 = Wall((255, 255, 0), 331, 40)
wall_group2.add(wall3)
wall1 = Wall((255, 255, 0), 391, 40)
wall_group2.add(wall1)
wall2 = Wall((255, 255, 0), 451, 40)
wall_group2.add(wall2)
wall3 = Wall((255, 255, 0), 511, 40)
wall_group2.add(wall3)

wall_group3 = pygame.sprite.Group()
wall3 = Wall((70,205,67), 121, 79)
wall_group3.add(wall3)
wall1 = Wall((70,205,67), 181, 79)
wall_group3.add(wall1)
wall2 = Wall((70,205,67), 241, 79)
wall_group3.add(wall2)
wall3 = Wall((70,205,67), 301, 79)
wall_group3.add(wall3)
wall1 = Wall((70,205,67), 361, 79)
wall_group3.add(wall1)
wall2 = Wall((70,205,67), 421, 79)
wall_group3.add(wall2)

wall_group4 = pygame.sprite.Group()
wall3 = Wall((156, 217, 234), 151, 118)
wall_group4.add(wall3)
wall1 = Wall((156, 217, 234), 211, 118)
wall_group4.add(wall1)
wall2 = Wall((156, 217, 234), 271, 118)
wall_group4.add(wall2)
wall3 = Wall((156, 217, 234), 331, 118)
wall_group4.add(wall3)
wall3 = Wall((156, 217, 234), 391, 118)
wall_group4.add(wall3)

check = 0
check2 = 0
win = 0
score = 0
defeated = False
background = pygame.Surface(setDisplay.get_size()).convert()
background.fill((255, 255, 255))
setDisplay.blit(background, (0,0))
rect_group = []
right = True
left = True
while True:
    for event in pygame.event.get():
        print event
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == pygame.K_LEFT:
                if left:
                    lead_x_change = -10                  
            if event.key == pygame.K_RIGHT:
                if right:
                    lead_x_change = 10
            if event.key == pygame.K_SPACE:
                pygame.quit()
                sys.exit()
        if event.type == KEYUP:
            lead_x_change = 0
        

    ball_group.clear(setDisplay,background)
    lead_x+=lead_x_change
    ball_group.update(True)
    setDisplay.fill((0,0,0))
    ball_group.draw(setDisplay)
    Rect = pygame.draw.rect(setDisplay,RED,(lead_x,378,20,4))
    rect_group.append(Rect)
    
    for i in rect_group:
        if i!=Rect:
            rect_group.remove(i)
    wall_group1.clear(setDisplay, background)
    wall_group1.draw(setDisplay)
    wall_group2.clear(setDisplay, background)
    wall_group2.draw(setDisplay)
    wall_group3.clear(setDisplay, background)
    wall_group3.draw(setDisplay)
    wall_group4.clear(setDisplay, background)
    wall_group4.draw(setDisplay)
    text = Font.render("Score:"+repr(score),True, WHITE, BLACK)
    textRect = text.get_rect()
    textRect.bottomright = setDisplay.get_rect().bottomright
    setDisplay.blit(text,textRect)
    for ball in ball_group:
        ball.checkdefeat()
    for ball in ball_group:
        ball.checkvictory()
    clock.tick(30)
    pygame.display.flip()
