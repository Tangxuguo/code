# palindrome partitioning
>http://www.lintcode.com/en/problem/palindrome-partitioning/

暴力搜索

DFS加回朔

    class Solution {
    public:
        /**
         * @param s: A string
         * @return: A list of lists of string
         */
        vector<vector<string>> partition(string s) {
            // write your code here
            vector<vector<string>> result;
            vector<string> output;
            DFS(s, result, 0, output);
            return result;
        }

        void DFS(string s, vector<vector<string>> &result, int start, vector<string> &output) {
            if (start == s.size()) {
                result.push_back(output);
                return;
            }
            string subString;
            for (int i = start; i < s.size(); i++) {
                subString.push_back(s[i]);
                if (isPalindrome(subString)) {
                    output.push_back(subString);
                    DFS(s, result, i+1, output);
                    output.pop_back();
                }
            }
        }

        bool isPalindrome(string subString) {
            for (int i = 0; i < subString.size()/2; i++) {
                if (subString[i] != subString[subString.size()-1-i]) {
                    return false;
                }
            }
            return true;
        }
    };
