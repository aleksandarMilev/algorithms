namespace Algorithms;

public static class Solution
{
    public static bool IsPowerOfFour(int num)
    {
        if (num <= 0) return false;

        while (true)
        {
            if (num % 4 == 0) num /= 4;
            else break;
        }

        return num == 1;
    }

    public static int[] TwoSum(int[] nums, int target)
    {
        var map = new Dictionary<int, int>();

        for (var i = 0; i < nums.Length; i++)
        {
            var complement = target - nums[i];

            if (map.ContainsKey(complement)) return [map[complement], i];
            else map[nums[i]] = i;
        }

        throw new ArgumentException("No valid pair found!");
    }

    public static bool IsPalindrome(int num)
    {
        if (num < 0 || (num % 10 == 0 && num != 0)) return false;

        var reversedHalf = 0;

        while (num > reversedHalf)
        {
            reversedHalf = reversedHalf * 10 + num % 10;
            num /= 10;
        }

        return num == reversedHalf || num == reversedHalf / 10;
    }

    public static int RomanToInt(string roman)
    {
        var romanToArabicMap = new Dictionary<char, int>()
        {
            { 'I', 1 },
            { 'V', 5 },
            { 'X', 10 },
            { 'L', 50 },
            { 'C', 100 },
            { 'D', 500 },
            { 'M', 1000 },
        };

        var arabic = 0;

        for (var i = 0; i < roman.Length - 1; i++)
        {
            var current = roman[i];
            var next = roman[i + 1];

            if (romanToArabicMap[current] >= romanToArabicMap[next]) arabic += romanToArabicMap[current];
            else arabic -= romanToArabicMap[current];
        }

        var last = roman[^1];
        arabic += romanToArabicMap[last];

        return arabic;
    }

    public static string LongestCommonPrefix(string[] strs)
    {
        if (strs.Length == 0) return string.Empty;
        if (strs.All(string.IsNullOrWhiteSpace)) return string.Empty;
        if (strs.Length == 1) return strs[0];

        var shortest = strs.MinBy(s => s.Length)!;

        for (var i = 0; i < shortest.Length; i++)
        {
            var currentPrefixes = strs.Select(s => s[i]).ToHashSet();
            if (currentPrefixes.Count > 1) return shortest[..i];
        }

        return shortest;
    }

    public static bool IsValid(string parentheses)
    {
        if (parentheses.Length < 2) return false;

        var openingToClosed = new Dictionary<char, char>()
        {
            { '{', '}' },
            { '[', ']'},
            { '(', ')' }
        };

        var stack = new Stack<char>();

        for (var i = 0; i < parentheses.Length; i++)
        {
            var current = parentheses[i];

            if (openingToClosed.ContainsKey(parentheses[i])) 
                stack.Push(current);
            else
            {
                if (stack.Count == 0) 
                    return false;
                else
                {
                    var last = stack.Pop();
                    if (openingToClosed[last] != current)
                        return false;
                }

            }
        }

        return stack.Count == 0;
    }
}
