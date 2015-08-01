# permutation index


第一种解法，DFS & 回朔法，排列问题
递归遍历所有可能，然后累加计算，直至到K为止。


注意：排列问题要记住所有已经访问过的点，当所有点都被访问过后可以退出

代码没有通过，超时了


    	class Solution {
    public:
        /**
         * @param A an integer array
         * @return a long integer
         */
        long long permutationIndex(vector<int>& A) {
            // Write your code here
            if (A.size() == 0) {
                return 0;
            }
            long long counter = 0;
            long long res = 0;
            vector<int> sortA = A;
            sort(sortA.begin(), sortA.end());
            vector<int> path;
            vector<int> visited(sortA.size(), 0);
            permuteHelper(counter,res, path, visited, 0, sortA, A);
            return res;
        }
        void permuteHelper(long long &counter, long long &res, vector<int> &path, vector<int> &visited, int pos, vector<int> &sortA, vector<int> & A) {
            if ( path.size() == sortA.size() ) {
                counter++;
                if (arrayEqual(path, A)) {
                    res = counter;
                    return;
                }
            }
            for (int i = 0; i< sortA.size(); i++) {
                if (visited[i] == 0) {
                    visited[i] = 1;
                    path.push_back(sortA[i]);
                    permuteHelper(counter, res, path, visited, i+1, sortA, A);
                    path.pop_back();
                    visited[i] = 0;
                }
            }
        }

        bool arrayEqual(vector<int> &path, vector<int> &A) {
            int m = A.size();
            for (int i = 0; i < m; i++) {
                if (path[i] != A[i]) return false;
            }
            return true;
        }
    };

第二种方法，数学解法。

递归，
例如：
2，1，4
先排序
1，2，4

计算[1,2,4]中比[2，1，4]的pos 0 即2小的个数i，乘以fac(m-1),
选定这个数开始，即在排序列表中删掉这个数，
重新递归，直到数列为空

    class Solution {
    public:
        /**
         * @param A an integer array
         * @return a long integer
         */
        long long permutationIndex(vector<int>& A) {
            // Write your code here
            if (A.size() == 0) {
                return 0;
            }
            long long counter = 1;
            vector<int> sortA = A;
            sort(sortA.begin(), sortA.end());
            int pos = 0;
            permuteHelper(counter, pos, sortA, A);
            return counter;
        }
        void permuteHelper(long long &counter, int pos, vector<int> & sortA, vector<int> & A) {
            int m = sortA.size();
            if (m == 0 || pos == A.size()-1) return;
            for (int i = 0; i < m; i++) {
                if (sortA[i] == A[pos]) {
                    counter += i * fac(m-1);
                    sortA.erase(sortA.begin()+i);
                    break;
                }
            }
            permuteHelper(counter, pos + 1, sortA, A);
        }

        long long fac(int  n ) {
            long long  res = 1;
            for (int  i = 1; i <= n; i++) {
                res *=i;
            }
            return res;
        }
    };




http://fisherlei.blogspot.com/2013/04/leetcode-permutation-sequence-solution.html
