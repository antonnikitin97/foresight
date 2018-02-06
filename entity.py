import pygame
from move import Move

class Entity:
    def __init__(self, x, y, spritelist, spriteindex=0):
        self.x = x
        self.y = y
        self.moves = []
        self.spritelist = spritelist
        self.spriteindex = spriteindex
        self.sprite = spritelist[spriteindex]
        self.move_to_x = 0  # These variables represent where the player *should be*
        self.move_to_y = 0

    def move(self, diffx, diffy, backlog=1):
        self.moves.append(Move(diffx, diffy, self))
        if len(self.moves) > backlog:
            self.moves.pop(0).move()

    def show(self, screen):
        screen.blit(self.sprite, (self.x, self.y))
