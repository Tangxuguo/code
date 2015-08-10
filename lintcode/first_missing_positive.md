# first missing positive

快排 O(NlogN)

注意过滤重复元素，以及可能出现的负数


    class Solution {
    public:
        /**
         * @param A: a vector of integers
         * @return: an integer
         */
        int firstMissingPositive(vector<int> A) {
            // write your code here

            sort(A.begin(), A.end());
            int res = 1;
            int m = A.size();
            if (m == 0) return 1;
            for (int i = 0; i < m; i++) {
                if (A[i] <= 0) continue;
                if (A[i] > 0 ) {
                    if ( A[i] != res) return res;
                    res += 1;
                    while (A[i] == A[i+1]) i++;
                }

            }
            return res;
        }
    };

交换方法

交换数组元素，使得数组中第i位存放数值(i+1)。最后遍历数组，寻找第一个不符合此要求的元素，返回其下标。整个过程需要遍历两次数组，复杂度为O(n)。

    class Solution {
    public:
        /**
         * @param A: a vector of integers
         * @return: an integer
         */
        int firstMissingPositive(vector<int> A) {
            // write your code here
            int n = A.size();
            int i = 0;
            while (i < n)
            {
                if (A[i] != (i+1) && A[i] >= 1 && A[i] <= n && A[A[i]-1] != A[i])
                    swap(A[i], A[A[i]-1]);
                else
                    i++;
            }
            for (i = 0; i < n; ++i)
                if (A[i] != (i+1))
                    return i+1;
            return n+1;
        }
    };


http://www.cnblogs.com/AnnieKim/archive/2013/04/21/3034631.html
