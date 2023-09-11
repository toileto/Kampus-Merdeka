import pytest
import psutil
import time
from challenge.ch_1_ans import longest_increasing_subsequence  # Replace with your actual function import


def memory_usage():
    process = psutil.Process()
    return process.memory_info().rss / (1024 ** 2)  # Memory usage in MB

def test_longest_increasing_subsequence():
    # Test case 1
    start_time = time.time()
    sequence = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    end_time = time.time()
    runtime = end_time - start_time
    mem_used = memory_usage()
    assert longest_increasing_subsequence(sequence) == 6
    print(f"Test 1: Runtime: {runtime} seconds, Memory Used: {mem_used} MB")

    # Test case 2
    start_time = time.time()
    sequence = [3, 4, -1, 0, 6, 2, 3]
    end_time = time.time()
    runtime = end_time - start_time
    mem_used = memory_usage()
    assert longest_increasing_subsequence(sequence) == 4
    print(f"Test 2: Runtime: {runtime} seconds, Memory Used: {mem_used} MB")

    # Test case 3 (edge case: empty input)
    start_time = time.time()
    sequence = []
    end_time = time.time()
    runtime = end_time - start_time
    mem_used = memory_usage()
    assert longest_increasing_subsequence(sequence) == 0
    print(f"Test 3: Runtime: {runtime} seconds, Memory Used: {mem_used} MB")

    # Test case 4 (edge case: single element)
    start_time = time.time()
    sequence = [5]
    end_time = time.time()
    runtime = end_time - start_time
    mem_used = memory_usage()
    assert longest_increasing_subsequence(sequence) == 1
    print(f"Test 4: Runtime: {runtime} seconds, Memory Used: {mem_used} MB")

    # Test case 5 (edge case: all elements in descending order)
    start_time = time.time()
    sequence = [5, 4, 3, 2, 1]
    end_time = time.time()
    runtime = end_time - start_time
    mem_used = memory_usage()
    assert longest_increasing_subsequence(sequence) == 1
    print(f"Test 5: Runtime: {runtime} seconds, Memory Used: {mem_used} MB")


if __name__ == "__main__":
    pytest.main()
