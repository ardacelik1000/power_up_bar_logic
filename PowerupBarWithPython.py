import pygame
import math

pygame.init()

Width = 1000 
Height = 800

Screen = pygame.display.set_mode([Width,Height])

fps = 60
Timer = pygame.time.Clock()
run = True 
PowerUpBarLineThickness = 5
BarSpeed = -0.01 
Angle = math.pi

#For Gravity Check
WallThickness = 10
Gravity = 0.5
BounceStop = 0.3 

cx, cy =  100, 100
radius = 100  #yaricap
start_angle = 0
color = ('white')

class Ball():
    #ball = Ball(Width/3,Height/3,40,'red',100,.7,0,0,0.02)
    def __init__(self, x_pos, y_pos, radius, color, mass, retention, y_speed, x_speed, friction): 
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.radius = radius
        self.color = color
        self.mass = mass
        self.retention = retention
        self.y_speed = y_speed
        self.x_speed = x_speed
        self.friction = friction
        self.selected = False

    def draw(self):
        self.circle = pygame.draw.circle(Screen,self.color,(self.x_pos,self.y_pos),self.radius)
    
    def GravityCheck(self):
        if self.y_pos < Height - self.radius - (WallThickness / 2):
                self.y_speed += Gravity
        else:
            if self.y_speed > BounceStop:
                    self.y_speed = self.y_speed * -1 * self.retention
            else:
               if abs(self.y_speed) <= BounceStop:
                    self.y_speed = 0
        
        return self.y_speed
    
    def UpdatePos(self): 
        self.y_pos += self.y_speed
        self.x_pos += self.x_speed
    


def PowerUpBar():
    end_angle = math.pi

    x = cx + radius * math.cos(Angle)
    y = cy - radius * math.sin(Angle)
    
    pygame.draw.arc(Screen, color, (cx - radius, cy - radius, radius*2, radius*2), start_angle, end_angle, PowerUpBarLineThickness)
    pygame.draw.line(Screen,'white',(cx,cy),(x,y),PowerUpBarLineThickness)
    

    pygame.draw.line(Screen,'green',(5,97),(15,97),PowerUpBarLineThickness)
    pygame.draw.line(Screen,'green',(13,60),(23,65),PowerUpBarLineThickness)
    pygame.draw.line(Screen,'green',(31,32),(41,41),PowerUpBarLineThickness)
    pygame.draw.line(Screen,'green',(65,9),(73,19),PowerUpBarLineThickness)
    pygame.draw.line(Screen,'yellow',(121,5),(117,16),PowerUpBarLineThickness)
    pygame.draw.line(Screen,'yellow',(160,26),(152,34),PowerUpBarLineThickness)
    pygame.draw.line(Screen,'red',(184,59),(173,66),PowerUpBarLineThickness)
    pygame.draw.line(Screen,'red',(194,98),(180,98),PowerUpBarLineThickness)

def UpdateAngle():
    # Angle is going to be the most important one to be able to detect the power of the ball in the game. 
    global Angle
    global BarSpeed
    Angle += BarSpeed
    if Angle<=0:
        BarSpeed *= -1
    if Angle == 3.141592653589793: 
        BarSpeed *= -1

ball = Ball(Width/3,Height/3,25,'purple',100,.7,0,0,0.02)
SavedAngle = 0 

while run:
    Timer.tick(fps)
    Screen.fill('black')
    UpdateAngle()
    PowerUpBar()
    MouseCoord = pygame.mouse.get_pos()

    ball.draw()
    ball.y_speed = ball.GravityCheck()
    ball.UpdatePos()

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            run = False
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_SPACE: 
                SavedAngle = Angle
    pygame.display.flip()

pygame.quit()