# n queens

难点在于如何判断当前某一位置是否可以放皇后，需要通过之前所有放置过的皇后位置来判断。对已经放置的任意皇后，需要判断当前位置是否在同一行、列、对角线上这三个条件。


2. 行放置皇后：排除在同一行的可能。
2. 记录之前所放皇后的列坐标：col[i]=j表示第i行的皇后在第j列。这样在放置第i+1行时，只要保证col[i+1] != col[k], k=0...i 即可。
3. 对角线判断：对于任意(i1, col[i1])和(i2, col[i2])，只有当abs(i1-i2) = abs(col[i1]-col[i2])时，两皇后才在同一对角线。


    class Solution {
    public:
        /**
         * Get all distinct N-Queen solutions
         * @param n: The number of queens
         * @return: All distinct solutions
         * For example, A string '...Q' shows a queen on forth position
         */
        vector<vector<string> > solveNQueens(int n) {
            // write your code here
            vector<vector<string>> allSol;
            vector<string> sol;
            vector<int> col;
            solveNQ(n, 0, col, sol, allSol);
            return allSol;
        }
        void solveNQ(int n, int irow, vector<int> &col, vector<string> &sol, vector<vector<string>> &allSol) {
            if(irow==n) {
                allSol.push_back(sol);
                return;
            }

            for(int icol=0; icol<n; icol++) {
                if(validPos(col, irow, icol)) {
                    string s(n,'.');
                    s[icol] = 'Q';
                    sol.push_back(s);
                    col.push_back(icol);
                    solveNQ(n, irow+1, col, sol, allSol);
                    sol.pop_back();
                    col.pop_back();
                }
            }
        }
        bool validPos(vector<int> &col, int irow, int icol) {
            for(int i=0; i<col.size(); i++) {
                if(icol==col[i] || abs(irow-i)==abs(icol-col[i]))
                    return false;
            }
            return true;
        }
    };





http://www.cnblogs.com/TenosDoIt/p/3801621.html
http://bangbingsyb.blogspot.com/2014/11/leetcode-n-queens-i-ii.html
http://blog.csdn.net/hackbuteer1/article/details/6657109
