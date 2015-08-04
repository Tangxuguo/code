# best time to buy and sell stock


O(N2)超时不通过

    class Solution {
    public:
        /**
         * @param prices: Given an integer array
         * @return: Maximum profit
         */
        int maxProfit(vector<int> &prices) {
            // write your code here
            int res = 0;
            int m = prices.size();
            for (int i = 0; i < m; i++) {
                for (int j = i+1; j < m; j++) {
                    res = max(res,prices[j]-prices[i]);
                }
            }
            return res;
        }
    };

O(N)

    class Solution {
    public:
        /**
         * @param prices: Given an integer array
         * @return: Maximum profit
         */
        int maxProfit(vector<int> &prices) {
            // write your code here
            int res = 0;
            int start = 0;
            int m = prices.size();
            for (int i = 1; i < m; i++) {
                res = max(res,prices[i] - prices[start]);
                if ((prices[i] - prices[start]) < 0) {
                    start = i;
                }
            }
            return res;
        }
    };

