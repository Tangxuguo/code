# valid sudoku
>http://www.lintcode.com/en/problem/valid-sudoku/#

题目没有要求必须要有解，只要当前的各个block没有重复的就可以了，感觉题目有点乱，话说如果要有解又该怎么办呢？


    class Solution {
    public:
        /**
          * @param board: the board
          * @return: wether the Sudoku is valid
          */
        bool isValidSudoku(const vector<vector<char>>& board) {
            if (board.size() != 9 && board[0].size() != 9) return false;

            //check row
            for (int i = 0; i < 9; i++) {
                vector<bool> used(9, false);
                for (int j = 0; j < 9; j++) {
                    if(board[i][j] == '.') continue;
                    int k = board[i][j]-'0';
                    if (k == 0 || used[k-1]) return false;
                    used[k-1] = true;
                }
            }

            //check col
            for (int j = 0; j < 9; j++) {
                vector<bool> used(9, false);
                for (int i = 0; i < 9; i++) {
                    if(board[i][j] == '.') continue;
                    int k = board[i][j]-'0';
                    if (k == 0 || used[k-1]) return false;
                    used[k-1] = true;
                }
            }

            //check sub box 3*3
            for(int i=0; i<3; i++) {
                for(int j=0; j<3; j++) {
                    int row = 3*i;
                    int col = 3*j;
                    vector<bool> used(9,false);
                    for(int m=row; m<row+3; m++) {
                        for(int n=col; n<col+3; n++) {
                            if(board[m][n] == '.') continue;
                            int k = board[m][n]-'0';
                            if(k==0 || used[k-1]) return false;
                            used[k-1]=true;
                        }
                    }
                }
            }

            return true;

        }
    };
