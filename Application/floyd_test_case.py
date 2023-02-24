"""
There are FIVE test cases and expected output.
Cases 1-4 id used to test the performance difference when vertices increase 
(3 vertices increase to 6 vertices)
Case 5 is an undirected graph at all vertices
Case 6 included negative edges
"""
# importing the module
import sys

# Define the number of NO_PATH in the graph
NO_PATH = sys.maxsize

# Test Case 1 : Distance matrix graph with 3 vertices
case_1 = [[0, 3, NO_PATH],
          [4, 0, 5],
          [9, 2, 0]]
# Expected output for Test Case 1
expect_output_1 = [[0, 3, 8],
                   [4, 0, 5],
                   [6, 2, 0]]

# Test Case 2 : Distance matrix graph with 4 vertices (default one)
case_2 = [[0, 7, NO_PATH, 8],
          [NO_PATH, 0, 5, NO_PATH],
          [NO_PATH, NO_PATH, 0, 2],
          [NO_PATH, NO_PATH, NO_PATH, 0]]
# Expected output for Test Case 2
expect_output_2 = [[0, 7, 12, 8],
                   [NO_PATH, 0, 5, 7],
                   [NO_PATH, NO_PATH, 0, 2],
                   [NO_PATH, NO_PATH, NO_PATH, 0]]

# Test Case 3 : Distance matrix graph with 5 vertices
case_3 = [[0, 3, NO_PATH, 2, NO_PATH],
          [NO_PATH, 0, NO_PATH, 5, 1],
          [2, NO_PATH, 0, 4, 2],
          [NO_PATH, 3, NO_PATH, 0, 4],
          [3, NO_PATH, 6, NO_PATH, 0]]
# Expected output for Test Case 3
expect_output_3 = [[0, 3, 10, 2, 4],
                   [4, 0, 7, 5, 1],
                   [2, 5, 0, 4, 2],
                   [7, 3, 10, 0, 4],
                   [3, 6, 6, 5, 0]]

# Test Case 4 : Distance matrix graph with 6 vertices
case_4 = [[0, 1, 4, NO_PATH, 2, NO_PATH],
          [NO_PATH, 0, 5, NO_PATH, NO_PATH, 1],
          [NO_PATH, NO_PATH, 0, 3, 3, NO_PATH],
          [NO_PATH, NO_PATH, 1, 0, NO_PATH, 7],
          [NO_PATH, 2, NO_PATH, NO_PATH, 0, 6],
          [NO_PATH, NO_PATH, NO_PATH, 2, NO_PATH, 0]]
# Expected output for Test Case 4
expect_output_4 = [[0, 1, 4, 4, 2, 2],
                   [NO_PATH, 0, 4, 3, 7, 1],
                   [NO_PATH, 5, 0, 3, 3, 6],
                   [NO_PATH, 6, 1, 0, 4, 7],
                   [NO_PATH, 2, 6, 5, 0, 3],
                   [NO_PATH, 8, 3, 2, 6, 0]]

# Test Case 5 : An undirected graph at all vertices
case_5 = [[0, 2, NO_PATH, NO_PATH],
          [NO_PATH, 0, 3, NO_PATH],
          [NO_PATH, NO_PATH, 0, 4],
          [5, NO_PATH, NO_PATH, 0]]
# Expected output for Test Case 5
expect_output_5 = [[0, 2, 5, 9],
                   [12, 0, 3, 7],
                   [9, 11, 0, 4],
                   [5, 7, 10, 0]]

# Test Case 6 : An undirected graph at all vertices with negative edges
case_6 = [[0, 5, NO_PATH, NO_PATH],
          [NO_PATH, 0, -3, 2],
          [-2, NO_PATH, 0, NO_PATH],
          [NO_PATH, -1, NO_PATH, 0]]
# Expected output for Test Case 6
expect_output_6 = [[0, 5, 2, 7],
                   [-5, 0, -3, 2],
                   [-2, 3, 0, 5],
                   [-6, -1, -4, 0]]
