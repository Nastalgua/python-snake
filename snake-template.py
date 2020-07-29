import random
import pygame
import sys

# Global vars
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480

GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH / GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT / GRID_SIZE

FRAME_RATE = 10
FONT = 'refusal'

SNAKE_COLOR = (84, 140, 80)
FOOD_COLOR = (207, 121, 112)
TILE_ONE_COLOR = (93, 216, 140)
TILE_TWO_COLOR = (93, 198, 140)

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class Snake(object):
    # Set the following class attributes
    # Your teacher should explain the math and what these variables should represent.
    def __init__(self):
        # self.length = 
        # self.positions = 
        # self.direction = 
        # self.color = 
        # self.score = 
        pass
    
    # This function should return the current head position
    # Better be one line or you and I are going to have some problems
    def get_head_position(self):
        pass
    
    # This function manages the turning of the snake. 
    # Moving backwards is not allowed, unless the snake is one block.
    def turn(self, point):
        pass
    
    # This function is called to move the the snake.
    # Your teacher should tell you about the algorithm on how the next positon if calculated. If they can't, they're bad. I'm kidding.
    # This method should also have collision check with the snake itself so it can call commit_die()
    def move(self):
        pass
    
    # Resets the snake
    def commit_die(self):
        self.length = 1
        self.positions = [(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)]
        self.direction = random.choice([ UP, DOWN, LEFT, RIGHT ])
        self.score = 0

    # Ignore this, don't worry too much about this. Pygame shenanigans
    def draw(self, surface):
        for pos in self.positions:
            rect = pygame.Rect((pos[0], pos[1]), (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, self.color, rect)
            pygame.draw.rect(surface, TILE_ONE_COLOR, rect, 1)

    # Handles the key presses in the game
    def handle_keys(self):
        # Here are some things that can help:
        # pygame.event.get() returns a collection / array of events being fired
        # a event from pygame.event.get() has the .type variable which can be matched up with pygame.{ some_key }
        # Those are your hints. Lmao
        pass

class Food(object):
    # Set the class attributes (hint: you should call one of the functions in your class)
    def __init__(self):
        # self.color
        # { function class here }
        pass
    
    # Generate a random position. 
    def random_position(self):
        # Hint: use the random module. specifically the .randint()
        pass

    # Ignore this, don't worry too much about this. Pygame shenanigans
    def draw(self, surface):
        rect = pygame.Rect((self.position[0], self.position[1]), (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, self.color, rect)
        pygame.draw.rect(surface, (93, 216, 228), rect, 1)

# Helpers (Ignore)
def drawGrid(surface):
    for y in range(0, int(GRID_HEIGHT)):
        for x in range(0, int(GRID_WIDTH)):
            if (x + y) % 2 == 0: # Lighter squre
                rect = pygame.Rect((x * GRID_SIZE, y * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
                pygame.draw.rect(surface,TILE_ONE_COLOR, rect)
            else: # Darker square
                rect = pygame.Rect((x * GRID_SIZE, y * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
                pygame.draw.rect(surface, TILE_TWO_COLOR, rect)

# Part of it is written already. 
# In main() there are comments. Where there are comments, is where you should write code.
# Ignore the parts that don't have comments in main()
def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    drawGrid(surface)

    ### Create snake object and food object from the classes you dealt with earlier
    # { Code here }

    my_font = pygame.font.SysFont(FONT, 27)

    while True:
        clock.tick(FRAME_RATE)
        snake.handle_keys()
        drawGrid(surface)
        
        snake.move()

        ### Collision checking with snake and food
        # { Code here }
        
        snake.draw(surface)
        food.draw(surface)

        screen.blit(surface, (0,0))

        score_text = my_font.render("Score: {0}".format(snake.score), 1, (255, 255, 255))
        screen.blit(score_text, (5, 10))

        pygame.display.update()

main()