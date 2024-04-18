import pygame
import random

WIDTH, HEIGHT = 800, 600
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
FPS = 10

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class Snake:
    def __init__(self):
        self.body = [(WIDTH // 2, HEIGHT // 2)]  # Initialize with a single segment
        self.direction = RIGHT
        self.grow = False

    def move(self):
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

        new_head = (self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1])
        self.body.insert(0, new_head)

    def grow_snake(self):
        self.grow = True

    def draw(self, surface):
        for segment in self.body:
            pygame.draw.rect(surface, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    def check_collision(self):
        # Check if snake collides with itself
        return len(self.body) != len(set(self.body))

    def check_boundaries(self):
        # Check if snake is out of bounds
        head_x, head_y = self.body[0]
        return head_x < 0 or head_x >= GRID_WIDTH or head_y < 0 or head_y >= GRID_HEIGHT

class Food:
    def __init__(self):
        self.position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

    def draw(self, surface):
        pygame.draw.rect(surface, RED, (self.position[0] * GRID_SIZE, self.position[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.font = pygame.font.SysFont(None, 40)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.snake.direction != DOWN:
                    self.snake.direction = UP
                elif event.key == pygame.K_DOWN and self.snake.direction != UP:
                    self.snake.direction = DOWN
                elif event.key == pygame.K_LEFT and self.snake.direction != RIGHT:
                    self.snake.direction = LEFT
                elif event.key == pygame.K_RIGHT and self.snake.direction != LEFT:
                    self.snake.direction = RIGHT

    def update(self):
        self.snake.move()

        # Check collision with food
        if self.snake.body[0] == self.food.position:
            self.snake.grow_snake()
            self.food = Food()
            self.score += 1

        # Check collision with boundaries or itself
        if self.snake.check_collision() or self.snake.check_boundaries():
            pygame.quit()
            quit()

    def draw(self):
        self.screen.fill(BLACK)
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        self.draw_score()
        pygame.display.flip()

    def draw_score(self):
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))
    def run(self):
        running = True
        while running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

if __name__ == "__main__":
    game = Game()
    game.run()
