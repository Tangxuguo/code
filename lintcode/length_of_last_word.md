# length of last word
>http://www.lintcode.com/en/problem/length-of-last-word/

从后面数，去掉空格

    class Solution {
    public:
        /**
         * @param s A string
         * @return the length of last word
         */
        int lengthOfLastWord(string& s) {
            // Write your code here
            int index = s.size()-1;
            int result = 0;

            while (index >=0 && s[index] == ' ') index--;
            if (index < 0) return 0;
            while (index >=0 && s[index] != ' ') {
                result++;
                index--;
            }
            return result;
        }
    };
