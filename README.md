# Mid-Module Assignment, CSCK541-Software Development in Practice Jan 2023 B
This is a Practical Assessment: Programming. 
Created by Pinga Lau Chi Shing, MSc Data Science and Artificial Intelligence student.
Submitted to The University of Liverpool.

## The requirement of the assignment 
Floyd’s algorithm is a shortest path algorithm that identifies the shortest path between two nodes on a graph.
  1. Write the Python code for an imperative and recursive version of Floyd’s algorithm.
  2. Put under source control.
  3. Write to PEP standards.
  4. Write unit tests for each function.
  5. Write performance tests.
  6. Include directory tree.
  7. Include a Readme.md and dependencies.txt / requirements.txt.

## The Application
Python file `floyd.py` included the main class Floyd with THREE functions.
    - `floyd_imperative(self, distance)`: identify the shortest path between two nodes on a graph using the imperative method.
    - `floyd_recursive(self, distance)`: identify the shortest path between two nodes on a graph using the recursive method.
    - `print_solution(self, distance)`: a utility function to print the matrix result.

Python file `floyd_test_case.py` pre-defined SIX sets of test case and the expected result.

Python file `floyd_test.py` for unit tests and performance test.
    - included SIX sets of test case.

## Usage
  1. Run the python code in the file `floyd_test.py`. You will get the tests and performance results of the pre-defined test cases.
  2. In the file `floyd.py`, you can change the driver's code to test what matrix graph you want to try. Then run the code and you will get the tests and performance results of that matrix graph.

## License
[MIT] Copyright (c) 2023 Pinga Lau Chi Shing
