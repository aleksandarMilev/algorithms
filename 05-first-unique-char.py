def solve(s):
    '''
    First Unique Character in a String
    ----------------------------------
    Given a string s, find the first non-repeating character in it 
    and return its index. If it doesn't exist, return -1.

    Example 1:
    Input: s = "leetcode"
    Output: 0
    Explanation: 'l' is the first non-repeating character.

    Example 2:
    Input: s = "loveleetcode"
    Output: 2
    Explanation: 'v' is the first non-repeating character.

    Example 3:
    Input: s = "aabb"
    Output: -1
    Explanation: No unique character.

    Constraints:
    1 <= len(s) <= 10^5
    s consists of only lowercase English letters.
    '''
    validate_input(s)

    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1

    for i, char in enumerate(s):
        if counts[char] == 1:
            return i

    return -1


def validate_input(s):
    if not isinstance(s, str):
        raise TypeError("Input must be a string.")
    if not s.islower():
        raise ValueError("String must contain only lowercase English letters.")
    if not (1 <= len(s) <= 10**5):
        raise ValueError("String length must be between 1 and 10^5.")


if __name__ == "__main__":
    print(solve("leetcode"))       # Expected: 0
    print(solve("loveleetcode"))   # Expected: 2
    print(solve("aabb"))           # Expected: -1
