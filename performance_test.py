import random
import time

from progressive_mean import ProgressiveMean

RANDOM_LIST_LEN = 10000

if __name__ == "__main__":

    random_numbers_list = [random.randint(1, RANDOM_LIST_LEN) for _ in range(RANDOM_LIST_LEN)]

    print(f"ProgressiveMean of random list of {RANDOM_LIST_LEN:,} elsements.")
    start = time.time()
    pa = ProgressiveMean()
    for e in random_numbers_list:
        pa.add_next(e)
    print(f"==> Result: {pa.mean:.6f}; Execution time: {time.time() - start:.10f}s.")

    print()
    print(f"Sum of a growing list of {RANDOM_LIST_LEN:,} elements divided by its length")
    start = time.time()
    for x in range(len(random_numbers_list)):
        mean = sum(random_numbers_list[:x + 1]) / len(random_numbers_list[:x + 1])
    print(f"==> Result: {mean:.6f}; Execution time: {time.time() - start:.10f}s.")

