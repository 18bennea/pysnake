from enum import Enum
import sys

class Entities(Enum):
    NULL = lambda x, y: Entity(x, y, "--")

class Direction(Enum):
    RIGHT = 100
    UP = 119
    LEFT = 97
    DOWN = 115

class Entity:
    def __init__(self, x: int, y: int, value: str):
        self.x = x
        self.y = y
        self.value = value

    def at(self):
        return (self.x, self.y)

class Game:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.map = [[Entities.NULL(i, j) for i in range(x)] for j in range(y)]

    def render(self):
        for y in range(self.y):
            for x in range(self.x):
                sys.stdout.write(self.map[x][y].value)

            print("\n", end="")

    def at(self, x: int, y: int):
        return self.map[x][y]

    def set(self, entity: Entity):
        self.map[entity.x][entity.y] = entity


class Snake(Entity):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, u"SS")
        self.direction = Direction.RIGHT.value

    def move(self, keypress: str, game: Game):
        if keypress == Direction.RIGHT.value:
            self.x += 1
            self.direction = Direction.RIGHT.value
        elif keypress == Direction.UP.value:
            self.y -= 1
            self.direction = Direction.UP.value
        elif keypress == Direction.LEFT.value:
            self.x -= 1
            self.direction = Direction.LEFT.value
        elif keypress == Direction.DOWN.value:
            self.y += 1
            self.direction = Direction.DOWN.value
        else: self.move(self.direction)
        if(self.x < 0 or self.y < 0 or self.x >= game.x or self.y >= game.y):
            return False
        else:
            return True
