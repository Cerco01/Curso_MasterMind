import os
import readchar

POS_X = 0
POS_Y = 1
MAP_WIDTH = 20
MAP_HEIGHT = 15

my_position = [6, 3]

while True:

    # Draw Map
    print("+" + "-" * MAP_WIDTH * 3 + "+")

    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")
        for coordinate_x in range(MAP_WIDTH):
            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                print(" @ ", end="")
            else:
               print("   ", end="")
        print("|")

    print("+" + "-" * MAP_WIDTH * 3 + "+")

    # Ask user where he wants to move.
    #direction = input("¿Dónde te quieres mover? [WASD]: ")
    direction = readchar.readchar()

    if direction == "w":
        my_position[POS_Y] -= 1
    elif direction == "s":
        my_position[POS_Y] += 1
    elif direction == "a":
        my_position[POS_X] -= 1
    elif direction == "d":
        my_position[POS_X] += 1
    elif direction == "q":
        break


    # Este es mi primer diseño de teletransporte entre límites del mapa. Mi maestra "Gemini me ha explicado que puedo
    # usar la fórmula del % módulo.
    """if my_position[POS_Y] > (MAP_HEIGHT - 1):
        my_position[POS_Y] = 0
    elif my_position[POS_Y] < 0:
        my_position[POS_Y] = MAP_HEIGHT - 1
    elif my_position[POS_X] < 0:
        my_position[POS_X] = MAP_WIDTH -1
    elif my_position[POS_X] > (MAP_WIDTH - 1):
        my_position[POS_X] = 0"""


    my_position[POS_Y] = my_position[POS_Y] % MAP_HEIGHT
    my_position[POS_X] = my_position[POS_X] % MAP_WIDTH



    os.system("cls")