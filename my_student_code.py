"""
@author AchiyaZigi
OOP - Ex4
Very simple GUI example for python client to communicates with the server and "play the game!"
"""
import sys
from types import SimpleNamespace

import pokimon
from client import Client
import json
from pygame import gfxdraw
import pygame
from pygame import *
from classes import GraphAlgo, Location

# init pygame
WIDTH, HEIGHT = 1080, 720

# default port
PORT = 6666
# server host (default localhost 127.0.0.1)
HOST = '127.0.0.1'
pygame.init()

screen = display.set_mode((WIDTH, HEIGHT), depth=32, flags=RESIZABLE)
clock = pygame.time.Clock()
pygame.font.init()

client = Client()
client.start_connection(HOST, PORT)

def getPOK() -> list:
    pokemons = client.get_pokemons()
    pokemons_obj = json.loads(pokemons)
    pokemons = []
    for pok in pokemons_obj['Pokemons']:
        data = pok['Pokemon']
        temp = str(data['pos'])
        loc = temp.split(',')
        tap = (float(loc[0]), float(loc[1]), float(loc[2]))
        pos = Location.Location(tap)
        pokemons.append(pokimon.pokimon(data['value'],data['type'],pos))
    return pokemons

# pokemons = client.get_pokemons()
# pokemons_obj = json.loads(pokemons, object_hook=lambda d: SimpleNamespace(**d))
#
# print(pokemons)

graph_json = client.get_graph()

FONT = pygame.font.SysFont('Arial', 20, bold=True)
# load the json string into SimpleNamespace Object

graph_algo = GraphAlgo.GraphAlgo()
graph_algo.load_from_json(graph_json)
graph = graph_algo.get_graph()
# graph = json.loads(graph_json, object_hook=lambda json_dict: SimpleNamespace(**json_dict))

# for n in graph.Nodes.values():
#     loc = n.get_pos()
#     x = int(loc.x)
#     y = int(loc.y)
#     n.pos = SimpleNamespace(x=float(x), y=float(y))

 # get data proportions
# min_x = min(list(graph.Nodes), key=lambda n: n.pos.x).pos.x
# min_y = min(list(graph.Nodes), key=lambda n: n.pos.y).pos.y
# max_x = max(list(graph.Nodes), key=lambda n: n.pos.x).pos.x
# max_y = max(list(graph.Nodes), key=lambda n: n.pos.y).pos.y
min_x = sys.float_info.max
min_y = sys.float_info.max
max_x = 0
max_y = 0
for node in graph.Nodes.values():
    if float(node.pos.x) < float(min_x):
        min_x = node.pos.x

    if float(node.pos.x) > float(max_x):
        max_x = node.pos.x

    if float(node.pos.y) < float(min_y):
        min_y = node.pos.y

    if float(node.pos.y) > float(max_y):
        max_y = node.pos.y


def scale(data, min_screen, max_screen, min_data, max_data):
    """
    get the scaled data with proportions min_data, max_data
    relative to min and max screen dimentions
    """
    return ((float(data) - float(min_data)) / (float(max_data)-float(min_data))) * (max_screen - min_screen) + min_screen


# decorate scale with the correct values

def my_scale(data, x=False, y=False):
    if x:
        return scale(data, 50, screen.get_width() - 50, min_x, max_x)
    if y:
        return scale(data, 50, screen.get_height()-50, min_y, max_y)


radius = 15

client.add_agent("{\"id\":0}")
# client.add_agent("{\"id\":1}")
# client.add_agent("{\"id\":2}")
# client.add_agent("{\"id\":3}")

# this commnad starts the server - the game is running now
client.start()

"""
The code below should be improved significantly:
The GUI and the "algo" are mixed - refactoring using MVC design pattern is required.
"""

while client.is_running() == 'true':
    pokemons = getPOK()
    for p in pokemons:
        x = p.pos.x
        y = p.pos.y
        a1 = my_scale(float(x), x=True)
        a2 = my_scale(float(y), y=True)
        tap = (a1,a2,0)
        p.pos = Location.Location(tap)

    for p in pokemons:
        for E in graph.Edges.values():
            src = E.src
            dest = E.dest
            type_Edge = 0
            if(src>dest):
                type_Edge = -1
            if(src<dest):
                type_Edge = 1
            pos_src = graph.Nodes[src].pos
            pos_dest = graph.Nodes[dest].pos
            x1 = my_scale(pos_src.x , x=True)
            x2 = my_scale(pos_dest.x , x=True)
            y1 = my_scale(pos_src.y , y=True)
            y2 = my_scale(pos_dest.y , y=True)
            if p.is_Edge(x1,y1,x2,y2,type_Edge) == True:
                print("src = "+str(src)+" dest = "+str(dest))


    agents = json.loads(client.get_agents(),object_hook=lambda d: SimpleNamespace(**d)).Agents
    agents = [agent.Agent for agent in agents]
    for a in agents:
        x, y, _ = a.pos.split(',')
        a.pos = SimpleNamespace(x=my_scale(float(x), x=True), y=my_scale(float(y), y=True))
    # check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    # refresh surface
    screen.fill(Color(0, 0, 0))

    # draw nodes
    for n in graph.Nodes.values():
        x = my_scale(n.pos.x, x=True)
        y = my_scale(n.pos.y, y=True)

        # its just to get a nice antialiased circle
        gfxdraw.filled_circle(screen, int(x), int(y),
                              radius, Color(64, 80, 174))
        gfxdraw.aacircle(screen, int(x), int(y),
                         radius, Color(255, 255, 255))

        # draw the node id
        id_srf = FONT.render(str(n.id), True, Color(255, 255, 255))
        rect = id_srf.get_rect(center=(x, y))
        screen.blit(id_srf, rect)

    # draw edges
    for e in graph.Edges.values():
        # find the edge nodes
        src = graph.Nodes[e.src]
        dest = graph.Nodes[e.dest]

        # scaled positions
        src_x = my_scale(src.pos.x, x=True)
        src_y = my_scale(src.pos.y, y=True)
        dest_x = my_scale(dest.pos.x, x=True)
        dest_y = my_scale(dest.pos.y, y=True)

        # draw the line
        pygame.draw.line(screen, Color(61, 72, 126),
                         (src_x, src_y), (dest_x, dest_y))

    # draw agents
    for agent in agents:
        pygame.draw.circle(screen, Color(122, 61, 23),(int(agent.pos.x), int(agent.pos.y)), 10)
    # draw pokemons (note: should differ (GUI wise) between the up and the down pokemons (currently they are marked in the same way).
    for p in pokemons:
        pygame.draw.circle(screen, Color(0, 255, 255), (int(p.pos.x), int(p.pos.y)), 10)

    # update screen changes
    display.update()

    # refresh rate
    clock.tick(60)

    # choose next edge
    for agent in agents:
        if agent.dest == -1:
            next_node = (agent.src - 1) % len(graph.Nodes)
            client.choose_next_edge('{"agent_id":'+str(agent.id)+', "next_node_id":'+str(next_node)+'}')
            ttl = client.time_to_end()
            print(ttl, client.get_info())

    client.move()
# game over:
