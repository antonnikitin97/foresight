import pygame
from pygame.locals import *


class Game:
    def __init__(self, screen):
        self.screen = screen


    def game_loop(self):

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    quit(-10)
