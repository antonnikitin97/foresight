import pygame
from pygame.locals import *
from player import Player
from move import Move


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.is_moving = False
        self.player = Player(0, 0, pygame.image.load_extended("Assets/Spiral.png").convert_alpha())

    def game_loop(self):
        diff_y = 0
        diff_x = 0

        while True:
            if pygame.key.get_pressed()[K_DOWN] and self.is_moving:
                diff_y += 0.01
            if pygame.key.get_pressed()[K_UP] and self.is_moving:
                diff_y -= 0.01
            if pygame.key.get_pressed()[K_LEFT] and self.is_moving:
                diff_x -= 0.01
            if pygame.key.get_pressed()[K_RIGHT] and self.is_moving:
                diff_x += 0.01
            print(diff_x, diff_y)
            
            self.screen.fill(0)
            self.player.show(self.screen)
            pygame.display.flip()

            if self.player.x <= self.player.move_to_x:
                self.player.x += 0.5

            if self.player.x >= self.player.move_to_x:
                self.player.x -= 0.5

            if self.player.y <= self.player.move_to_y:
                self.player.y += 0.5

            if self.player.y >= self.player.move_to_y:
                self.player.y -= 0.5

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_DOWN or event.key == K_UP or event.key == K_LEFT or event.key == K_RIGHT:
                        self.is_moving = True
                    if event.key == K_RETURN and self.is_moving:
                        self.is_moving = False
                        self.player.move(diff_x, diff_y)
                        diff_x, diff_y = 0, 0  # Reset the differences after each move
                if event.type == QUIT:
                    quit(-10)
