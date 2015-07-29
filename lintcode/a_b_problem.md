# a b problem

位运算实现整数加法本质就是用二进制进行运算。

其主要用了两个基本表达式：

    x^y //执行加法，不考虑进位。相同为0不同为1
    (x&y)<<1 //进位操作，处理进位
    令x=x^y ；y=(x&y)<<1

进行迭代，每迭代一次进位操作右面就多一位0，最多需要“加数二进制位长度”次迭代就没有进位了，此时x^y的值就是结果。

我们来做个3位数的加法：

    101+011=1000 //正常加法
    位运算加法：
    （1） 101 ^ 011 = 110 相加，不考虑进位
    (101 & 011) 统计需要进位的地方
    (101 & 011)<<1 = 010 向前进位
    （2） 110 ^ 010 = 100 加上需要进位的
    (110 & 010)<<1 = 100 统计这次需要进位的
    （3） 100 ^ 100 = 000
    (100 & 100)<<1 = 1000
此时进行相加操作就没有进位了，即000 ^ 1000=1000即是最后结果。

    class Solution {
    public:
        /*
         * @param a: The first integer
         * @param b: The second integer
         * @return: The sum of a and b
         */
        int aplusb(int a, int b) {
            // write your code here, try to do it without arithmetic operators.
            while (b != 0) {
                int carry = a & b;
                a ^= b;
                b = carry << 1;
            }
            return a;
        }
    };




https://github.com/kamyu104/LintCode/blob/master/C++/a-b-problem.cpp
