# recover rotated sorted array
>http://www.lintcode.com/en/problem/recover-rotated-sorted-array/

三次翻转法，首先翻转前i个数，然后翻转后n-i个数，最后整体再翻转一次

    class Solution {
    public:
        void recoverRotatedSortedArray(vector<int> &nums) {
            // write your code here
            if (nums.size() <= 1) return;
            int i = 1;
            while (i < nums.size()) {
                if (nums[i] < nums[i-1]) {
                    break;
                }
                i++;
            }

            for (int j = 0; j <= (i-1)/2; j++) {
                int tmp = nums[j];
                nums[j] = nums[i-1-j];
                nums[i-1-j] = tmp;
            }

            for (int j = i; j <= (nums.size()-1+i)/2; j++) {
                int tmp = nums[j];
                nums[j] = nums[nums.size()-1-j+i];
                nums[nums.size()-1-j+i] = tmp;
            }

            for (int j = 0; j <= (nums.size()-1)/2; j++) {
                int tmp = nums[j];
                nums[j] = nums[nums.size()-1-j];
                nums[nums.size()-1-j] = tmp;
            }
        }
    };
