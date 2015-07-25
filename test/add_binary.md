# add binary


和字符串相加类似，主要考虑进位

    class Solution {
    public:
        /**
         * @param a a number
         * @param b a number
         * @return the result
         */
        string addBinary(string& a, string& b) {
            // Write your code here
            int a_index = a.size() - 1;
            int b_index = b.size() - 1;
            int carry = 0;
            string result;

            while (a_index >= 0 || b_index >= 0 || carry > 0) {
                int a_val = a_index >= 0 ? a[a_index] - '0' : 0;
                int b_val = b_index >= 0 ? b[b_index] - '0' : 0;
                int adder = a_val + b_val + carry;
                carry = adder / 2;
                adder = adder % 2;
                result.push_back(adder + '0');
                a_index--;
                b_index--;
            }
            reverse(result.begin(), result.end());

            return result;
        }
    };
