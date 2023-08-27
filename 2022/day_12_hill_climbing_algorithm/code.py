#! /usr/bin/python3


import os
from grid import Grid


def read_file(file_name: str) -> str:
    f = open(f'{os.path.dirname(os.path.realpath(__file__))}/{file_name}', 'r')
    text = f.read()
    f.close()
    return text


if __name__ == "__main__":
    text = read_file('input').split('\n')
    grid = Grid(text)
    print(f'Part 1: {grid.find_shortest_path_from_the_end(grid.end, grid.start)} steps')
    print(f'Part 2: {grid.find_shortest_path_from_the_end(grid.end)} steps')