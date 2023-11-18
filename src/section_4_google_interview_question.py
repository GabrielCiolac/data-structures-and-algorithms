#!/usr/bin/env python3

'''
https://www.youtube.com/watch?v=XKu_SEDAykw

Question: You're given a collection of numbers, and a sum.

Find a pair of numbers in that collection who add together to the given sum.
fun(collection, sum) -> tuple():
'''

from typing import List, Optional, Tuple

log_results = True

def time_function(func, *args, **kwargs):
    import time
    start = time.time()
    response = func(*args, **kwargs)
    end = time.time()
    if log_results:
        print(f"{func.__name__} took {end - start} seconds to run, and returned {response}")
    else:
        print(f"{func.__name__} took {end - start} seconds to run")


def find_pair(nums: List[int], sum: int) -> Optional[Tuple[int, int]]:
    nums_set = set() # using a set to make lookups O(1) instead of O(n)

    for num in nums:
        if sum - num in nums_set:
            return (num, sum - num)
        nums_set.add(num)

    return None



if __name__ == "__main__":
    time_function(find_pair, [1, 2, 3, 4, 5], 7)

    # time it with a large list
    time_function(find_pair, list(range(1000000)), 999999)

    # time it with an even larger list
    time_function(find_pair, list(range(100000000)), 99999999)

    # time the set conversions of the above
    log_results = False
    convert_to_set = lambda x: set(x)
    time_function(convert_to_set, list(range(1000000)))
    time_function(convert_to_set, list(range(100000000)))