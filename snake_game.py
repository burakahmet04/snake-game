import pygame
import sys
import random

# Sabitler
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BLOCK_SIZE = 20

# Renkler
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


# Yılan ve yiyecek sınıfları
class Snake:
    def __init__(self):
        self.body = [(100, 100), (80, 100), (60, 100)]
        self.direction = (BLOCK_SIZE, 0)

    def move(self):
        head = (self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1])
        self.body.insert(0, head)
        self.body.pop()

    def grow(self):
        head = (self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1])
        self.body.insert(0, head)

    def change_direction(self, direction):
        self.direction = direction


class Food:
    def __init__(self):
        self.position = (random.randint(0, (SCREEN_WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
                         random.randint(0, (SCREEN_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE)

    def respawn(self):
        self.position = (random.randint(0, (SCREEN_WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
                         random.randint(0, (SCREEN_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE)


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake Game")

    snake = Snake()
    food = Food()

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != (0, BLOCK_SIZE):
                    snake.change_direction((0, -BLOCK_SIZE))
                if event.key == pygame.K_DOWN and snake.direction != (0, -BLOCK_SIZE):
                    snake.change_direction((0, BLOCK_SIZE))
                if event.key == pygame.K_LEFT and snake.direction != (BLOCK_SIZE, 0):
                    snake.change_direction((-BLOCK_SIZE, 0))
                if event.key == pygame.K_RIGHT and snake.direction != (-BLOCK_SIZE, 0):
                    snake.change_direction((BLOCK_SIZE, 0))

        snake.move()

        if snake.body[0] == food.position:
            snake.grow()
            food.respawn()

        if (snake.body[0][0] < 0 or snake.body[0][0] >= SCREEN_WIDTH or
                snake.body[0][1] < 0 or snake.body[0][1] >= SCREEN_HEIGHT or
                snake.body[0] in snake.body[1:]):
            break

        screen.fill(WHITE)

        for segment in snake.body:
            pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))

        pygame.draw.rect(screen, RED, pygame.Rect(food.position[0], food.position[1], BLOCK_SIZE, BLOCK_SIZE))

        pygame.display.flip()
        clock.tick(5)


if __name__ == "__main__":
    main()
    