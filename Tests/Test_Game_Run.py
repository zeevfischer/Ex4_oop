import sys
import unittest

import Ex4
import client
from Ex4 import src_dest_pok
from classes.DiGraph import DiGraph
from classes.GraphAlgo import GraphAlgo
from classes.Location import Location
from pokemon import pokemon
import agent





class MyTestCase(unittest.TestCase):
    agent_dict = {"id": "0", "value": "0", "src": "0", "dest": "-1", "speed": "10", "pos": "1,1,1"}
    pos = Location((1, 1, 1))
    agent = agent('0', '0', '0', '-1', '10', pos)
    poke1 = pokemon("5.0", "-1", Location((2.5,2.5,0)))
    poke2 = pokemon("5.0", "1", Location((1.5, 1.5, 0)))
    poke3 = pokemon('5.0', '-1', Location((3.5,3.5,0)))
    poke_list = []
    poke_list.append(poke1)
    poke_list.append(poke2)
    poke_list.append(poke3)
    graph = DiGraph()
    graph.add_node(0, (0, 0, 0))
    graph.add_node(1, (1, 1, 1))
    graph.add_node(2, (2, 2, 2))
    graph.add_node(3, (3, 3, 3))
    graph.add_node(4, (4, 4, 4))
    graph.add_edge(0, 1, 1)
    graph.add_edge(1, 2, 1)
    graph.add_edge(2, 3, 1)
    graph.add_edge(3, 4, 1)
    algo = GraphAlgo(graph)

    def test_find_pok_edge(self):
        pokeList = [];
        for pok in self.poke_list:
            pokeList.append(src_dest_pok())
        edge = self.algo.graph.get_edge(1, 2)
        self.assertEqual(self.poke_list[1].edge.src, edge.src)
        self.assertEqual(self.poke_list[1].edge.dest, edge.dest)

    # def test_closest_pokemon(self):
    #     for pok in self.poke_list:
    #         Gui.find_pok_edge(pok, self.algo)
    #     Gui.closest_pokemon(self.agent, self.poke_list, self.algo)
    #     self.assertEqual(self.agent.pokemon, self.poke2)


if __name__ == '__main__':
    unittest.main()
