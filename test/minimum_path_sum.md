# minimum path sum
>  [http://www.lintcode.com/en/problem/minimum-path-sum](http://www.lintcode.com/en/problem/minimum-path-sum)

动态规划，关键找到边界，以及递推公式

    class Solution {
    public:
        /**
         * @param grid: a list of lists of integers.
         * @return: An integer, minimizes the sum of all numbers along its path
         */
        int minPathSum(vector<vector<int> > &grid) {
            // write your code here
            if (grid.size() == 0) return 0;
            int m = grid.size();
            int n = grid[0].size();
            vector<vector<int>> tab(m, vector<int>(n, 0));
            tab[0][0] = grid[0][0];

            for (int i = 1; i < m; i++) {
                tab[i][0] = tab[i-1][0] + grid[i][0];
            }
            for (int j = 1; j < n; j++) {
                tab[0][j] = tab[0][j-1] + grid[0][j];
            }
            for (int i = 1; i < m; i++) {
                for (int j = 1; j < n; j++) {
                    tab[i][j] = min(tab[i-1][j], tab[i][j-1]) + grid[i][j];
                }
            }
            return tab[m-1][n-1];
        }
    };
