# maximal square

枚举就OK了，时间复杂度为O(n^3)



动态规划优化到O(n^2)。构造一个新的矩阵dp，dp[i][j]表示以点(i, j)为右下角的正方形的边长；状态转移方程：

    dp[i][j] = min(dp[i-1][j-1], min(dp[i-1][j], dp[i][j-1])) + 1;

对于题目所给的例子就有：

    1 0 1 0 0
    1 0 1 1 1
    1 1 1 1 1
    1 0 0 1 0

转化成：

    1 0 1 0 0
    1 0 1 1 1
    1 1 1 2 1
    1 0 0 1 0




    class Solution {
    public:
        /**
         * @param matrix: a matrix of 0 and 1
         * @return: an integer
         */
        int maxSquare(vector<vector<int> > &matrix) {
            // write your code here
            if (matrix.size() == 0) return 0;
            int maxLen = 0;
            int m = matrix.size();
            int n = matrix[0].size();
            vector<vector<int> > dp(m, vector<int>(n, 0));
            for (int i = 0; i < m; i++) {
                if (matrix[i][0] == 1) {
                        dp[i][0] = 1;
                        maxLen = max(maxLen, dp[i][0]);
                }
            }
            for (int j = 0; j < n; j++) {
                if (matrix[0][j] == 1) {
                        dp[0][j] = 1;
                        maxLen = max(maxLen, dp[0][j]);
                }
            }

            for (int i = 1; i < m; i++) {
                for (int j =1; j < n; j++) {
                    if (matrix[i][j] == 1) {
                        dp[i][j] = min(dp[i-1][j], min(dp[i][j-1], dp[i-1][j-1])) + 1;
                    } else {
                        dp[i][j] = 0;
                    }
                    maxLen = max(maxLen, dp[i][j]);
                }
            }
            return maxLen*maxLen;
        }
    };


http://www.cnblogs.com/easonliu/p/4548769.html
