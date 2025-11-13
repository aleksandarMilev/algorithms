def solve(nums):
    '''
    Majority Element
    ----------------
    Given an array nums of size n, return the majority element -
    the element that appears more than ⌊n / 2⌋ times.

    You may assume that the array is non-empty and the majority element always exists.

    Example 1:
    Input: nums = [3,2,3]
    Output: 3

    Example 2:
    Input: nums = [2,2,1,1,1,2,2]
    Output: 2

    Constraints:
    - n == len(nums)
    - 1 <= n <= 5 * 10^4
    - -10^9 <= nums[i] <= 10^9
    - The majority element always exists
    '''
    validate_input(nums)

    seen = {}
    for num in nums:
        seen[num] = seen.get(num, 0) + 1

    return max(seen, key=seen.get)


def validate_input(nums):
    if not isinstance(nums, list):
        raise TypeError("Input must be a list of integers.")
    if not all(isinstance(num, int) for num in nums):
        raise ValueError("All elements in the array must be integers.")
    if not (1 <= len(nums) <= 5 * 10**4):
        raise ValueError("Array length must be between 1 and 5 * 10^4.")


if __name__ == "__main__":
    print(solve([3,2,3]))          # Expected: 3
    print(solve([2,2,1,1,1,2,2]))  # Expected: 2
