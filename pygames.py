import random
import time
from pygame import *
init()

# Classes
# Bird Class
class Bird():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.img = image.load("bird.png")
        self.velocity = 0
        self.gravity = 0.5
    def blit(self):
       self.rect = screen.blit(self.img,(self.x,self.y))
    def jump(self):
        self.velocity = -10
    def move(self):
        self.velocity = self.velocity + self.gravity
        self.y = self.y + self.velocity
    def collides_with(self, pipe):
        return pipe.rect.colliderect(self.rect)
             

#Pipes Class
class Pipe():
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.rect = None
        # Get the correct pipe image
        up_img = image.load("pipe.png")
        if self.direction == "up":
            self.img = up_img
        else:
           self.img = transform.flip(up_img, 0, 1)

       
    def move(self):
        left_speed = 5
        self.x = self.x - left_speed
    def blit(self):
        self.rect = screen.blit(self.img, (self.x, self.y))

#SETUP
#pygame setup
screen = display.set_mode((800, 600))
background_image = image.load("bg.png")
Game_over = image.load("game_over.jpg")

#Set up the bird
bird = Bird(10,250)

#Set up the pipes
#pipes_info = [(300, 350, "up"), (600, -350, "down"), (800, 350, "up"), (900, -350, "down"), (1200, 350, "up")]
pipes_info = []
pipe_gap = 300
pipe_last_x = 0
n = 1000
for i in range(n):
    Pipe.x = pipe_last_x + pipe_gap
    UorD = random.choice(["up", "down"])
    Ycoord = random.randint(250, 500)
    if UorD == "down":
        Ycoord = Ycoord * -1
        
    pipe = (Pipe.x, Ycoord, UorD)
    pipes_info.append(pipe)
    pipe_last_x = Pipe.x
pipe_image = []
for x,y,direction in pipes_info:
    pipe_image.append(Pipe(x,y,direction))


#GAME TIME
game_mode = "waiting"

while True:
    screen.blit(background_image,(0,0))
    new_event = event.poll() 
    if game_mode == "waiting":
    #Waiting to play
        if new_event.type == KEYDOWN:
            print("Start game")

            game_mode = "playing"
    elif game_mode == "playing":
        bird.move()
        if new_event.type == KEYDOWN:
            bird.jump()
    # Moving Objects
        for pipe in pipe_image:
            pipe.move()

    elif game_mode == "game over":
     # Game over
        screen.blit(Game_over,(0,0))


    # Show the pics!
    bird.blit()
    for pipe in pipe_image:
        pipe.blit()
        if bird.collides_with(pipe):
            game_mode = "game over"
    display.update()