# fibonacci
>  [http://www.lintcode.com/en/problem/fibonacci](http://www.lintcode.com/en/problem/fibonacci)

动态规划，找递推公式

    class Solution{
    public:
        /**
         * @param n: an integer
         * @return an integer f(n)
         */
        int fibonacci(int n) {
            // write your code here
            int a[3];
            a[0] = 0;
            a[1] = 1;
            if (n < 1) {
                return -1;
            }
            if (n <= 2) {
                return a[n-1];
            }
            for (int i=3; i <= n; i++) {
                a[2] = a[0] + a[1];
                a[0] = a[1];
                a[1] = a[2];
            }

            return a[2];
        }
    };


