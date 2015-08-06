# best time to buy and sell stock ii


相邻相减大于0，则累加

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
            for (int i = 1; i < m; i++) {
                if ((prices[i] - prices[i-1]) > 0) {
                    res += prices[i] - prices[i-1];
                }
            }
            return res;
        }
    };
