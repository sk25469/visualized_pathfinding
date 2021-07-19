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
        self.row = row        # Current row and col of the node
        self.col = col
        self.width = width
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

    # to represent the barrier in the grid, we will use a BLACK color
    def is_barrier(self):
        return self.color == BLACK

    # start node is defined with an ORANGE color
    def is_start(self):
        return self.color == ORANGE

    # end node is defined by PURPLE color
    def is_end(self):
        return self.color == TURQUOISE

    # to reset the color of current node
    def reset(self):
        return self.color == WHITE

    # Now all the methods to make a particular node the different states describes above
    def make_visited(self):
        self.color = RED

    def make_reachable(self):
        self.color = GREEN

    def make_barrier(self):
        self.color = BLACK

    def make_start(self):
        self.color = ORANGE

    def make_end(self):
        self.color = TURQUOISE

    # We will show the actual path from start to end with purple nodes
    def make_path(self):
        self.color = PURPLE

    # Method to draw the barriers on the grid of a particular color, on the window
    # win, at positions x and y from the top left corner
    def draw(self, win):
        pygame.draw.rect(
            win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbor(self, grid):
        pass

    # To compare the 2 nodes together we will define this method
    def __lt__(self, other):
        return False
