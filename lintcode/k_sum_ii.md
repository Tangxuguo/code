# k sum ii



DFS 暴搜，注意是顺序无关

    class Solution {
    public:
        /**
         * @param A: an integer array.
         * @param k: a positive integer (k <= length(A))
         * @param target: a integer
         * @return a list of lists of integer
         */
        vector<vector<int> > kSumII(vector<int> A, int k, int target) {
            // write your code here
            vector<vector<int> > result;
            vector<int> path;
            int pos = 0;
            DFS(result, A, path, pos, k, target);
            return result;
        }
        void DFS(vector<vector<int> > & result, vector<int> A, vector<int> &path, int pos, int k, int target) {
            if (path.size() == k) {
                if (accumulate(path.begin(), path.end(), 0) == target) {
                    result.push_back(path);
                }
                return;
            }
            int m = A.size();
            for (int i = pos; i < m; i++) {
                path.push_back(A[i]);
                DFS(result, A, path, i+1, k, target);
                path.pop_back();

            }
        }
    };

