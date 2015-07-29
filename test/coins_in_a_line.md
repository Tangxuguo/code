# coins in a line
>  [http://www.lintcode.com/en/problem/coins-in-a-line](http://www.lintcode.com/en/problem/coins-in-a-line)

找规律，其实不是3的倍数就可以了，每轮拿的硬币和为3

    class Solution {
    public:
        /**
         * @param n: an integer
         * @return: a boolean which equals to true if the first player will win
         */
         bool firstWillWin(int n) {
            // write your code here
            if (n % 3 == 0) {
                return false;
            } else {
                return true;
            }
        }
    };
