def solve(nums, target):
    """
    01. Two Sum
    -----------
    Given an array of integers `nums` and an integer `target`, return indices of the two numbers
    such that they add up to `target`.

    Example:
        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]

    Assume exactly one solution exists, and you may not use the same element twice.
    """

    existing = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in existing:
            return [existing[complement], i]
        existing[num] = i

    raise ValueError('Solution does not exist with the given input!')

if __name__ == "__main__":
    print(solve([2, 7, 11, 15], 9))  # Expected output: [0, 1]