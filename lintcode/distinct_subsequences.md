# distinct subsequences

暴搜，超时

    class Solution {
    public:
        /**
         * @param S, T: Two string.
         * @return: Count the number of distinct subsequences
         */
        int numDistinct(string &S, string &T) {
            // write your code here
            int res = 0;
            string path;
            numDistinctHelper(res, path, 0, S, T);
            return res;
        }
        void numDistinctHelper(int &res, string &path, int pos, string &S, string &T) {
            if (path.size() == T.size()) {
                if (isequal(path, T)) {
                    res+=1;
                }
                return;
            }
            for (int i = pos; i < S.size(); i++) {
                path.push_back(S[i]);
                numDistinctHelper(res, path, i+1, S, T);
                path.pop_back();
            }
        }
        bool isequal(string &path, string &T) {
            for (int i = path.size()-1; i >= 0; i--) {
                if (path[i] != T[i]) return false;
            }
            return true;
        }
    };


动态规划：

设母串的长度为 i，
子串的长度为 j，我们要求的就是长度为 j 的子串在长度为 i 的母串中出现的次数，设dp[i][j]是从字符串S[0...i-1]中删除几个字符得到字符串T[0...j-1]的*不同的删除方法种类*，动态规划方程如下，若母串的最后一个字符与子串的最后一个字符不同，则长度为 j 的子串在长度为 i 的母串中出现的次数就是母串的前 i - 1 个字符中子串出现的次数，即 dp[i][j] = dp[i - 1][j ]，若母串的最后一个字符与子串的最后一个字符相同，那么除了前 i - 1 个字符出现字串的次数外，还要加上子串的前 j - 1 个字符在母串的前 i - 1 个字符中出现的次数，即 dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]。




+ 如果S[i-1] = T[j-1],dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
+ 如果S[i-1] 不等于 T[j-1], dp[i][j] = dp[i-1][j]
+ 初始条件：当T为空字符串时，从任意的S删除几个字符得到T的方法为1

注意，开辟数组大小,数组长度要大一，考虑到空串
初始化
递归判断条件



    class Solution {
    public:
        /**
         * @param S, T: Two string.
         * @return: Count the number of distinct subsequences
         */
        int numDistinct(string &S, string &T) {
            // write your code here
            if (S.size() < T.size()) return 0;
            vector<vector<int>> dp(S.size()+1, vector<int>(T.size()+1, 0));
            dp[0][0] = 1;
            for (int i = 1; i <= S.size(); i++) { //T is empty
                dp[i][0] = 1;
            }
            for (int j = 1; j <= T.size(); j++) { //S is empty
                dp[0][j] = 0;
            }
            for (int i = 1; i <= S.size(); i++) {
                for (int j = 1; j <= T.size(); j++) {
                    if (S[i-1] == T[j-1]) {
                        dp[i][j] = dp[i-1][j-1] + dp[i-1][j];
                    } else {
                        dp[i][j] = dp[i-1][j];
                    }
                }
            }
            return dp[S.size()][T.size()];
        }

    };

滚动数组，O(N)空间

    class Solution {
    public:
        /**
         * @param S, T: Two string.
         * @return: Count the number of distinct subsequences
         */
        int numDistinct(string &S, string &T) {
            // write your code here
            int match[200];
            if(S.size() < T.size()) return 0;
            match[0] = 1;
            for(int i=1; i <= T.size(); i++)
                match[i] = 0;
            for(int i=1; i<= S.size(); i ++)
                for(int j =T.size(); j>=1; j--)
                  if(S[i-1] == T[j-1])
                    match[j]+= match[j-1];
            return match[T.size()];
        }

    };




http://www.cnblogs.com/TenosDoIt/p/3440022.html
http://blog.csdn.net/abcbc/article/details/8978146
http://fisherlei.blogspot.com/2012/12/leetcode-distinct-subsequences_19.html
