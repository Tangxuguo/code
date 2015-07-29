# unique paths ii
>  [http://www.lintcode.com/en/problem/unique-paths-ii](http://www.lintcode.com/en/problem/unique-paths-ii)


首先初始化边界条件，入口，及左边第一列，上边第一行

然后动态规划，遇到障碍就清零，没有障碍就累加上面和左边的值


    class Solution {
    public:
        /**
         * @param obstacleGrid: A list of lists of integers
         * @return: An integer
         */
        int uniquePathsWithObstacles(vector<vector<int> > &obstacleGrid) {
            // write your code here
            if (obstacleGrid.size() == 0) return 0;
            int m = obstacleGrid.size();
            int n = obstacleGrid[0].size();
            vector<vector<int> > table(m, vector<int>(n, 1));
            if (obstacleGrid[0][0] == 1) {
                    table[0][0] = 0;
            } else {
                    table[0][0] = 1;
            }
            for (int i = 1; i < m; i++) {
                if (obstacleGrid[i][0] == 1) {
                    table[i][0] = 0;
                } else {
                    table[i][0] = table[i-1][0];
                }
            }
            for (int j = 1; j < n; j++) {
                if (obstacleGrid[0][j] == 1) {
                    table[0][j] = 0;
                } else {
                    table[0][j] = table[0][j-1];
                }
            }
            for (int i = 1; i < m; i++) {
                for (int j = 1; j < n; j++) {
                    if (obstacleGrid[i][j] == 1) {
                       table[i][j] = 0;
                    } else {
                        table[i][j] = table[i-1][j] + table[i][j-1];
                    }
                }
            }
            return table[m-1][n-1];
        }
    };

省内存的做法，按行扫描

    class Solution {
    public:
        /**
         * @param obstacleGrid: A list of lists of integers
         * @return: An integer
         */
        int uniquePathsWithObstacles(vector<vector<int> > &obstacleGrid) {
            // write your code here
            if (obstacleGrid.size() == 0) return 0;
            int m = obstacleGrid.size();
            int n = obstacleGrid[0].size();
            vector<int> res(n, 0);
            res[0] = 1;
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    if (obstacleGrid[i][j] == 1) {
                        res[j] = 0;
                    } else {
                        if (j > 0)
                            res[j] += res[j-1];
                    }
                }
            }
            return res[n-1];;
        }
    };
