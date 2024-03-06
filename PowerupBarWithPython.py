import pygame
import math
import time 

pygame.init()

Width = 1000 
Height = 800

Screen = pygame.display.set_mode([Width,Height])

fps = 60
Timer = pygame.time.Clock()
run = True 

#Thicknesses
PowerUpBarLineThickness = 5
BallDirectionThickness = 6
WallThickness = 10


#For The Bar
BarSpeed = -0.01 
Angle = math.pi
cx, cy =  100, 100
radius = 100  #yaricap
start_angle = 0

#For Gravity Check
Gravity = 0.5
BounceStop = 0.3 


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

    def draw(self):
        self.circle = pygame.draw.circle(Screen,self.color,(self.x_pos,self.y_pos),self.radius)
    
    def GravityCheck(self):
        if self.y_pos < Height - self.radius - (WallThickness / 2):
                self.y_speed += Gravity
        else:
                # If the speed of the ball is higher than certain amount of value, it's 0.3 for 'BounceStop', the ball goes to the opposite side when it touches to the surface.
            if self.y_speed > BounceStop:
                    self.y_speed = self.y_speed * -1 * self.retention
            # if the absolute of the value of speed is less than 0.3, it stops.
            else:
                if abs(self.y_speed) <= BounceStop:
                    self.y_speed = 0
        
        return self.y_speed
    
    def UpdatePos(self): 
        #We are updating the position of the ball by adding speed.
        self.y_pos += self.y_speed
        self.x_pos += self.x_speed
    
    def BallArrow(self,mouse): 
        #When you bring the mouse closer to the ball, it appears.
        if (self.x_pos-100 < mouse[0] <self.x_pos +100) and (self.y_pos-100 < mouse[1]):
            if (self.y_speed == 0 and self.x_speed == 0):
                pygame.draw.line(Screen,'white',(self.x_pos,self.y_pos),(mouse[0],mouse[1]),BallDirectionThickness)

    def SpaceKeyPressed(self):
        #it's planned that the power of hit and the angle will be detected under this function. 
        # To do 
        BallPower = 0.1/Angle
        PowerWithString = None
        

        if(BallPower< 0.03446383139834663):
            PowerWithString = 'Slow 0'
        if(0.03446383139834663<BallPower<=0.036878695576790556):
            PowerWithString = 'Slow 1'
        if(0.036878695576790556<BallPower<=0.041813140649139734):
            PowerWithString = 'Slow 3'
        if(0.041813140649139734<BallPower<=0.05021107093348202):
            PowerWithString = 'Slow 4'
        if(0.05021107093348202<BallPower<=0.0703436386981033):
            PowerWithString = 'Medium 0'
        if(0.0703436386981033<BallPower<=0.10850780939982202):
            PowerWithString = 'Medium 1'
        if(0.10850780939982202<BallPower<=0.2076443634565331):
            PowerWithString = 'Max 0'
        if(0.2076443634565331<BallPower<=0.5219406805340868):
            PowerWithString = 'Max 1'
        
        return PowerWithString


def PowerUpBar():
    end_angle = math.pi
    #radius and angle is equal to at the beginning 100 

    x = cx + radius * math.cos(Angle)
    y = cy - radius * math.sin(Angle)
    
    # Drawing the half circle for the bar and the line inside it.
    pygame.draw.arc(Screen, 'white', (cx - radius, cy - radius, radius*2, radius*2), start_angle, end_angle, PowerUpBarLineThickness)
    pygame.draw.line(Screen,'white',(cx,cy),(x,y),PowerUpBarLineThickness)
    
    #The small lines inside the bar
    pygame.draw.line(Screen,'green',(5,97),(15,97),PowerUpBarLineThickness)
    pygame.draw.line(Screen,'green',(13,60),(23,65),PowerUpBarLineThickness)
    pygame.draw.line(Screen,'green',(31,32),(41,41),PowerUpBarLineThickness)
    pygame.draw.line(Screen,'green',(65,9),(73,19),PowerUpBarLineThickness)
    pygame.draw.line(Screen,'yellow',(121,5),(117,16),PowerUpBarLineThickness)
    pygame.draw.line(Screen,'yellow',(160,26),(152,34),PowerUpBarLineThickness)
    pygame.draw.line(Screen,'red',(184,59),(173,66),PowerUpBarLineThickness)
    pygame.draw.line(Screen,'red',(194,98),(180,98),PowerUpBarLineThickness)

def UpdateBarAngle():
    # Bar Angle is going to be the most important one to be able to detect the power of the ball in the game. 
    global Angle
    global BarSpeed
    Angle += BarSpeed
    if Angle<=0:
        BarSpeed *= -1
    if Angle == 3.141592653589793: 
        BarSpeed *= -1

ball = Ball(Width/3,Height/3,25,'purple',100,.7,0,0,0.02)

while run:
    Timer.tick(fps)
    Screen.fill('black')

    #For the power bar
    UpdateBarAngle()
    PowerUpBar()

    #Getting the position of the mouse 
    MouseCoord = pygame.mouse.get_pos()
    #Drawing the ball, updating the position if the ball, calling 'gravity check' method from the Ball class, and drawing the arrow appears when the mouse is close to the ball
    ball.draw()
    ball.UpdatePos()
    ball.y_speed = ball.GravityCheck()
    ball.BallArrow(MouseCoord) 

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            run = False

    pygame.display.flip()

pygame.quit()