# divide two integers

任何一个整数可以表示成以2的幂为底的一组基的线性组合，即num=a_0*2^0+a_1*2^1+a_2*2^2+...+a_n*2^n。基于以上这个公式以及左移一位相当于乘以2，我们先让除数左移直到大于被除数之前得到一个最大的基。然后接下来我们每次尝试减去这个基，如果可以则结果增加加2^k,然后基继续右移迭代，直到基为0为止。因为这个方法的迭代次数是按2的幂直到超过结果，所以时间复杂度为O(logn)

注意 abs取值前必须转为long long 型，防止溢出

    class Solution {
    public:
        /**
         * @param dividend the dividend
         * @param divisor the divisor
         * @return the result
         */
        int divide(int dividend, int divisor) {
            // Write your code here
            long long dividend_l = dividend;
            long long divisor_l = divisor;
            dividend_l = abs(dividend_l);
            divisor_l = abs(divisor_l);
            long long res = 0;
            while (dividend_l >= divisor_l) {
                long long t = divisor_l;
                for (int i = 1; dividend_l >= t; i <<= 1, t <<= 1) {
                    dividend_l -= t;
                    res += i;
                }
            }
            res = ((dividend < 0) ^ (divisor < 0)) ? -res : res;
            if (res > INT_MAX || res < INT_MIN) return INT_MAX;
            return  res;
        }
    };

http://blog.csdn.net/linhuanmars/article/details/20024907
http://blog.csdn.net/kenden23/article/details/16986763
