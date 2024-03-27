from prisoners_dilemma_functions import random_name, petty_crimes_list, medium_crimes_list, bad_crimes_list
import random
import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()
username = str(input("Pick a username: "))
sentence_a = 0
sentence_b = 0
random_int = random.randint(1, 2)
times_generated = random.randint(1, 20)
if times_generated < 5:
    crime = petty_crimes_list()
elif 10 > times_generated > 5:
    crime = medium_crimes_list
else:
    crime = bad_crimes_list

if random_int == 1:
    player_a = username
    player_b = random_name()
else:
    player_a = random_name()
    player_b = username
for n in range(1, times_generated):
    if player_a and player_b:
        sentence_a += 1
        sentence_b += 1
    elif player_a and not player_b:
        sentence_a += 3
    elif not player_a and player_b:
        sentence_b += 3
    else:
        continue
