def solve(num):
    '''
    Palindrome Number
    -----------------
    Given an integer num, return true if num is a palindrome, and false otherwise.

    Example 1:
    Input: num = 121
    Output: true
    Explanation: 121 reads as 121 from left to right and from right to left.
    
    Example 2:
    Input: num = -121
    Output: false
    Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

    Example 3:
    Input: num = 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
    
    Constraints:
    -2^31 <= num <= 2^31 - 1

    Follow up: Could you solve it without converting the integer to a string?
    '''
    validateInput(-2**31, 2**31 - 1, num)

    if num < 0:
        return False
    
    if num < 10:
        return True

    reversed_half = 0
    while num > reversed_half:
        reversed_half = reversed_half * 10 +  num % 10
        num //= 10

    return reversed_half == num or reversed_half // 10 == num


def validateInput(min, max, num):
    if num < min or num > max:
        raise ValueError(f"{num} value should be between {min} and {max}!")
    
if __name__ == "__main__":
    print(solve(1221))   # Expected: True
    print(solve(121))    # Expected: True
    print(solve(12321))  # Expected: True
    print(solve(10))     # Expected: False
    print(solve(-121))   # Expected: False
    print(solve(0))      # Expected: True