# valid parentheses
>http://www.lintcode.com/en/problem/valid-parentheses/#


要注意的地方是不能对空栈调用top方法，负载会溢出

    class Solution {
    public:
        /**
         * @param s A string
         * @return whether the string is a valid parentheses
         */
        bool isValidParentheses(string& s) {
            // Write your code here
            stack<char> res;
            for (int i = 0; i < s.size(); i++) {
                if (!res.empty()) {
                    if ((res.top() == '(' && s[i] == ')')
                        || (res.top() == '{' && s[i] == '}')
                        || (res.top() == '[' && s[i] == ']') ) {

                        res.pop();
                    } else {
                    res.push(s[i]);
                    }
                } else {
                    res.push(s[i]);
                }
            }
            if (res.empty()) {
                return true;
            }

            return false;
        }
    };

