"""
This is a simple Floyd's algorithm with looping. 
The application will check and print the shortest path base on the inputted graph.
The application will calculate the running time of function floyd(distance).
"""
# importing the module
import sys
import itertools
import time


def floyd(distance):
    """
    A simple implementation of Floyd's algorithm function with looping.
    """
    # Performance testing by brute force
    start_time = time.perf_counter()  # datetime.datetime.now()
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
    end_time = time.perf_counter()  # datetime.datetime.now()
    # Any value that have sys.maxsize has no path
    print_solution(distance)
    # print the program running time
    print(
        f'The running time of Floyd algorithm with looping: {end_time - start_time}.')


def print_solution(dist):
    """
    A utility function to print the solution.
    """
    print(
        "Following matrix shows the shortest distances between every pair of vertices")
    for i in range(MAX_LENGTH):
        for j in range(MAX_LENGTH):
            if (dist[i][j] == NO_PATH):
                print(("NO_PATH"), end="  ")
            else:
                print(f'      {dist[i][j]}', end="  ")
            if j == MAX_LENGTH-1:
                print()


# Driver's code
if __name__ == "__main__":

    # Define the number of NO_PATH in the graph
    NO_PATH = sys.maxsize
    # Define the distance matrix of the graph
    graph = [[0, 7, NO_PATH, 8],
             [NO_PATH, 0, 5, NO_PATH],
             [NO_PATH, NO_PATH, 0, 2],
             [NO_PATH, NO_PATH, NO_PATH, 0]]
    # Get and define the length of the graph
    MAX_LENGTH = len(graph[0])

    # Function call
    floyd(graph)
    print("-------------------------------------------------------------------------------")
    print("-------------------------------------------------------------------------------")
