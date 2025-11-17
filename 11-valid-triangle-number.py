def solve(nums):
    '''
    Valid Triangle Number
    ---------------------
    Given an integer array nums, return the number of triplets (i, j, k) such that:
        i < j < k  and  nums[i] + nums[j] > nums[k]

    A triplet meeting that condition can form the sides of a triangle.

    Example 1:
    Input: nums = [2,2,3,4]
    Output: 3
    Explanation: Valid triplets are (2,3,4), (2,3,4), (2,2,3)

    Example 2:
    Input: nums = [4,2,3,4]
    Output: 4

    Constraints:
    - 3 <= len(nums) <= 1000
    - 0 <= nums[i] <= 1000
    '''
    validate_input(nums)

    triplets_count = 0 # count total valid triplets
    nums = sorted(nums) # if nums are not ordered by ascending, we can not use the two pointer approach below
    largest_num_idx = len(nums) - 1 # pointer to the largest num of the array, we treat it as the largest side of a potential triangle

    while largest_num_idx >= 2: # we need at least 3 nums to form a triangle
        middle_num_idx = largest_num_idx - 1 # treat the num before largest as the middle side of potential triangle
        smallest_num_idx = 0 # treat the first num in the array as the smallest side of potential triangle

        while smallest_num_idx < middle_num_idx: # we need at least 2 nums range to check
            if nums[smallest_num_idx] + nums[middle_num_idx] > nums[largest_num_idx]: # check if we form a valid triangle with the current nums
                triplets_count += middle_num_idx - smallest_num_idx # every num in the range current smallest <=> current middle will also form a valid triplet with the current large num
                middle_num_idx -= 1 # move the middle num pointer one step left to check for other valid combinations in this range 
            else: # else the sum is not large enough, move the smallest num pointer one step right to increase it 
                smallest_num_idx += 1

        largest_num_idx -= 1

    return triplets_count


def validate_input(nums):
    if not isinstance(nums, list):
        raise TypeError("Input must be a list of integers.")
    if not all(isinstance(num, int) for num in nums):
        raise ValueError("All elements in nums must be integers.")
    if not (3 <= len(nums) <= 1000):
        raise ValueError("Array length must be between 3 and 1000.")
    if not all(0 <= num <= 1000 for num in nums):
        raise ValueError("All numbers must be between 0 and 1000.")


if __name__ == "__main__":
    print(solve([2, 2, 3, 4]))  # Expected: 3
    print(solve([4, 2, 3, 4]))  # Expected: 4