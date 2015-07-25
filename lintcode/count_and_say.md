# count and say
>http://www.lintcode.com/zh-cn/problem/count-and-say/#

主要包括两个步骤，统计字符串中重复的字符，然后把统计数字转为字符串，最后记得要把最后的计算值加入

    class Solution {
    public:
        /**
         * @param n the nth
         * @return the nth sequence
         */
        string countAndSay(int n) {
            // Write your code here
            string result;
            result.push_back('1');

            for (int i = 1; i < n; i++) {
                string tmp;
                int counter = 1;
                int j = 1;
                for (; j < result.size(); j++) {
                    if (result[j-1] == result[j]) {
                        counter++;
                    } else {
                        string counter_str;
                        while (counter != 0) {
                            counter_str.push_back(counter + '0');
                            counter = counter/10;
                        }
                        reverse(counter_str.begin(), counter_str.end());
                        tmp = tmp + counter_str + result[j-1];
                        counter = 1;
                    }
                }
                string counter_str;
                while (counter != 0) {
                    counter_str.push_back(counter + '0');
                    counter = counter/10;
                }
                reverse(counter_str.begin(), counter_str.end());
                tmp = tmp + counter_str + result[j-1];
                result = tmp;
            }
            return result;
        }
    };

