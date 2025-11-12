def solve(s):
    '''
    Valid Parentheses
    -----------------
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
    determine if the input string is valid.

    A string is valid if:
    1. Open brackets are closed by the same type of brackets.
    2. Open brackets are closed in the correct order.
    3. Every closing bracket has a corresponding opening bracket.

    Example 1:
    Input: s = "()"
    Output: True

    Example 2:
    Input: s = "()[]{}"
    Output: True

    Example 3:
    Input: s = "(]"
    Output: False

    Example 4:
    Input: s = "([)]"
    Output: False

    Example 5:
    Input: s = "{[]}"
    Output: True

    Constraints:
    1 <= len(s) <= 10^4
    s consists only of parentheses characters: ()[]{}.
    '''
    def validateInput(s):
        if not isinstance(s, str):
            raise ValueError('s should be a string!')
        
        length = len(s)
        if length < 1 or length > 10**4:
            raise ValueError('s length should be between 1 and 10**4 characters long!')
        
        allowed = ['(', ')', '[', ']', '{', '}']
        for char in s:
            if char not in allowed:
                raise ValueError(f's should contain only {allowed} characters!')


    validateInput(s)

    def isOpening(char):
        return char in ['(', '[', '{',]
    
    length = len(s)
    if length == 0 or length % 2 != 0:
        return False
    
    parentheses_map = { '(': ')', '[': ']', '{': '}', }
    
    seen = []
    for char in s:
        if isOpening(char):
            seen.append(char)
        else:
            if not seen:
                return False
            if parentheses_map[seen.pop()] != char:
                return False

    return len(seen) == 0 

    
if __name__ == "__main__":
    print(solve("()"))         # Expected: True
    print(solve("()[]{}"))     # Expected: True
    print(solve("(]"))         # Expected: False
    print(solve("([)]"))       # Expected: False
    print(solve("{[]}"))       # Expected: True
