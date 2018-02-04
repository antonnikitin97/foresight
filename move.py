class Move:
    def __init__(self, diff_x, diff_y, entity):
        self.diff_x = diff_x
        self.diff_y = diff_y
        self.entity = entity

    def move(self):
        self.entity.x += self.diff_x
        self.entity.y += self.diff_y




