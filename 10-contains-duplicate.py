def solve(nums, k):
    '''
    Contains Duplicate II
    ---------------------
    Given an integer array nums and an integer k, return True if there are two distinct indices 
    i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k, otherwise return False.

    Example 1:
    Input: nums = [1,2,3,1], k = 3
    Output: True
    Explanation: nums[0] == nums[3] and abs(0 - 3) = 3 <= 3

    Example 2:
    Input: nums = [1,0,1,1], k = 1
    Output: True

    Example 3:
    Input: nums = [1,2,3,1,2,3], k = 2
    Output: False

    Constraints:
    - 1 <= len(nums) <= 10^5
    - -10^9 <= nums[i] <= 10^9
    - 0 <= k <= 10^5
    '''
    validate_input(nums, k)

    seen = {}  # dictionary to track uniqueness (key: the number, value: its index)
    for i, num in enumerate(nums):  # loop through each number and its index
        if num in seen:  # if we already have the number as a key, we matched the first condition (nums[i] == nums[j])
            if abs(seen[num] - i) <= k: # check if we matched the second condition (abs(i - j) <= k)
                return True  # if so, return True
            else:
                seen[num] = i  # there may be the same number on another index in the array, which will match the second condition with the current index. So we overwrite the value of the already seen number with the current index
        else:
            seen[num] = i  # current number has not been seen, so add it with its index in the dictionary

    return False  # if we come here, there are no two elements to match the condition in the array


def validate_input(nums, k):
    if not isinstance(nums, list):
        raise TypeError("nums must be a list of integers.")
    if not all(isinstance(num, int) for num in nums):
        raise ValueError("All elements in nums must be integers.")
    if not isinstance(k, int):
        raise TypeError("k must be an integer.")
    if not (0 <= k <= 10**5):
        raise ValueError("k must be between 0 and 10^5.")
    if not (1 <= len(nums) <= 10**5):
        raise ValueError("Array length must be between 1 and 10^5.")


if __name__ == "__main__":
    print(solve([1, 2, 3, 1], 3))         # Expected: True
    print(solve([1, 0, 1, 1], 1))         # Expected: True
    print(solve([1, 2, 3, 1, 2, 3], 2))   # Expected: False
