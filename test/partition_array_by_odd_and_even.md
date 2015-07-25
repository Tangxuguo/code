# partition array by odd and even


只要两个根指针，奇数不动，left指针往前移，偶数的话，把偶数移到最后一个，right--，当两根指针相遇时停止

    class Solution {
    public:
        /**
         * @param nums: a vector of integers
         * @return: nothing
         */
        void partitionArray(vector<int> &nums) {
            // write your code here
            if (nums.size() <= 1) return;
            int right = nums.size()-1;
            for (int left = 0; left < right; ) {
                if (nums[left]%2 == 0) {
                    int tmp = nums[left];
                    nums[left] = nums[right];
                    nums[right] = tmp;
                    right--;
                } else {
                    left++;
                }
            }
        }
    };
