import unittest
from classes.DiGraph import *
from classes.GraphAlgo import *

from classes.GraphAlgo import GraphAlgo


class TestGraph(unittest.TestCase):
    def initGraph(self):
        self.graph = DiGraph()
        self.graph.add_node(1, (1, 1, 1))
        self.graph.add_node(2, (1, 2, 2))
        self.graph.add_node(3, (3, 3, 1))
        self.graph.add_node(4, (4, 4, 4))
        self.graph.add_edge(1, 2, 10)
        self.graph.add_edge(2, 3, 20)
        self.graph.add_edge(3, 4, 15)
        self.graph.add_edge(4, 1, 30)

    def test_Vsize(self):
        self.initGraph()
        self.assertEqual(self.graph.v_size(), 4)
        self.graph.remove_node(1)
        self.assertEqual(self.graph.v_size(), 3)
        self.graph.add_node(1, (1, 2, 3))
        self.assertEqual(self.graph.v_size(), 4)

    def test_Eszie(self):
        self.initGraph()
        self.assertEqual(self.graph.e_size(), 4)

    def test_getAll_V(self):
        self.initGraph()
        self.assertEqual(len(self.graph.get_all_v()), 4)
        for i in range(4):
            self.assertTrue(self.graph.get_all_v()[i+1] is not None)


    def test_all_in(self):
        self.initGraph()

        into1 = 4
        temp = self.graph.Nodes.get(1).into
        self.assertEqual(into1, temp[0])

        into2 = 1
        temp = self.graph.Nodes.get(2).into
        self.assertEqual(into2, temp[0])

        into3 = 2
        temp = self.graph.Nodes.get(3).into
        self.assertEqual(into3, temp[0])

        into4 = 3
        temp = self.graph.Nodes.get(4).into
        self.assertEqual(into4, temp[0])


    def test_all_out(self):

        self.initGraph()
        out1 = 2
        temp = self.graph.Nodes.get(1).out
        self.assertEqual(out1, temp[0])

        out2 = 3
        temp = self.graph.Nodes.get(2).out
        self.assertEqual(out2, temp[0])

        out3 = 4
        temp = self.graph.Nodes.get(3).out
        self.assertEqual(out3, temp[0])

        out4 = 1
        temp = self.graph.Nodes.get(4).out
        self.assertEqual(out4, temp[0])