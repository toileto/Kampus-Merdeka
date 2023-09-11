import pytest
import time
import psutil
from challenge.ch_2_ans import is_connected  # Replace with your actual function import

def memory_usage():
    process = psutil.Process()
    return process.memory_info().rss / (1024 ** 2)  # Memory usage in MB


def test_is_connected():
    # Example graph
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'E'],
        'D': ['B'],
        'E': ['C'],
    }

    # Test case 1
    start_time = time.time()
    result1 = is_connected(graph, 'A', 'D')
    end_time = time.time()
    runtime = end_time - start_time
    mem_used = memory_usage()
    assert result1 == True
    print(f"Test 1: Runtime: {runtime} seconds, Memory Used: {mem_used} MB")

    # Test case 2
    start_time = time.time()
    result2 = is_connected(graph, 'A', 'E')
    end_time = time.time()
    runtime = end_time - start_time
    mem_used = memory_usage()
    assert result2 == True
    print(f"Test 2: Runtime: {runtime} seconds, Memory Used: {mem_used} MB")


if __name__ == "__main__":
    pytest.main()
