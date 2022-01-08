import json
import sys
import client
import pygame
from pygame.constants import RESIZABLE
import pygame.gfxdraw
# from classes.GraphAlgo import GraphAlgo
import math
from tkinter import *

pygame.font.init()
clock = pygame.time.Clock()
FONT = pygame.font.SysFont('comicsans', 20)
screen = pygame.display.set_mode((1300, 750), depth=32, flags=RESIZABLE)
# screen.fill((255, 255, 255))
######################
ball = pygame.image.load('GUIdata/ball.png')
ball = pygame.transform.scale(ball,(25,25))
backrond = pygame.image.load('GUIdata/b1.jpg')
# backrond = pygame.image.load('GUIdata/b2.png')
backrond = pygame.transform.scale(backrond,(screen.get_width(),screen.get_height()))
up_pokemon = pygame.image.load('GUIdata/charmander.png')
up_pokemon = pygame.transform.scale(up_pokemon,(35,35))
down_pokemon = pygame.image.load('GUIdata/pika.png')
down_pokemon = pygame.transform.scale(down_pokemon,(35,35))
agent =  pygame.image.load('GUIdata/agent2.png')
agent = pygame.transform.scale(agent,(35,35))
######################


def scale(data: int, min_screen, max_screen, min_data, max_data):
    """
    get the scaled data with proportions min_data, max_data
    relative to min and max screen dimensions
    """
    return ((float(data) - float(min_data)) / (float(max_data) - float(min_data))) * (
            float(max_screen) - float(min_screen)) + float(min_screen)

min_x = sys.float_info.max
min_y = sys.float_info.max
max_x = 0
max_y = 0

def min_max(graph):
    global min_x, min_y, max_x, max_y
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

class Button:
    def __init__(self, rect: pygame.Rect, color: tuple = (0, 0, 0)):
        self.rect = rect
        self.color = color
        self.pressed = False

    def press(self):
        self.pressed = not self.pressed

class Gui:
    pygame.font.init()
    clock = pygame.time.Clock()
    FONT = pygame.font.SysFont('comicsans', 20)


    def __init__(self, algo = None,client: client = None):
        self.client = client
        self.algo = algo
        min_max(algo.graph)
        self.button1 = Button(pygame.Rect(0, 0, 70, 40), (200, 200, 200))
        self.list_of_algo = []

    def arrow(self, start, end, d, h, color):
        dx = (end[0] - start[0])
        dy = (end[1] - start[1])
        D = (math.sqrt(dx * dx + dy * dy))
        xm = (D - d)
        xn = (xm)
        ym = (h)
        yn = -h
        sin = dy / D
        cos = dx / D
        x = xm * cos - ym * sin + start[0]
        ym = xm * sin + ym * cos + start[1]
        xm = x
        x = xn * cos - yn * sin + start[0]
        yn = xn * sin + yn * cos + start[1]
        xn = x
        points = [(end[0], end[1]), (int(xm), int(ym)), (int(xn), int(yn))]

        pygame.draw.line(screen, color, start, end, width=4)
        pygame.draw.polygon(screen, color, points)

    def my_scale(self, data, x=False, y=False):
        if x:
            return scale(data, 50, screen.get_width() - 50, min_x, max_x)
        if y:
            return scale(data, 50, screen.get_height() - 50, min_y, max_y)

    def draw(self):
        if self.client.is_running():
            # this prints the Nodes and the Edges
            for edge in self.algo.graph.Edges.values():
                src = edge.src
                dest = edge.dest
                w = edge.weight
                src_x = self.my_scale(self.algo.graph.Nodes.get(src).pos.x, x=True)
                src_y = self.my_scale(self.algo.graph.Nodes.get(src).pos.y, y=True)
                dest_x = self.my_scale(self.algo.graph.Nodes.get(dest).pos.x, x=True)
                dest_y = self.my_scale(self.algo.graph.Nodes.get(dest).pos.y, y=True)

                Gui.arrow(self, (src_x, src_y), (dest_x, dest_y), 25, 6, color=(63, 97, 235))

                # FONT = pygame.font.SysFont('comicsans', 10)
                # text_surface = FONT.render(str(round(w, 2)), True, (0, 0, 0))
                # screen.blit(text_surface, ((src_x * 0.25 + dest_x * 0.75), (src_y * 0.25 + dest_y * 0.75)))

            for src in self.algo.graph.Nodes.values():
                x = self.my_scale(src.pos.x, x=True)
                y = self.my_scale(src.pos.y, y=True)
                FONT = pygame.font.SysFont('comicsans', 13)
                screen.blit(ball,(x-12,y-12))
                node_text = FONT.render(str(src.id), True, (0, 0, 0))
                screen.blit(node_text, (x - 12, y - 20))

            FONT = pygame.font.SysFont('comicsans', 20)
            # button activation here i set all the buttons on the graph
            # here you can also see what each button dose acording to its string
            pygame.draw.rect(screen, self.button1.color, self.button1.rect)
            button_text = FONT.render("stop", True, (0, 0, 0))
            screen.blit(button_text, (self.button1.rect.x + 10, self.button1.rect.y + 5))

            #this will draw the info needed in this project
            info = pygame.Rect(80, 0, 130, 40)
            pygame.draw.rect(screen,(200, 200, 200),info)
            data = json.loads(self.client.get_info())["GameServer"]
            info_text = FONT.render('moves = ' + str(data['moves']), True, (0, 0, 0))
            screen.blit(info_text, (info.x + 10, info.y + 5))

            info = pygame.Rect(220, 0, 130, 40)
            pygame.draw.rect(screen, (200, 200, 200), info)
            if self.client.is_running:
                data = json.loads(self.client.get_info())["GameServer"]
            info_text = FONT.render('grade = ' + str(data['grade']), True, (0, 0, 0))
            screen.blit(info_text, (info.x + 10, info.y + 5))

            info = pygame.Rect(360, 0, 150, 40)
            pygame.draw.rect(screen, (200, 200, 200), info)
            info_text = FONT.render('time left = ' + str(int(float(self.client.time_to_end()) / 1000)), True, (0, 0, 0))
            screen.blit(info_text, (info.x + 10, info.y + 5))

    def draw_agent(self):
        my_agents = self.client.get_agents()
        agents_obj = json.loads(my_agents)
        for a in agents_obj['Agents']:
            data = a['Agent']
            temp = str(data['pos'])
            loc = temp.split(',')
            x = self.my_scale(float(loc[0]), x=True)
            y = self.my_scale(float(loc[1]), y=True)
            radius = 10
            pygame.draw.circle(screen, color=(160, 220, 0), center=(x, y), radius=radius)
            screen.blit(agent, (x-12, y-12))

    def draw_pokimon(self):
        pokemons = self.client.get_pokemons()
        pokemons_obj = json.loads(pokemons)
        for pok in pokemons_obj['Pokemons']:
            data = pok['Pokemon']
            temp = str(data['pos'])
            loc = temp.split(',')

            x = self.my_scale(float(loc[0]), x=True)
            y = self.my_scale(float(loc[1]), y=True)
            if int(data['type']) < 0:
                screen.blit(up_pokemon,(x-12,y-12))

                FONT = pygame.font.SysFont('comicsans', 13)
                node_text = FONT.render(str(data['value']), True, (0, 0, 0))
                screen.blit(node_text, (x - 12, y - 20))

            if int(data['type']) >= 0:
                screen.blit(down_pokemon,(x-12,y-12))

                FONT = pygame.font.SysFont('comicsans', 13)
                node_text = FONT.render(str(data['value']), True, (0, 0, 0))
                screen.blit(node_text, (x - 12, y - 20))

    def on_click(self, event):
            if event == "button1":
                self.client.stop_connection()
                sys.exit()

    def play(self):
        if self.client.is_running():
            global backrond
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # button one action
                    if self.button1.rect.collidepoint(event.pos):
                        self.button1.press()
                        if self.button1.pressed:
                            self.on_click("button1")
                        else:
                            self.list_of_algo.clear()
            pygame.display.set_mode((screen.get_width(), screen.get_height()), depth=32, flags=RESIZABLE)
            backrond = pygame.transform.scale(backrond, (screen.get_width(), screen.get_height()))
            screen.blit(backrond, [0,0])
            self.draw()
            self.draw_agent()
            self.draw_pokimon()
            pygame.display.update()
        else:
            sys.exit()

# if __name__ == '__main__':
#     a=GraphAlgo()
#     a.load_from_json("../data/A1.json")
#     Gui(a)
