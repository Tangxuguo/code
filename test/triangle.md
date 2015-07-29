# triangle
>  [http://www.lintcode.com/en/problem/triangle](http://www.lintcode.com/en/problem/triangle)

动态规划，按行扫描，注意边界，第一个和最后一个，注意扫描顺序，从后往前扫，不然取得值是本轮的值，扫完最后一行，求个最小值

    class Solution {
    public:
        /**
         * @param triangle: a list of lists of integers.
         * @return: An integer, minimum path sum.
         */
        int minimumTotal(vector<vector<int> > &triangle) {
            // write your code here
            int m = triangle.size();
            if (m == 0) return 0;
            vector<int> res(m, 0);
            res[0] = triangle[0][0];

            for (int i = 1; i < m; i++) {
                for (int j = i; j >= 0; j--) {
                    if (j == 0) {
                        res[0] = res[0] + triangle[i][0];
                    } else if (j == i) {
                        res[j] = res[j-1] + triangle[i][i];
                    } else {
                        res[j] = min(res[j-1], res[j]) + triangle[i][j];
                    }
                }
            }

            int minSum = res[0];
            for (int i = 0; i < res.size(); i++) {
                minSum = min(res[i], minSum);
            }
            return minSum;
        }
    };

