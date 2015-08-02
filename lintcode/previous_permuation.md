# previous permuation


不能直接找，第一步找到乱序的，然后找到哪一个比它大，移到合适的位置，最后反转


    class Solution {
    public:
        /**
         * @param nums: An array of integers
         * @return: An array of integers that's previous permuation
         */
        vector<int> previousPermuation(vector<int> &nums) {
            if (nums.empty() || nums.size() <= 1) {
                return nums;
            }
            // step1: find nums[i] > nums[i + 1]
            int i = 0;
            for (i = nums.size() - 2; i >= 0; --i) {
                if (nums[i] > nums[i + 1]) {
                    break;
                } else if (0 == i) {
                    // reverse nums if reach minimum
                    reverse(nums, 0, nums.size() - 1);
                    return nums;
                }
            }
            // step2: find nums[i] > nums[j]
            int j = 0;
            for (j = nums.size() - 1; j > i; --j) {
                if (nums[i] > nums[j]) break;
            }
            // step3: swap betwenn nums[i] and nums[j]
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
            // step4: reverse between [i + 1, n - 1]
            reverse(nums, i + 1, nums.size() - 1);

            return nums;
        }

    private:
        void reverse(vector<int>& nums, int start, int end) {
            for (int i = start, j = end; i < j; ++i, --j) {
                int temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
            }
        }
    };


http://algorithm.yuanbin.me/exhaustive_search/previous_permuation.html
