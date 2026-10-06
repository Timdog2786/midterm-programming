import time
import random
import seaborn
import pandas
import matplotlib.pyplot 

# =======================================================
# DO NOT MODIFY THE ALGORITHM IMPLEMENTATIONS
# =======================================================

def find_duplicates_slow(data):
    """An O(n^2) algorithm to find duplicates."""
    n = len(data)
    for i in range(n):
        for j in range(i + 1, n):
            if data[i] == data[j]:
                return True
    return False

def find_duplicates_fast(data):
    """An O(n) algorithm to find duplicates."""
    seen = set()
    for item in data:
        if item in seen:
            return True
        seen.add(item)
    return False


# =======================================================
# YOUR TASK: FIX THE BENCHMARKING SCRIPT BELOW
# =======================================================

def flawed_benchmark():
    """
    This benchmarking function contains several methodological errors.
    Rewrite this function to properly and fairly compare the two algorithms to demonstrate their scaling behavior.
    """
    print("Running flawed benchmark...")

    element_count = 50000
    tests = [(1000, 10000, element_count), (1000, 100000, element_count), (1000, 1000000, element_count), (1000, 10000000, element_count), (1000, 100000000, element_count)]
    ranges = []
    fast_benchmark = []
    slow_benchmark = []
    for min_value, max_value, n_elements in tests:
        AVERAGE_TEST = 10
        n = n_elements
        data = [random.randint(min_value, max_value) for _ in range(n)]

        total_time = 0
        for _ in range(AVERAGE_TEST):
            start_time = time.perf_counter()
            ended_early = find_duplicates_slow(data)
            end_time = time.perf_counter()
            total_time += end_time - start_time
        slow_benchmark.append((total_time/AVERAGE_TEST, ended_early))


        total_time = 0
        for _ in range(AVERAGE_TEST):
            start_time_2 = time.perf_counter()
            ended_early = find_duplicates_fast(data)
            end_time_2 = time.perf_counter()
            total_time += end_time_2 - start_time_2
        fast_benchmark.append((total_time/AVERAGE_TEST, ended_early))

        ranges.append(max_value - min_value)

    
    df = pandas.DataFrame({"range": ranges + ranges,
                           "alogrithem_time": [i[0] for i in slow_benchmark] + [i[0] for i in fast_benchmark],
                           "early_finish": [i[1] for i in slow_benchmark] + [i[1] for i in fast_benchmark], 
                           "method": ["slow" for _ in range(len(slow_benchmark))] + ["fast" for _ in range(len(fast_benchmark))]})

    print(df)
    graph = seaborn.lineplot(df,
                     x="range",
                     y="alogrithem_time",
                     hue="method",
                     style="early_finish",
                     markers={True: "", False: "x"},
                     mew = 3,
                     mec = "red")
    graph.set_yscale('log')
    graph.set_xlim(min(ranges), max(ranges))
    graph.set_xticks(ranges)
    graph.set_xscale("log")
    graph.set_xlabel("Range of values")
    graph.set_ylabel("Time to find matching pair (seconds)")
    matplotlib.pyplot.show()

if __name__ == "__main__":
    flawed_benchmark()