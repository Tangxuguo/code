# n queens ii

和N皇后一样的解法

    class Solution {
    public:
        /**
         * Calculate the total number of distinct N-Queen solutions.
         * @param n: The number of queens.
         * @return: The total number of distinct solutions.
         */
        int totalNQueens(int n) {
            // write your code here
            vector<vector<string>> allsol;
            vector<string> sol;
            vector<int> col;
            solveNQ(n, 0, allsol, sol, col);
            return allsol.size();
        }
        void solveNQ(int n, int irow, vector<vector<string>> &allsol, vector<string> &sol, vector<int> &col) {
            if (irow == n) {
                allsol.push_back(sol);
                return;
            }
            for (int icol = 0; icol < n; icol++) {
                if (validpos(col, icol, irow)) {
                    string s(n, '.');
                    s[icol] = 'Q';
                    col.push_back(icol);
                    sol.push_back(s);
                    solveNQ(n, irow+1, allsol, sol, col);
                    col.pop_back();
                    sol.pop_back();
                }
            }
        }
        bool validpos(vector<int> col, int icol, int irow) {
            for (int i = 0; i < col.size(); i++) {
                if (col[i] == icol || abs(irow-i) == abs(icol-col[i]))
                    return false;
            }
            return true;
        }
    };

