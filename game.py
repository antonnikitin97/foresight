import pygame
from pygame.locals import *
from player import Player
from move import Move


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.is_moving = False
        self.player = None

    def game_loop(self):
        diff_y = 0
        diff_x = 0

        while True:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_DOWN or event.key == K_UP or event.key == K_LEFT or event.key == K_RIGHT:
                        self.is_moving = True
                    if event.key == K_RETURN and self.is_moving:
                        self.is_moving = False
                        Move(diff_x, diff_y, self.player)
                        diff_x, diff_y = 0, 0 # Reset the differences after each move
                if event.type == QUIT:
                    quit(-10)

            if pygame.key.get_pressed()[K_DOWN] and self.is_moving:
                diff_y += 0.01
            if pygame.key.get_pressed()[K_UP] and self.is_moving:
                diff_y -= 0.01
            if pygame.key.get_pressed()[K_LEFT] and self.is_moving:
                diff_x -= 0.01
            if pygame.key.get_pressed()[K_RIGHT] and self.is_moving:
                diff_x += 0.01
