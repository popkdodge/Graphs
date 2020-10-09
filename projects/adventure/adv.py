from room import Room
from player import Player
from world import World

import random
from ast import literal_eval


from util import Stack
# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
#establishing Current Room from player model
backtracking = []
graph = {}
reverse = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}
visited = set()

def walk_maze():
    while len(visited) != len(room_graph):
        #check if current_room is already visited
        current_room = player.current_room.id
        if current_room not in visited:
            possible_exits = player.current_room.get_exits()
            exits = {}
            #saving possible path in the graph
            for exit in possible_exits:
                exits[exit] = "?"
            graph[current_room] = exits
            #add current standing room in to visited
            visited.add(player.current_room.id)
        # above will also give us a key value pair that we 
        # can accesst to look for room we havent visited
        # because we initally mark it as "?"
        if any(backtracking):
            # This will map out the route from current room to 
            # the previous room
            graph[current_room][backtracking[-1]] = previous_room
        direction_uncheck = []
        for key, value in graph[current_room].items():
            # we can do this because we store a key value
            # pair withing the graph
            if value == "?":
                direction_uncheck.append(key)
        
        if len(direction_uncheck) > 0:
            # Selecting a direction out of the stack
            #direction = direction_uncheck[0]
            #direction_uncheck[1:]
            direction = random.choice(direction_uncheck)
            # set a variable to to save the pointer of the 
            # current room
            previous_room = player.current_room.id
            # move the player to the next room
            player.travel(direction)
            # sent the current_room the player is in as the 
            # a variable to be access
            next_room = player.current_room.id
            # update the mapp with a direction from
            # previous room
            graph[previous_room][direction] = next_room
            # add the traversal_path
            traversal_path.append(direction)
            # regester the opposite path in case of
            # dead end to be able to backtrack
            backtracking.append(reverse[direction])
        
        else:
            if len(direction_uncheck) == 0:
                # move in the opposite_direction
                opposite_direction = backtracking[-1]
                # set previous room
                prev_room = player.current_room.id
                # move player
                player.travel(opposite_direction)
                # set next room
                next_room = player.current_room.id
                # set the key equal to the room in that direction
                graph[prev_room][direction] = next_room
                # remove from path
                backtracking.pop()
                # track the direction
                traversal_path.append(opposite_direction)
    return graph
print(graph)
walk_maze()
# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
