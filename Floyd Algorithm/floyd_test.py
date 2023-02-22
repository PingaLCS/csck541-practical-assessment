import unittest
import floyd
import sys


class TestFloyd(unittest.TestCase):
    def test_floyd(self, input_graph, expected_graph):
        print(input_graph)
        print(expected_graph)
        self.assertEqual(floyd.floyd_algorithm.floyd_looping(
            input_graph), expected_graph)


if __name__ == '__man__':
    # Define the number of NO_PATH in the graph
    NO_PATH = sys.maxsize
    # Define the distance matrix of the graph
    graph = [[0, 7, NO_PATH, 8],
             [NO_PATH, 0, 5, NO_PATH],
             [NO_PATH, NO_PATH, 0, 2],
             [NO_PATH, NO_PATH, NO_PATH, 0]]
    # expected result
    expected_graph = [[0, 7, 12, 8],
                      [NO_PATH, 0, 5, 7],
                      [NO_PATH, NO_PATH, 0, 2],
                      [NO_PATH, NO_PATH, NO_PATH, 0]]
    # Get and define the length of the graph
    MAX_LENGTH = len(graph[0])

    print('Start Unit')
    unittest.main()
    m = TestFloyd()
    m.test_floyd(graph, expected_graph)
