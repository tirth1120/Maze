import pygame
import time
import random

WIDTH = 450
HEIGHT = 450
FPS = 40

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Linkedin: tirth1120")
clock = pygame.time.Clock()

black = (0, 0, 0)
GREEN = (180,255,100)
lime = (180,255,100)
YELLOW = (0, 215, 0, 255)

x = 0                   
y = 0                   
w = 20

Box = []
visited = []
stack = []
dicct = {}

def cell(x, y, w):
    for i in range(1,21):
        x = 20                                                            
        y = y + 20                                                        
        for j in range(1, 21):
            pygame.draw.line(screen, black, [x, y], [x + w, y])           
            pygame.draw.line(screen, black, [x + w, y], [x + w, y + w])   
            pygame.draw.line(screen, black, [x + w, y + w], [x, y + w])   
            pygame.draw.line(screen, black, [x, y + w], [x, y])           
            Box.append((x,y))                                            
            x = x + 20                                                    


def up(x, y):
    pygame.draw.rect(screen, lime, (x + 1, y - w + 1, 19, 39), 0)         
    pygame.display.update()                                              


def down(x, y):
    pygame.draw.rect(screen, lime, (x +  1, y + 1, 19, 39), 0)
    pygame.display.update()

def right(x, y):
    pygame.draw.rect(screen, lime, (x +1, y +1, 39, 19), 0)
    pygame.display.update()

def left(x, y):
    pygame.draw.rect(screen, lime, (x - w +1, y +1, 39, 19), 0)
    pygame.display.update()

def cell1( x, y):
    pygame.draw.rect(screen, GREEN, (x +1, y +1, 18, 18), 0)          
    pygame.display.update()


def backtracking(x, y):
    pygame.draw.rect(screen, lime, (x +1, y +1, 18, 18), 0)        
    pygame.display.update()                                       


def sol(x,y):
    pygame.draw.rect(screen, YELLOW, (x+4, y+4, 8, 8), 0)           
    pygame.display.update()                                   


def puzzel(x,y):
    cell1(x, y)                                   
    stack.append((x,y))                                           
    visited.append((x,y))                                         
    while len(stack) > 0:                                         
        time.sleep(.01)                                            
        cell = []                                                 
        if (x + w, y) not in visited and (x + w, y) in Box:      
            cell.append("right")                                   

        if (x - w, y) not in visited and (x - w, y) in Box:      
            cell.append("left")

        if (x , y + w) not in visited and (x , y + w) in Box:   
            cell.append("down")

        if (x, y - w) not in visited and (x , y - w) in Box:     
            cell.append("up")

        if len(cell) > 0:                                         
            cell_chosen = (random.choice(cell))                    

            if cell_chosen == "right":                            
                right(x, y)                                   
                dicct[(x + w, y)] = x, y                        
                x = x + w                                          
                visited.append((x, y))                              
                stack.append((x, y))                                

            elif cell_chosen == "left":
                left(x, y)
                dicct[(x - w, y)] = x, y
                x = x - w
                visited.append((x, y))
                stack.append((x, y))

            elif cell_chosen == "down":
                down(x, y)
                dicct[(x , y + w)] = x, y
                y = y + w
                visited.append((x, y))
                stack.append((x, y))

            elif cell_chosen == "up":
                up(x, y)
                dicct[(x , y - w)] = x, y
                y = y - w
                visited.append((x, y))
                stack.append((x, y))
        else:
            x, y = stack.pop()                                    
            cell1(x, y)                                     
            time.sleep(.02)                                       
            backtracking(x, y)                               


def plot_route_back(x,y):
    sol(x, y)                                          
    while (x, y) != (25,25):                                     
        x, y = dicct[x, y]                                    
        sol(x, y)                                      
        time.sleep(.1)


x, y = 20, 20                     
cell(40, 0, 20)             
puzzel(x,y)              
plot_route_back(400, 400)         


running = True
while running:

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False