"""
This is a unit test for Floyd's algorithm.
Included performance test and ptint the result
"""
# importing the module
import unittest
import floyd
import floyd_test_case
import time


class TestFloyd(unittest.TestCase):
    """
    This is a class that included the unit test for Floyd's algorithm. 
    Also, included performance test and result
    """

    def test_case_1_i(self):
        # Performance testing by brute force
        start_time = time.perf_counter()
        result_graph = floyd.Floyd.floyd_imperative(
            self, floyd_test_case.case_1)
        end_time = time.perf_counter()
        # Unit test for case 1
        self.assertEqual(result_graph, floyd_test_case.expect_output_1)
        # Print the program running time of case 1
        print(
            f'[Performance Test] The running time of case 1 for the imperative floyd algorithm: {end_time - start_time}.')

    def test_case_2_i(self):
        # Performance testing by brute force
        start_time = time.perf_counter()
        result_graph = floyd.Floyd.floyd_imperative(
            self, floyd_test_case.case_2)
        end_time = time.perf_counter()
        # Unit test for case 2
        self.assertEqual(result_graph, floyd_test_case.expect_output_2)
        # Print the program running time of case 2
        print(
            f'[Performance Test] The running time of case 2 for the imperative floyd algorithm: {end_time - start_time}.')

    def test_case_3_i(self):
        # Performance testing by brute force
        start_time = time.perf_counter()
        result_graph = floyd.Floyd.floyd_imperative(
            self, floyd_test_case.case_3)
        end_time = time.perf_counter()
        # Unit test for case 3
        self.assertEqual(result_graph, floyd_test_case.expect_output_3)
        # Print the program running time of case 3
        print(
            f'[Performance Test] The running time of case 3 for the imperative floyd algorithm: {end_time - start_time}.')

    def test_case_4_i(self):
        # Performance testing by brute force
        start_time = time.perf_counter()
        result_graph = floyd.Floyd.floyd_imperative(
            self, floyd_test_case.case_4)
        end_time = time.perf_counter()
        # Unit test for case 4
        self.assertEqual(result_graph, floyd_test_case.expect_output_4)
        # Print the program running time of case 4
        print(
            f'[Performance Test] The running time of case 4 for the imperative floyd algorithm: {end_time - start_time}.')

    def test_case_1_r(self):
        # Performance testing by brute force
        start_time = time.perf_counter()
        result_graph = floyd.Floyd.floyd_recursive(
            self, floyd_test_case.case_1)
        end_time = time.perf_counter()
        # Unit test for case 1
        self.assertEqual(result_graph, floyd_test_case.expect_output_1)
        # Print the program running time of case 1
        print(
            f'[Performance Test] The running time of case 1 for the recursive floyd algorithm: {end_time - start_time}.')

    def test_case_2_r(self):
        # Performance testing by brute force
        start_time = time.perf_counter()
        result_graph = floyd.Floyd.floyd_recursive(
            self, floyd_test_case.case_2)
        end_time = time.perf_counter()
        # Unit test for case 2
        self.assertEqual(result_graph, floyd_test_case.expect_output_2)
        # Print the program running time of case 2
        print(
            f'[Performance Test] The running time of case 2 for the recursive floyd algorithm: {end_time - start_time}.')

    def test_case_3_r(self):
        # Performance testing by brute force
        start_time = time.perf_counter()
        result_graph = floyd.Floyd.floyd_recursive(
            self, floyd_test_case.case_3)
        end_time = time.perf_counter()
        # Unit test for case 3
        self.assertEqual(result_graph, floyd_test_case.expect_output_3)
        # Print the program running time of case 3
        print(
            f'[Performance Test] The running time of case 3 for the recursive floyd algorithm: {end_time - start_time}.')

    def test_case_4_r(self):
        # Performance testing by brute force
        start_time = time.perf_counter()
        result_graph = floyd.Floyd.floyd_recursive(
            self, floyd_test_case.case_4)
        end_time = time.perf_counter()
        # Unit test for case 4
        self.assertEqual(result_graph, floyd_test_case.expect_output_4)
        # Print the program running time of case 4
        print(
            f'[Performance Test] The running time of case 4 for the recursive floyd algorithm: {end_time - start_time}.')

    def test_case_5_i(self):
        # Performance testing by brute force
        start_time = time.perf_counter()
        result_graph = floyd.Floyd.floyd_imperative(
            self, floyd_test_case.case_5)
        end_time = time.perf_counter()
        # Unit test for case 5
        self.assertEqual(result_graph,  floyd_test_case.expect_output_5)
        # Print the program running time of case 5
        print(
            f'[Performance Test] The running time of case 5 for the imperative floyd algorithm: {end_time - start_time}.')

    def test_case_5_r(self):
        # Performance testing by brute force
        start_time = time.perf_counter()
        result_graph = floyd.Floyd.floyd_recursive(
            self, floyd_test_case.case_5)
        end_time = time.perf_counter()
        # Unit test for case 5
        self.assertEqual(result_graph, floyd_test_case.expect_output_5)
        # Print the program running time of case 5
        print(
            f'[Performance Test] The running time of case 5 for the recursive floyd algorithm: {end_time - start_time}.')

    def test_case_6_i(self):
        # Performance testing by brute force
        start_time = time.perf_counter()
        result_graph = floyd.Floyd.floyd_imperative(
            self, floyd_test_case.case_6)
        end_time = time.perf_counter()
        # Unit test for case 6
        self.assertEqual(result_graph,  floyd_test_case.expect_output_6)
        # Print the program running time of case 6
        print(
            f'[Performance Test] The running time of case 6 for the imperative floyd algorithm: {end_time - start_time}.')

    def test_case_6_r(self):
        # Performance testing by brute force
        start_time = time.perf_counter()
        result_graph = floyd.Floyd.floyd_recursive(
            self, floyd_test_case.case_6)
        end_time = time.perf_counter()
        # Unit test for case 6
        self.assertEqual(result_graph,  floyd_test_case.expect_output_6)
        # Print the program running time of case 6
        print(
            f'[Performance Test] The running time of case 6 for the recursive floyd algorithm: {end_time - start_time}.')


if __name__ == "__main__":
    unittest.main()
