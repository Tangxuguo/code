# number of islands

种子填充算法，本质是DFS，需要对每个位置加一个访问标志位，注意是4方向连通

    class Solution {
    public:
        /**
         * @param grid a boolean 2D matrix
         * @return an integer
         */
        int numIslands(vector<vector<bool>>& grid) {
            // Write your code here
            if (grid.size() == 0) return 0;
            int result = 0;
            vector<vector<bool>> visited(grid.size(),vector<bool>(grid[0].size(),false));
            for (int i = 0; i < grid.size(); i++) {
                for (int j = 0; j < grid[0].size(); j++) {
                    if (grid[i][j] == true && visited[i][j] == false) {
                        result++;
                        DFS(grid,visited,i,j);
                    }
                }
            }
            return result;
        }

        void DFS(vector<vector<bool>>& grid, vector<vector<bool>>& visited, int i, int j) {
            if (i < 0 || i >= grid.size() || j < 0 && j >= grid[0].size() ) {
                return;
            }
            if (grid[i][j] == true && visited[i][j] == false) {
                visited[i][j] = true;
                DFS(grid,visited,i+1,j);
                DFS(grid,visited,i-1,j);
                DFS(grid,visited,i,j+1);
                DFS(grid,visited,i,j-1);

            }
        }
    };
