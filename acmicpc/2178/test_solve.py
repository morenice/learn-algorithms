import unittest
import solve


def print_maze(maze):
    for i in range(len(maze)):
        print(maze[i])


class SolveTestCase(unittest.TestCase):
    def test_make_empty_maze(self):
        maze = solve.make_empty_maze(5, 7)
        self.assertEqual(len(maze), 5)
        self.assertEqual(maze[0][0], 0)
        self.assertEqual(maze[4][6], 0)

    def test_breath_first_search(self):
        maze = [[1, 0, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 1], [1, 1, 1, 0, 1, 1]]
        maze_distance = solve.bfs(maze, 0, 0)
        self.assertEqual(maze_distance[3][5], 15)

    def test_breath_first_search2(self):
        maze = [[1, 1, 0, 1, 1, 0], [1, 1, 0, 1, 1, 0], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 0, 1]]
        maze_distance = solve.bfs(maze, 0, 0)
        self.assertEqual(maze_distance[3][5], 9)


if __name__ == '__main__':
    unittest.main()
