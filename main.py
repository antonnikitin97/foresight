import pygame
import game

pygame.init()
screen_dimensions = (640, 480)
screen = pygame.display.set_mode(screen_dimensions)
game = game.Game(screen)
game.game_loop()
