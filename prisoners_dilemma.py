from prisoners_dilemma_functions import random_name
import random
username = str(input("Pick a username: "))
sentence_a = 0
sentence_b = 0
random_int = random.randint(1, 2)
times_generated = random.randint(1,20)
if times_generated < 5:
    petty_crimes_list
elif 10 > times_generated > 5:
    medium_crimes_list
else:
    bad_crimes_list

if random_int == 1:
    player_a = username
    player_b = random_name()
else:
    player_a = random_name()
    player_b = username
for n in range(1, times_generated):
    if player_a == True and player_b == True:
        sentence_a += 1
        sentence_b += 1
    elif player_a == True and player_b == False:
        player_a += 3
    elif player_a == False and player_b == True:
        player_b += 3
    else:
        continue
