import pygame
import math
from queue import PriorityQueue

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Path Finding Algorithm")


# Different color codes of the nodes in the grid
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

# We will define a class for every single node, or cubes in the grid

# Every cube will keep track of its
# 1. x and y co-ordinate
# 2. Track its color, as colors are important and we move our algorithm by figuring
#    if we reached the end node
# We keep the absolute x and y value, as we need a absolute distance in case of A*


class Node:
    def __init(self, row, col, width, total_row):
        self.row = row
        self.col = col
        self.x = row * width  # This way we calculate the absoulute co-ordinate
        self.y = col * width
        self.color = WHITE    # Initially all the nodes are white
        self.neighbor = []    # Keep track of all the neighbor of the current node
        self.total_row = total_row

    # returns the present co-ordinates of the current node
    def get_node(self):
        return self.row, self.col

    # to check if we already visited the current node
    # As said earlier, we will check if it is visited if the color is RED
    def is_visited(self):
        return self.color == RED

    # to check the nodes which are reachable from the current node
    # We represent these nodes by GREEN
    def is_reachable(self):
        return self.color == GREEN
