#!/usr/bin/env python3

# given 2 arrays, create a function that lets a user know (true/false) whether these two arrays contain any common items
from typing import List
from section_4_google_interview_question import time_function

def has_next(arr1:List, current_index:int) -> bool:
    try:
        arr1[current_index + 1]
        return True
    except IndexError:
        return False

def find_common(array1: List, array2: List) -> bool:
    set1 = set()
    set2 = set()

    for index in range(len(array1)):
        set1.add(array1[index])
        set2.add(array2[index])

        if array1[index] in set2:
            return True
        elif array2[index] in set1:
            return True
        elif has_next(array1, index) is False:
            return False
        elif has_next(array2, index) is False:
            return False
    
    return False



if __name__ == "__main__":
    # Test case 1: Pair exists in the list
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [6, 7, 8, 9, 10]
    expected1 = False
    assert find_common(nums1, nums2) == expected1

    # Test case 2: Pair does not exist in the list
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [5, 6, 7, 8, 9]
    expected2 = True
    assert find_common(nums1, nums2) == expected2

    # Test case 3: Pair with duplicate numbers
    nums1 = [1, 2, 3, 4, 5, 5]
    nums2 = [5, 6, 7, 8, 9, 5]
    expected3 = True

    assert find_common(nums1, nums2) == expected3

    # time it with a large list, second list is descending
    time_function(find_common, list(range(1000000)), list(range(1000000, 0, -1)))

    # time with a larger list, second list is descending
    time_function(find_common, list(range(100000000)), list(range(100000000, 0, -1)))

