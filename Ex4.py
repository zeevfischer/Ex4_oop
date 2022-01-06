import sys
from types import SimpleNamespace

import agent
import pokimon
from client import Client
import json
from pygame import gfxdraw
import pygame
from pygame import *
from classes import GraphAlgo, Location

PORT = 6666
# server host (default localhost 127.0.0.1)
HOST = '127.0.0.1'
client = Client()
client.start_connection(HOST, PORT)

####################
graph_json = client.get_graph() # this is the graph from the client
algo = GraphAlgo.GraphAlgo() # my algo that will hole the Graph and let me use it
algo.load_from_json(graph_json)
graph = algo.get_graph() # the Graph
####################

# this get me a list of all the pokimons
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

# this will use the function above and the Graph to deturmin the Edge each pokimon is on
def src_dest_pok():
    pokemons = getPOK()
    for pok in range(len(pokemons)):
        for E in graph:
            src = E.src
            dest = E.dest
            type_Edge = 0
            if (src > dest):
                type_Edge = -1
            if (src < dest):
                type_Edge = 1
            pos_src = graph.Nodes[src].pos
            pos_dest = graph.Nodes[dest].pos
            x1 = pos_src.x
            x2 = pos_dest.x
            y1 = pos_src.y
            y2 = pos_dest.y

            if pok.is_Edge(x1,y1,x2,y2,type_Edge) == True:
                pok.src = int(src)
                pok.dest = int(dest)

# this adds all the agents to the client
# agent 1 will go to the src of the first pokimon
# if there are more agents then pokimons then tha agent will go to the center og the Graph
# if there are more pokimons then agents the algorithem will take car of that
def agents():
    pokemons = getPOK()
    size = int(json.loads(client.get_info())["GameServer"]["agents"])
    for i in range(size):
        if pokemons[i] != None:
           client.add_agent("{\"id\":" + str(pokemons[i].src) + "}")
        else:
            id, cost = algo.centerPoint()
            client.add_agent("{\"id\":" + str(id) + "}")
agents()

def getagents():
    my_agents = client.get_agents()
    agents_obj = json.loads(my_agents)
    my_agents = []
    for a in agents_obj['Agents']:
        data = a['Agent']
        temp = str(data['pos'])
        loc = temp.split(',')
        tap = (float(loc[0]), float(loc[1]), float(loc[2]))
        pos = Location.Location(tap)
        my_agents.append(agent.agent(int(data['id']),float(data['value']),int(data['src'],int(data['dest']),float(data['speed']),pos)))

    return my_agents


"""
what i have:
    agents 
    list pokimon
    Graph 
    
what is left:
    print pokimon on grapg
    allocate agent to pokimon while printing it
"""
# if the agent is on a Node and not on the move its dest is -1 and only then can he be moved
def allocate_agent_to_pok():
    pokemons = getPOK()
    my_agents = getagents()
    best_agent_id = -1
    best_agent_location = -1
    for i in range(len(pokemons)):
        pok = pokemons[i]
        for j in range(len(my_agents)):
            agent = my_agents[i]
            if agent.dest == -1:
                





        for agent in agents:
            if agent.dest == -1:
                next_node = (agent.src - 1) % len(graph.Nodes)
                client.choose_next_edge(
                    '{"agent_id":' + str(agent.id) + ', "next_node_id":' + str(next_node) + '}')
                ttl = client.time_to_end()
                print(ttl, client.get_info())

        client.move()











client.start()