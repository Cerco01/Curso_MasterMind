import os
import random
import readchar

POS_X = 0
POS_Y = 1
NUM_OF_MAP_OBJECTS = 1

obstacle_definition = """\
##             #####################     #########
      ###
      #######                                     
      #######                                     
#      #                                      ####
#                 ###                 ############
##              ####                          ####
              ##########                          
       ##                     #####               
       ###                     ########           
#                                                #
#                                                #
###                  #####                       #
######              #######                   ####
########           #######                     ###
########                                      ####
#######                                     ######
#######            ##                       ######
###                 ############        ##########
##             #####################     #########\
"""


my_position = [2, 0]
tail_length = 0
tail = []
map_objects = []
last_direction = ""

# Create obstacle map.
temp_map = obstacle_definition.split("\n")
MAP_WIDTH = max(len(row) for row in temp_map)
MAP_HEIGHT = len(temp_map)
obstacle_definition = []
for row in temp_map:
    padded_row = list(row.ljust(MAP_WIDTH))
    obstacle_definition.append(padded_row)





# Apple generation function.
def generate_map_objects():
    global map_objects, my_position, tail, NUM_OF_MAP_OBJECTS, MAP_WIDTH, MAP_HEIGHT, obstacle_definition

    # Attempts counter and limit for victory condition.
    max_attempts = 500
    attempts = 0
    while len(map_objects) < NUM_OF_MAP_OBJECTS:

        # Check limit and declare victory.
        if attempts > max_attempts:
            os.system("cls")
            print("¡¡¡FELICIDADES!!! HAS LLENADO EL MAPA Y GANADO EL JUEGO.")
            print(f"Puntuación final: {tail_length}")
            input("\nPulsa Enter para salir...")
            os._exit(0)

        new_obstacle_position = [random.randint(0, MAP_WIDTH - 1), random.randint(0, MAP_HEIGHT - 1)]

        # Check if the new position is available.
        if (new_obstacle_position not in map_objects and
            new_obstacle_position != my_position and
            new_obstacle_position not in tail and
            obstacle_definition[new_obstacle_position[POS_Y]][new_obstacle_position[POS_X]] != "#"):

            map_objects.append(new_obstacle_position)
            attempts = 0 # Reset attempts on successful generation.

        else:
            attempts += 1 # Increment if the generation attempt fails.




# Generate random objects on the map.
generate_map_objects()


# Main Loop
while True:

    # Draw Map
    print("Bienvenido al SNAKE de Axel: Busca las Manzanas (*) con tu Serpiente (@).\n+" + "-" * MAP_WIDTH * 2 + "+")

    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="") # Left Border

        for coordinate_x in range(MAP_WIDTH):
            char_to_draw = "  "
            object_in_cell = None

            # Draw Order.
            # 1. Obstacles.
            if obstacle_definition[coordinate_y][coordinate_x] == "#":
                char_to_draw = "##"

            # 2. Apple (*).
            for map_object in map_objects:
                if map_object[POS_X] == coordinate_x and map_object[POS_Y] == coordinate_y:
                    char_to_draw = " *"
                    object_in_cell = map_object

            # 3. Tail (o).
            for tail_piece in tail:
                if tail_piece[POS_X] == coordinate_x and tail_piece[POS_Y] == coordinate_y:
                    char_to_draw = " o"

            # 4. Head (@)
            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = " @"

            print(f"{char_to_draw}", end="")

        print("|") # Right Border

    print("+" + "-" * MAP_WIDTH * 2 + "+")
    print(f"Puntuación: {tail_length}")

    # ReadChar + Wrap-Around. (WASD input)
    direction = readchar.readchar()
    new_position = None
    is_opposite_move = False

    # Calculate potential new position (with wrap-around).
    if direction == "w":
        new_position = [my_position[POS_X], (my_position[POS_Y] - 1) % MAP_HEIGHT]

    elif direction == "s":
        new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_HEIGHT]

    elif direction == "a":
        new_position = [(my_position[POS_X] - 1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction == "d":
        new_position = [(my_position[POS_X] + 1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction == "q":
        break

    # Movement Restriction Logic: 180-degree turn only allowed when tail_length == 0.
    if new_position:
        if (direction == "w" and last_direction == "s") or \
           (direction == "s" and last_direction == "w") or \
           (direction == "a" and last_direction == "d") or \
           (direction == "d" and last_direction == "a"):
            is_opposite_move = True

    # Block movement if it's opposite AND the snake has a tail.
    if is_opposite_move and tail_length > 0:
        new_position = None # Movement is cancelled.

    # Final movement execution.
    if new_position:
        # Check for wall collision (Movement is blocked if obstacle is present).
        if obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":

            # Update last_direction only on a valid move.
            last_direction = direction

            # Move logic.
            tail.insert(0, my_position.copy())
            tail = tail[:tail_length]
            my_position = new_position

    # Apple consumption logic.
    if my_position in map_objects:
        map_objects.remove(my_position)
        tail_length += 1
        generate_map_objects()

    # Defeat Condition: Self-collision.
    if my_position in tail:
        os.system("cls")
        if my_position in tail:
            print("¡¡¡TE HAS ATROPELLADO!!!\n\n")

        input("Enter para reiniciar el juego...")

        # Reset game state.
        my_position = [2, 0]
        tail_length = 0
        tail = []
        map_objects = []
        last_direction = ""
        generate_map_objects()
        os.system("cls")
        continue

    os.system("cls")