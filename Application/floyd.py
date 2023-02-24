"""
This is a simple Floyd's algorithm with TWO methods, imperative and recursive. 
The application will check and print the shortest path base on the inputted graph.
The application will calculate the running time of the functions floyd_imperative() and floyd_recursive().
"""
# Importing the module
import sys
import itertools
import time


class Floyd:
    """
    This is a calss included 3 functions.
    Function floyd_imperative() is a Floyd's algorithm with imperative. 
    Function floyd_recursion() is a Floyd's algorithm with recursion.
    Function print_solution() is a print function for the matrix.
    """

    def floyd_imperative(self, distance):
        """
        A simple implementation of Floyd's algorithm function with imperative.
        """
        # Define MAX_LENGTH
        MAX_LENGTH = len(distance[0])

        # Main calculation for imperative
        for intermediate, start_node, end_node\
                in itertools.product(range(MAX_LENGTH), range(MAX_LENGTH), range(MAX_LENGTH)):
            # Assume that if start_node and end_node are the same
            # then the distance would be zero
            if start_node == end_node:
                distance[start_node][end_node] = 0
                continue
            # return all possible paths and find the minimum
            distance[start_node][end_node] = min(distance[start_node][end_node],
                                                 distance[start_node][intermediate] + distance[intermediate][end_node])

        # Return graph
        return distance

    def floyd_recursive(self, distance):
        """
        A simple implementation of Floyd's algorithm function with recursive.
        """
        # Define MAX_LENGTH
        MAX_LENGTH = len(distance[0])

        # Main calculation for recursive
        def recursive(intermediate, start_node, end_node):
            if intermediate == -1:
                return distance[start_node][end_node]
            else:
                return min(recursive(intermediate - 1, start_node, end_node),
                           recursive(intermediate - 1, start_node, intermediate) + recursive(intermediate - 1, intermediate, end_node))

        for intermediate, start_node, end_node\
                in itertools.product(range(MAX_LENGTH), range(MAX_LENGTH), range(MAX_LENGTH)):
            # return all possible paths and find the minimum
            distance[start_node][end_node] = recursive(
                intermediate, start_node, end_node)

        # Return graph
        return distance

    def print_solution(self, distance):
        """
        A utility function to print the solution.
        """
        # Define the number of NO_PATH in the graph
        NO_PATH = sys.maxsize
        MAX_LENGTH = len(distance[0])

        # Main print function
        for i in range(MAX_LENGTH):
            for j in range(MAX_LENGTH):
                if (distance[i][j] == NO_PATH):
                    # Any value that have sys.maxsize has no path
                    print(("NO_PATH"), end="  ")
                else:
                    print(f'      {distance[i][j]}', end="  ")
                if j == MAX_LENGTH-1:
                    print()
        print("-------------------------------------------------------------------------")


# Driver's code
if __name__ == "__main__":
    # Define the number of NO_PATH in the graph
    NO_PATH = sys.maxsize
    # Define the distance matrix of the graph
    input_imperative_graph = [[0, 3, NO_PATH, NO_PATH],
                              [NO_PATH, 0, -3, 2],
                              [-2, NO_PATH, 0, NO_PATH],
                              [NO_PATH, -1, NO_PATH, 0]]
    # Function call
    floyd_algorithm = Floyd()
    # Print input graph
    print("[Input Graph] Show the distances between every pair of vertices of the input graph matrix:")
    floyd_algorithm.print_solution(input_imperative_graph)
    # Print output graph with floyd imperative
    print("[Output Graph (imperative)] Following matrix shows the shortest distances between every pair of vertices:")
    # Performance testing by brute force
    start_time = time.perf_counter()
    result_graph = floyd_algorithm.floyd_imperative(input_imperative_graph)
    end_time = time.perf_counter()
    print(
        f'The running time of case 6 for the imperative floyd algorithm: {end_time - start_time}.')
    floyd_algorithm.print_solution(
        floyd_algorithm.floyd_imperative(result_graph))
    # Renew input graph
    input_recursive_graph = [[0, 3, NO_PATH, NO_PATH],
                             [NO_PATH, 0, -3, 2],
                             [-2, NO_PATH, 0, NO_PATH],
                             [NO_PATH, -1, NO_PATH, 0]]
    # Print output graph with floyd recursive
    print("[Output Graph (recursive)] Following matrix shows the shortest distances between every pair of vertices:")
    # Performance testing by brute force
    start_time = time.perf_counter()
    result_graph = floyd_algorithm.floyd_recursive(input_recursive_graph)
    end_time = time.perf_counter()
    print(
        f'The running time of case 6 for the recursive floyd algorithm: {end_time - start_time}.')
    floyd_algorithm.print_solution(
        floyd_algorithm.floyd_recursive(result_graph))
