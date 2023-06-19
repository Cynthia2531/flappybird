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

#Set up the bird
bird = Bird(10,250)

#Set up the pipes
pipes_info = [(300, 350, "up"), (600, -350, "down"), (800, 350, "up"), (900, -350, "down"), (1200, 350, "up")]
pipe_image = []
for x,y,direction in pipes_info:
    pipe_image.append(Pipe(x,y,direction))


#GAME TIME
game_mode = "waiting"
game_mode = "playing"
game_mode = "game over"

while True:
    screen.blit(background_image,(0,0))
    #Waiting to play
    
    # Moving Objects
    for pipe in pipe_image:
        pipe.move()
    # Game over

    # Show the pics!
    bird.blit()
    for pipe in pipe_image:
        pipe.blit()
    display.update()
