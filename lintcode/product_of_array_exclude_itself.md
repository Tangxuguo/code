# product of array exclude itself
>http://www.lintcode.com/en/problem/product-of-array-exclude-itself/

暴力解法

    class Solution {
    public:
        /**
         * @param A: Given an integers array A
         * @return: A long long array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
         */
        vector<long long> productExcludeItself(vector<int> &nums) {
            // write your code here
            vector<long long> result(nums.size(), 1);
            for (int i = 0; i < nums.size(); i++) {
                for (int j = 0; j < nums.size(); j++) {
                    if (i != j) {
                        result[i] = result[i]*nums[j];
                    }
                }
            }
            return result;
        }
    };


分治算法，详细的解释可以参考(http://stackoverflow.com/questions/2680548/given-an-array-of-numbers-return-array-of-products-of-all-other-numbers-no-div)

    class Solution {
    public:
        /**
         * @param A: Given an integers array A
         * @return: A long long array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
         */
        vector<long long> productExcludeItself(vector<int> &nums) {
            // write your code here
            vector<long long> result(nums.size(), 1);
            long long p = 1;
            for (int i = 0; i < nums.size(); i++) {
                result[i] = p;
                p = p * nums[i];
            }

            p = 1;
            for (int i = nums.size()-1; i >= 0; i--) {
                result[i] *= p;
                p = p * nums[i];
            }

            return result;
        }
    };
