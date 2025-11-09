def solve(string):
    """
    Longest Substring Without Repeating Characters
    ----------------------------------------------
    Given a string `string`, find the length of the longest substring 
    without duplicate characters.

    Example 1:
        Input: string = "abcabcbb"
        Output: 3
        Explanation: The answer is "abc", with the length of 3. 
        Note that "bca" and "cab" are also valid answers.

    Example 2:
        Input: string = "bbbbb"
        Output: 1
        Explanation: The answer is "b".

    Example 3:
        Input: string = "pwwkew"
        Output: 3
        Explanation: The answer is "wke", with the length of 3.

    Constraints:
        0 <= s.length <= 5 * 10^4
        s consists of English letters, digits, symbols, and spaces.
    """
    validateInput(1, 5 * 10**4, len(string))

    seen = set()
    left = 0
    longest = 0

    for right, character in enumerate(string):
        while character in seen:
            seen.remove(string[left])
            left += 1

        seen.add(character)
        longest = max(longest, right - left + 1)

    return longest


def validateInput(min_length, max_length, length):
    if length < min_length or length > max_length:
        raise ValueError(f'The string length should be between {min_length} and {max_length}!')

if __name__ == "__main__":
    print(solve('abcabcbb'))  # Expected: 3
    print(solve('bbbbb'))     # Expected: 1
    print(solve('pwwkew'))    # Expected: 3
    print(solve("dvdf"))      # Expected: 3
