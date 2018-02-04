from entity import Entity


class Player(Entity):
    def __init__(self, x, y, sprite):
        super(Player, self).__init__(x, y, [sprite])

    def move(self, diffx, diffy):
        super(Player, self).move(diffx, diffy)