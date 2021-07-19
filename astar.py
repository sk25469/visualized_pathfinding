import pygame
import math
from queue import PriorityQueue

WIDTH = 700
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

    # Method to draw on rectangle on the grid of a particular color, on the window
    # win, then we give the rectangle to draw x,y co-ordinate as well as width and height
    # in our case, width is same as height

    def draw(self, win):
        pygame.draw.rect(
            win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbor(self, grid):
        pass

    # To compare the 2 nodes together we will define this method
    def __lt__(self, other):
        return False

# A* algorithm uses a heuristic function apart from normal edge distances, and this is how
# it is better than dijsktra, so heuristic function can be thought as the actual distance between
# the x and y co-ordinates of the nodes, hence we calculate the sum of actual distance and the
# sum of edge distance to calculate which value to pop from the priority queue


# Here we will call this heuristic distance absolute_dist, but actually we will be using
# abs(x1 - x2) + abs(y1 - y2), we call this the manhattan distance

def absolute_dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

# We need to make a grid, for that we will make a list of rows number of lists and for each
# we will append the nodes


def make_grid(rows, width):
    grid = []
    # This will be the gap between each of the columns, or the length of each cube
    # width is the length of the whole window, hence we do integer division
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, rows)
            grid[i].append(node)

    return grid

# Now we will draw the actual grid, instead of drawing individual cubes, we can draw
# vertical and horizontal lines


def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        # This draws the horizontal lines in the win window of the color GREY, the two arguments
        # in the functions are the (start point), (end point)
        #     (start_x, start_y), (end_x, end_y)
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))


# This function draws the different colors on the window and tell the pygame to update
# the screen when something new is drawn

def draw(win, grid, rows, width):

    # First we will fill the screen with white
    win.fill(WHITE)

    # Now we will draw the nodes of their own specific colors in the entire grid
    for row in grid:
        for node in row:
            node.draw(win)

    # the order is important here,
    # 1. The screen is filled with WHITE
    # 2. all the nodes are drawn with particular colors
    # 3. now we will draw grid line on top of those nodes
    draw_grid(win, rows, width)

    # Now we will update the screen
    pygame.display.update()
