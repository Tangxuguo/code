# reverse integer
>  [http://www.lintcode.com/en/problem/reverse-integer](http://www.lintcode.com/en/problem/reverse-integer)


针对正负做不同的处理，注意正负溢出值不一样

    class Solution {
    public:
        /**
         * @param n the integer to be reversed
         * @return the reversed integer
         */
        int reverseInteger(int n) {
            // Write your code here
            vector<int> digits;
            int result = 0;
            int tmp = 1;
            if (n >= 0) {
                while (n != 0) {
                    digits.push_back(n);
                    n = n/10;
                }
                for (int i = digits.size()-1; i >=0; i--) {

                    if (INT_MAX - result > digits[i]*tmp) {
                        result += digits[i]*tmp;
                    } else {
                        return 0;
                    }
                    if (tmp < INT_MAX/10) {
                        tmp = tmp*10;
                    } else {
                        return 0;
                    }
                }
                return result;
            } else {
                n = -n;
                while (n != 0) {
                    digits.push_back(n);
                    n = n/10;
                }
                for (int  i = digits.size()-1; i >=0; i--) {
                    if (INT_MIN  + digits[i]*tmp < result) {
                        result -= digits[i]*tmp;
                    } else {
                        return 0;
                    }
                    if (tmp < INT_MAX/10) {
                        tmp = tmp*10;
                    } else {
                        return 0;
                    }
                }
                return result;
            }
        }
    };

