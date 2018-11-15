from game import Game, Snake, Entities, Direction
import msvcrt as m
import os
import time

if __name__ == '__main__':
    game = Game(20, 20)
    snake = Snake(10, 10)
    game.set(snake)
    game.render()
    running = True
    # Main game loop
    while(running):
        keypress = None
        if(m.kbhit()):
            keypress = ord(m.getch())
            os.system('cls')
            game.set(Entities.NULL(snake.x, snake.y))
            running = snake.move(game, keypress)
            if(not running):
                break
            game.set(snake)
            game.render()
    os.system('cls')
    print("You Lose")
