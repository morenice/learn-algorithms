# -*- coding: utf-8 -*-
import copy


def make_empty_maze(m, n):
    return [[0 for i in range(n)] for k in range(m)]


def init_maze_for_distance(maze):
    for i in range(len(maze)):
        for k in range(len(maze[i])):
            maze[i][k] = -1


def make_maze(m, n):
    maze = make_empty_maze(m, n)
    for i in range(m):
        row = input()
        for k, value in enumerate(row):
            maze[i][k] = int(value)
    return maze


def is_possible_move_maze(maze, row, col):
    try:
        if row < 0 or col < 0:
            return False

        if maze[row][col] == 1:
            return True

        return False
    except:
        return False


def is_visited_maze(maze_distance, row, col):
    try:
        if maze_distance[row][col] == -1:
            return False

        return True
    except:
        return True


def bfs(maze, x, y):
    """ bfs: maze and start point row, column"""
    maze_distance = copy.deepcopy(maze)
    init_maze_for_distance(maze_distance)

    stack = list()
    stack.append((x, y))
    maze_distance[x][y] = 1

    while True:
        if len(stack) == 0:
            break

        (row, col) = stack.pop()

        if is_possible_move_maze(maze, row+1, col) and \
                is_visited_maze(maze_distance, row+1, col) == False:
            stack.append((row+1, col))
            maze_distance[row+1][col] = maze_distance[row][col] + 1

        if is_possible_move_maze(maze, row, col+1) and  \
                is_visited_maze(maze_distance, row, col+1) == False:
            stack.append((row, col+1))
            maze_distance[row][col+1] = maze_distance[row][col] + 1

        if is_possible_move_maze(maze, row-1, col) and  \
                is_visited_maze(maze_distance, row-1, col) == False:
            stack.append((row-1, col))
            maze_distance[row-1][col] = maze_distance[row][col] + 1

        if is_possible_move_maze(maze, row, col-1) and \
                is_visited_maze(maze_distance, row, col-1) == False:
            stack.append((row, col-1))
            maze_distance[row][col-1] = maze_distance[row][col] + 1

    return maze_distance


if __name__ == '__main__':
    maze_size = input().split(' ')
    x = int(maze_size[0])
    y = int(maze_size[1])

    maze = make_maze(x, y)
    maze_distance = bfs(maze, 0, 0)
    print(maze_distance[x-1][y-1])
