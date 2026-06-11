import os
import random
import time
import msvcrt

WIDTH = 20
HEIGHT = 10


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def draw_board(gekko, fly, score, moves):
    clear_screen()
    print('Gekko Game')
    print('Score:', score, 'Moves:', moves)
    print('-' * (WIDTH + 2))
    for y in range(HEIGHT):
        row = '|'
        for x in range(WIDTH):
            if (x, y) == gekko:
                row += 'G'
            elif (x, y) == fly:
                row += '*'
            else:
                row += ' '
        row += '|'
        print(row)
    print('-' * (WIDTH + 2))
    print('Use W A S D to move, Q to quit.')


def get_move():
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch().decode('utf-8', errors='ignore').lower()
            if key in ('w', 'a', 's', 'd', 'q'):
                return key
        time.sleep(0.05)


def place_fly(exclude):
    while True:
        pos = (random.randrange(WIDTH), random.randrange(HEIGHT))
        if pos != exclude:
            return pos


def move_gekko(position, direction):
    x, y = position
    if direction == 'w':
        y = max(0, y - 1)
    elif direction == 's':
        y = min(HEIGHT - 1, y + 1)
    elif direction == 'a':
        x = max(0, x - 1)
    elif direction == 'd':
        x = min(WIDTH - 1, x + 1)
    return x, y


def main():
    gekko = (WIDTH // 2, HEIGHT // 2)
    fly = place_fly(gekko)
    score = 0
    moves = 0

    draw_board(gekko, fly, score, moves)
    while True:
        move = get_move()
        if move == 'q':
            break

        new_position = move_gekko(gekko, move)
        if new_position != gekko:
            gekko = new_position
            moves += 1

        if gekko == fly:
            score += 1
            fly = place_fly(gekko)

        draw_board(gekko, fly, score, moves)

    clear_screen()
    print('Thanks for playing!')
    print('Final score:', score)
    print('Total moves:', moves)


if __name__ == '__main__':
    main()
