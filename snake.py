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
    def __init__(self):
        self.length = 1
        self.positions = [(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)]
        self.direction = random.choice([ UP, DOWN, LEFT, RIGHT ])
        self.color = SNAKE_COLOR
        self.score = 0
        pass
    
    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction: # Prevent users from going backwards
            return
        else:
            self.direction = point
    
    def move(self):
        head_pos = self.get_head_position()
        x, y = self.direction

        # Takes the snake vector, multiply with GRID_SIZE, and adds to the player position
        # Modulo is used in order to allow the snake to wrap around.
        new_coords = ( 
            (head_pos[0] + (x * GRID_SIZE)) % SCREEN_WIDTH, 
            (head_pos[1] + (y * GRID_SIZE)) % SCREEN_HEIGHT 
        )

        if len(self.positions) > 2 and new_coords in self.positions[2:]:
            self.commit_die()
        else:
            self.positions.insert(0, new_coords)
            
            # This prevents the snake from lengthening it's body it did not eat the food in the move() call
            # This also gets rid of the last piece of the snake when it moves 
            if len(self.positions) > self.length:
                self.positions.pop()

    def commit_die(self):
        self.length = 1
        self.positions = [(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)]
        self.direction = random.choice([ UP, DOWN, LEFT, RIGHT ])
        self.score = 0

    def draw(self, surface):
        for pos in self.positions:
            rect = pygame.Rect((pos[0], pos[1]), (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, self.color, rect)
            pygame.draw.rect(surface, TILE_ONE_COLOR, rect, 1)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.turn(UP)
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.turn(DOWN)
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.turn(LEFT)
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.turn(RIGHT)

class Food(object):
    def __init__(self):
        self.random_position()
        self.color = FOOD_COLOR

    def random_position(self):
        # Without the minus one, the food can spawn outside of the game window, which means a impossible level
        self.position = (random.randint(0, GRID_WIDTH - 1) * GRID_SIZE, random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE)

    def draw(self, surface):
        rect = pygame.Rect((self.position[0], self.position[1]), (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, self.color, rect)
        pygame.draw.rect(surface, (93, 216, 228), rect, 1)

# Helpers
def drawGrid(surface):
    for y in range(0, int(GRID_HEIGHT)):
        for x in range(0, int(GRID_WIDTH)):
            if (x + y) % 2 == 0: # Lighter squre
                rect = pygame.Rect((x * GRID_SIZE, y * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
                pygame.draw.rect(surface,TILE_ONE_COLOR, rect)
            else: # Darker square
                rect = pygame.Rect((x * GRID_SIZE, y * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
                pygame.draw.rect(surface, TILE_TWO_COLOR, rect)

def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    drawGrid(surface)

    # Object initaliziation
    snake = Snake()
    food = Food()

    my_font = pygame.font.SysFont(FONT, 27)

    # Game loop
    while True:
        clock.tick(FRAME_RATE)
        snake.handle_keys()
        drawGrid(surface)
        
        snake.move()

        if snake.get_head_position() == food.position:
            snake.length += 1
            snake.score += 1
            food.random_position()
        
        snake.draw(surface)
        food.draw(surface)

        screen.blit(surface, (0,0))

        score_text = my_font.render("Score: {0}".format(snake.score), 1, (255, 255, 255))
        screen.blit(score_text, (5, 10))

        pygame.display.update()

main()