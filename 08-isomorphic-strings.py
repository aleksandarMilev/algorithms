def solve(s, t):
    '''
    Isomorphic Strings
    ------------------
    Given two strings s and t, determine if they are isomorphic.

    Two strings are isomorphic if the characters in s can be replaced to get t.
    - Each character in s must map to exactly one character in t.
    - No two characters in s may map to the same character in t.

    Example 1:
    Input: s = "egg", t = "add"
    Output: True
    Explanation: e -> a, g -> d

    Example 2:
    Input: s = "foo", t = "bar"
    Output: False

    Example 3:
    Input: s = "paper", t = "title"
    Output: True

    Example 4:
    Input: s = "ab", t = "aa"
    Output: False

    Constraints:
    - 1 <= len(s), len(t) <= 5 * 10^4
    - s and t consist of any printable ASCII characters.
    '''
    validate_input(s, t)

    s_to_t = {}
    t_to_s = {}

    for i, s_char in enumerate(s):
        if s_char in s_to_t:
            if s_to_t[s_char] != t[i]:
                return False
        elif t[i] in t_to_s:
            if t_to_s[t[i]] != s_char:
                return False
        else:
            s_to_t[s_char] = t[i]
            t_to_s[t[i]] = s_char

    return True


def validate_input(s, t):
    if not isinstance(s, str) or not isinstance(t, str):
        raise TypeError("Both inputs must be strings.")
    if len(s) != len(t):
        raise ValueError("Strings must be of the same length.")
    if not (1 <= len(s) <= 5 * 10**4):
        raise ValueError("String length must be between 1 and 5 * 10^4.")


if __name__ == "__main__":
    print(solve('egg', 'add'))          # Expected: True
    print(solve('foo', 'bar'))          # Expected: False
    print(solve('paper', 'title'))      # Expected: True
    print(solve('ab', 'aa'))            # Expected: False
