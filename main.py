import pygame

# Setup - settings
pygame.init()
width = 700 # Szerokosc
height = 500 # Wysokosc
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()
FPS = 60 # Klatki na sekunde
white = (255, 255, 255)
black = (0, 0, 0)
paddle_width = 15
paddle_height = 100

shift = 10
paddle_left_x = 0 + shift # Zero jako wartość początkowa
paddle_right_x = width - paddle_width - shift
paddle_y = (height >> 1) - (paddle_height >> 1)


class Paddle:
    paddle_color = white
    paddle_velocity = 4

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, scr):
        pygame.draw.rect(scr, self.paddle_color, (self.x, self.y, self.width, self.height))

    def move(self, down: bool):
        if down:
            self.y += self.paddle_velocity
        else:
            self.y -= self.paddle_velocity


def draw(scr, paddles):
    scr.fill(black)

    for paddle in paddles:
        paddle.draw(scr)

    pygame.display.update()

def paddle_keys_movement(keys, paddle_left, paddle_right):
    border_left_top = paddle_left.y - paddle_left.paddle_velocity >= 0
    border_left_bottom = paddle_left.y + paddle_left.paddle_velocity + paddle_left.height <= height
    border_right_top = paddle_right.y - paddle_right.paddle_velocity >= 0
    border_right_bottom = paddle_right.y - paddle_right.paddle_velocity + paddle_right.height<= height
    # User LEFT
    if keys[pygame.K_w] and border_left_top :
        paddle_left.move(down = False)
    if keys[pygame.K_s] and border_left_bottom:
        paddle_left.move(down = True)
    # User Right
    if keys[pygame.K_UP] and border_right_top:
        paddle_right.move(down = False)
    if keys[pygame.K_DOWN] and border_right_bottom:
        paddle_right.move(down = True)


def main():
    running = True

    paddle_left = Paddle(paddle_left_x, paddle_y, paddle_width, paddle_height)
    paddle_right = Paddle(paddle_right_x, paddle_y, paddle_width, paddle_height)
    paddles = [paddle_left, paddle_right]

    while running:
        clock.tick(FPS)
        draw(screen, paddles)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break


        keys = pygame.key.get_pressed()
        paddle_keys_movement(keys, paddle_left, paddle_right)

    pygame.quit()

if __name__ == "__main__":
    main()