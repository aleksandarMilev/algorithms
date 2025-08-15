namespace Algorithms;

using System.Text;

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

    public static int RomanToInt(string romanian)
    {
        var romanianToArabicMap = new Dictionary<string, int>
        {
            { "I", 1 },
            { "V", 5 },
            { "X", 10 },
            { "L", 50 },
            { "C", 100 },
            { "D", 500 },
            { "M", 1_000 },
        };

        var result = new StringBuilder();


        return int.Parse(result.ToString());
    }
}
