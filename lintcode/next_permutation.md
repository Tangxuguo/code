# next permutation


不能直接找，
第一步找到乱序的
第二步找到哪一个比它大，互换位置
最后反转

    class Solution {
    public:
        /**
         * @param nums: An array of integers
         * @return: An array of integers that's next permuation
         */
        vector<int> nextPermutation(vector<int> &nums) {
            // write your code here
            int m = nums.size();
            int i = m-1;
            for (; i > 0; i--) {
                if (nums[i] > nums[i-1]) {
                    break;
                }
            }
            for (int j = m-1; j >= i; j--) {
                if (i == 0) break;
                if (nums[j] > nums[i-1]) {
                    int tmp = nums[j];
                    nums[j] = nums[i-1];
                    nums[i-1] = tmp;
                    break;
                }
            }
            for (int k = i; k <= (i+m-1)/2; k++) {
                int tmp = nums[k];
                nums[k] = nums[m-1 - (k-i)];
                nums[m-1 - (k-i)] = tmp;
            }
            return nums;
        }
    };
