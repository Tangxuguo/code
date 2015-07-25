# valid palindrome
>http://www.lintcode.com/en/problem/valid-palindrome/

用两个指针过滤无关字符，把字符统一转换成小写字符

    class Solution {
    public:
        /**
         * @param s A string
         * @return Whether the string is a valid palindrome
         */
        bool isPalindrome(string& s) {
            // Write your code here
            int i = 0;
            int j = s.size()-1;
            while (i < j) {
                if (!( isalpha(s[i]) || isdigit(s[i]) )) {
                    i++;
                    continue;
                }
                if (!( isalpha(s[j]) || isdigit(s[j]) )) {
                    j--;
                    continue;
                }
                if (tolower(s[i]) == tolower(s[j])) {
                    i++;
                    j--;
                } else {
                    return false;
                }
            }
            return true;
        }
    };

