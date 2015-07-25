# unique paths
>http://www.lintcode.com/en/problem/unique-paths/

动态规划，注意边界，边界上只能从一个方向进入

    class Solution {
    public:
        /**
         * @param n, m: positive integer (1 <= n ,m <= 100)
         * @return an integer
         */
        int uniquePaths(int m, int n) {
            // wirte your code here
            vector<vector<int> > table(m, vector<int>(n, 1));
            for (int i = 1; i < m; i++) {
                for (int j = 1; j < n; j++) {
                    table[i][j] = table[i-1][j] + table[i][j-1];
                }
            }
            return table[m-1][n-1];
        }
    };

省空间的做法，按行扫描

    class Solution {
    public:
        /**
         * @param n, m: positive integer (1 <= n ,m <= 100)
         * @return an integer
         */
        int uniquePaths(int m, int n) {
            // wirte your code here
            vector<int> res(n, 0);
            res[0] = 1;
            for (int i = 0; i < m; i++) {
                for (int j = 1; j < n; j++) {
                    res[j] += res[j-1];
                }
            }
            return res[n-1];
        }
    };
