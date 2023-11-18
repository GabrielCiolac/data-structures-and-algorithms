# Test case 1: Pair exists in the list
from section_4_google_interview_question import find_pair


nums1 = [1, 2, 3, 4, 5]
sum1 = 7
expected1 = (2, 5)
assert find_pair(nums1, sum1) == expected1

# Test case 2: Pair does not exist in the list
nums2 = [1, 2, 3, 4, 5]
sum2 = 10
expected2 = None
assert find_pair(nums2, sum2) == expected2

# Test case 3: Pair with duplicate numbers
nums3 = [1, 2, 3, 4, 5, 5]
sum3 = 10
expected3 = (5, 5)
assert find_pair(nums3, sum3) == expected3

# Test case 4: Empty list
nums4 = []
sum4 = 5
expected4 = None
assert find_pair(nums4, sum4) == expected4

# Test case 5: Pair with negative numbers
nums5 = [-1, 2, -3, 4, -5]
sum5 = -4
expected5 = (-3, -1)
assert find_pair(nums5, sum5) == expected5

print("All test cases passed!")
