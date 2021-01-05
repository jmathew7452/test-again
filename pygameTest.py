import pygame
import random
pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red   = (255, 0, 0)

dis = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Snake game')

game_over = False

x1 = 300
y1 = 300

red_x = 200
red_y = 200

x1_change = 0
y1_change = 0

tail_counter = 0
tail_x = 0
tail_y = 0
tail_trail_x = [0] * 300
tail_trail_y = [0] * 300
hold_tail = False
tail_trail = 0


clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
                hold_tail = False
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
                hold_tail = False
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -10
                hold_tail = False
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 10
                hold_tail = False
        if event.type == pygame.KEYUP:
                x1_change = 0
                y1_change = 0
                hold_tail = True

    if(x1 == 0 and x1_change == -10):
        x1_change = 0
    if(x1 == 390 and x1_change == 10):
        x1_change = 0
    if(y1 == 0 and y1_change == -10):
        y1_change = 0
    if(y1 == 390 and y1_change == 10):
        y1_change = 0

    x1 += x1_change
    y1 += y1_change

    if(x1 <= (red_x + 11) and x1 >= (red_x - 11)):
        if(y1 <= (red_y + 11) and y1 >= (red_y - 11)):
            red_x = random.randint(10, 380)
            red_y = random.randint(10, 380)
            tail_counter+=1
            print(tail_counter)


    if(hold_tail == False):
        t = tail_counter
        if(t > 0):
            while(t > 0):
                tail_trail_x[t] = tail_trail_x[t-1]
                tail_trail_y[t] = tail_trail_y[t-1]
                t = t - 1
        tail_trail_x[0] = tail_x
        tail_trail_y[0] = tail_y
        tail_x = (x1 - x1_change)
        tail_y = (y1 - y1_change)


    dis.fill(white)
    pygame.draw.rect(dis, black, [x1, y1, 10, 10])
    pygame.draw.rect(dis, red, [red_x, red_y, 10, 10])

    for z in range(tail_counter):
        if(x1 == tail_trail_x[z] and y1 == tail_trail_y[z]):
            pygame.quit()
            print("Game Over")

    if(x1 == tail_x and y1 == tail_y and tail_counter >= 1):
        pygame.quit()
        print("Game Over")

    if(tail_counter >= 1):
        tail_creator()
    def tail_creator():
        pygame.draw.rect(dis, black, [tail_x, tail_y, 10, 10])
        for y in range(tail_counter-1):
            pygame.draw.rect(dis, black, [tail_trail_x[y], tail_trail_y[y], 10, 10])

    pygame.display.update()
    clock.tick(30)

pygame.quit()
quit()

#pygame testing
#hi github!
#test again
#testing branch