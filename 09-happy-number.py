def solve(num):
    '''
    Happy Number
    ------------
    Write an algorithm to determine if a number num is a happy number.

    A happy number is defined by this process:
    - Starting with any positive integer, replace it with the sum of the squares of its digits.
    - Repeat the process until the number equals 1 (where it stays),
      or it loops endlessly in a cycle which does not include 1.
    - A number for which this process ends in 1 is a happy number.

    Example 1:
    Input: num = 19
    Output: True
    Explanation:
        1² + 9² = 82
        8² + 2² = 68
        6² + 8² = 100
        1² + 0² + 0² = 1

    Example 2:
    Input: num = 2
    Output: False

    Constraints:
    1 <= num <= 2^31 - 1
    '''
    validate_input(num)

    digits_sum = 0 # current sum
    sums = set() # set to keep the unique sums

    while num != 1: # loop while the number is not 1
        toStr = str(num) # parse to string for more straightforward enumeration
        for digit in toStr: # loop through each digit
            digits_sum += int(digit)**2 # add the square of the current digit to the total sum

        if digits_sum == 1: # if this is True, the number is happy, so we break and return true
            break

        if digits_sum in sums: # If the sum is not 1 and it already exists after processing the current num, we have a cycle, so we break and return False
            break
        else:
            sums.add(digits_sum) # else, add the current sum in the set

        num = digits_sum # the number is now equal to the current sum
        digits_sum = 0 # reset the sum

    return digits_sum == 1 # return True if the number is happy, otherwise return False

def validate_input(num):
    if not isinstance(num, int):
        raise TypeError("Input must be an integer.")
    if not (1 <= num <= 2**31 - 1):
        raise ValueError("Number must be between 1 and 2^31 - 1.")


if __name__ == "__main__":
    print(solve(19))  # Expected: True
    print(solve(2))   # Expected: False