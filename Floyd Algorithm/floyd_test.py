"""
This is a unit test for Floyd's algorithm with looping. 
"""
# importing the module
import unittest
import sys
import floyd


class TestFloyd(unittest.TestCase):
    """
    This is a class that included the unit test for Floyd's algorithm with looping. 
    """

    def test_floyd(self):
        """
        A test of Floyd's algorithm function with looping.
        Define the input graph and preset the expected graph.
        Test the result graph is equal to the input graph or not.
        """
        # Define the number of NO_PATH in the graph
        NO_PATH = sys.maxsize
        # Define the distance matrix of the graph (test case)
        input_graph = [[0, 5, NO_PATH, 10],
                       [NO_PATH, 0, 3, NO_PATH],
                       [NO_PATH, NO_PATH, 0, 1],
                       [NO_PATH, NO_PATH, NO_PATH, 0]]
        # expected result (test case)
        expected_graph = [[0, 5, 8, 9],
                          [NO_PATH, 0, 3, 4],
                          [NO_PATH, NO_PATH, 0, 1],
                          [NO_PATH, NO_PATH, NO_PATH, 0]]
        # Get and define the length of the graph
        MAX_LENGTH = len(input_graph[0])

        # Define object
        mfloyd = floyd.Floyd()
        # Result graph
        result_graph = mfloyd.floyd_looping(input_graph)
        # print the expected graph
        print("[Expected Graph] Show the distances between every pair of vertices of the expected graph matrix:")
        mfloyd.print_solution(expected_graph, MAX_LENGTH)

        # Test the result graph is/not equal to expected graph
        self.assertEqual(result_graph, expected_graph)


if __name__ == "__main__":
    unittest.main()
