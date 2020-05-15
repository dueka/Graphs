from room import Room
from player import Player
from world import World
from stack import Stack
import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
tranversal_path = []
reversed_directions = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}
tranversal_graph = {}
visited = {}
# tranversal_graph.enqueue([player.current_room.id])

s = Stack()
prev_room = None
prev_point = None

while len(tranversal_graph) < len(room_graph):
    current_room = player.current_room.id

    if current_room not in tranversal_graph:
        # Set exits to a dictionary and assign the "exit : ? to direction and do a for loop inside the function"
        exits = {direction: '?' for direction in player.current_room.get_exits()}
        # set the value of transversal_graph to exits
        tranversal_graph[current_room] = exits

    if prev_room:
        # to check for the current_room, set the prev_room and prev_point
        tranversal_graph[prev_room][prev_point] = current_room
        # Get the reverse of the poin
        reverse_point = reversed_directions[prev_point]
        tranversal_graph[current_room][reverse_point] = prev_room
    prev_room = current_room

    next_room = False

    next_movement = False

    for exit_point, room in tranversal_graph[current_room].items():
        if room == '?':
            prev_point = exit_point
            s.push(exit_point)
            tranversal_path.append(exit_point)
            player.travel(exit_point)
            next_movement = True
            break

        if not next_movement:
            exit_point = reversed_directions[s.pop()]
            tranversal_path.append(exit_point)
            prev_point = exit_point
            player.travel(exit_point)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
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
