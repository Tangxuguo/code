# space replacement
>http://www.lintcode.com/en/problem/space-replacement/

注意每1个空格增加2个字符，不是3个

    class Solution {
    public:
        /**
         * @param string: An array of Char
         * @param length: The true length of the string
         * @return: The true length of new string
         */
        int replaceBlank(char string[], int length) {
            // Write your code here
            int blankCounter = 0;
            for (int i = 0; i < length; i++) {
                if (string[i] == ' ') {
                    blankCounter++;
                }
            }
            int j = length + blankCounter*2-1;
            for (int i = length-1; i >= 0; i--) {
                if (string[i] == ' ') {
                    string[j-2] = '%';
                    string[j-1] = '2';
                    string[j] = '0';
                    j-=3;
                } else {
                    string[j] = string[i];
                    j-=1;
                }
            }
            return length + blankCounter*2;
        }
    };

