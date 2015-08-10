# 3 sum closest


和3sum，一样

坑，是返回的是三个数之和，不是最小差

    class Solution {
    public:
        /**
         * @param numbers: Give an array numbers of n integer
         * @param target: An integer
         * @return: return the sum of the three integers, the sum closest target.
         */
        int threeSumClosest(vector<int> nums, int target) {
            // write your code here
            sort(nums.begin(), nums.end());

            int m = nums.size();
            int res = nums[0] + nums[1] + nums[2];
            for (int i = 0; i < nums.size();) {
                twosum(res, i, nums, target-nums[i]);
                i++;
                while (i < m && nums[i] == nums[i-1]) i++;
            }
            return res;
        }
        void twosum(int &res, int i, vector<int> &nums, int target) {
            int m = nums.size();
            int left = i+1;
            int right = m-1;
            while (left < right) {
                res = abs(nums[left] + nums[right] - target) < abs(res-target-nums[i]) ? (nums[left] + nums[right] + nums[i]):res;
                if (nums[left] + nums[right] > target) {
                    right--;
                } else {
                    left++;
                }
            }
        }
    };

http://blog.csdn.net/linhuanmars/article/details/19712011
