# longest increasing continuous subsequence
>http://www.lintcode.com/en/problem/longest-increasing-continuous-subsequence/

定义一个计算器，分别统计上升和下降序列

    class Solution {
    public:
        /**
         * @param A an array of Integer
         * @return  an integer
         */
        int longestIncreasingContinuousSubsequence(vector<int>& A) {
            // Write your code here
            int counter1 = 1;
            int counter2 = 1;
            if (A.size() == 0) return 0;
            int max = 1;
            for (int i = 1; i < A.size(); i++) {
                if (A[i-1] < A[i]) {
                    counter1++;
                    max = counter1 > max ? counter1:max;
                } else {
                    counter1 = 1;
                }
            }
            for (int i = 1; i < A.size(); i++) {
                if (A[i-1] > A[i]) {
                    counter2++;
                    max = counter2 > max ? counter2:max;
                } else {
                    counter2 = 1;
                }
            }

            return max;
        }
    };
