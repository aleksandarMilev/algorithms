namespace Algorithms;

public static class Solution
{
    public static bool IsPowerOfFour(int n)
    {
        if (n <= 0) return false;

        while (true)
        {
            if (n % 4 == 0) n /= 4;
            else break;
        }

        return n == 1;
    }
}
