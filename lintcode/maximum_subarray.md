# maximum subarray
>http://www.lintcode.com/en/problem/maximum-subarray/

动态规划，和最小数组和一样

    class Solution {
    public:
        /**
         * @param nums: A list of integers
         * @return: A integer indicate the sum of max subarray
         */
        int maxSubArray(vector<int> nums) {
            // write your code here
            if (nums.size() == 0) return 0;
            int Sum = 0;
            int maxSum = nums[0];

            for (int i = 0; i < nums.size(); i++) {
                Sum += nums[i];
                maxSum = max(Sum, maxSum);
                if (Sum < 0) {
                    Sum = 0;
                }

            }

            return maxSum;
        }
    };
