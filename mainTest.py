import unittest
import pygame
from snake_game import Snake, Food, Game, WIDTH, HEIGHT, GRID_SIZE

class TestSnakeGame(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

    def tearDown(self):
        pygame.quit()

    def test_snake_movement(self):
        snake = Snake()
        initial_length = len(snake.body)

        snake.move()

        self.assertEqual(len(snake.body), initial_length - 1)

    def test_snake_growth(self):
        snake = Snake()
        initial_length = len(snake.body)

        snake.grow_snake()

        self.assertEqual(len(snake.body), initial_length + 1)

    def test_snake_wall_collision(self):
        snake = Snake()
        snake.body = [(0, 0)]
        snake.direction = (-1, 0)  # Move left

        snake.move()

        self.assertTrue(snake.check_boundaries())

    def test_food_generation(self):
        food = Food()

        self.assertTrue(0 <= food.position[0] < WIDTH // GRID_SIZE)
        self.assertTrue(0 <= food.position[1] < HEIGHT // GRID_SIZE)

    def test_food_collision(self):
        snake = Snake()
        food = Food()
        food.position = snake.body[0]

        snake.move()

        self.assertTrue(snake.grow)

    def test_food_not_on_snake(self):
        snake = Snake()
        food = Food()
        snake.body = [(1, 1), (1, 2)]
        food.position = (1, 1)

        self.assertNotIn(food.position, snake.body)

    def test_game_loop(self):
        game = Game()
        game.run()

if __name__ == "__main__":
    unittest.main()
