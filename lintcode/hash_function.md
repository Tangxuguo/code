# hash function

>http://www.lintcode.com/en/problem/hash-function/#


用到了几个规律(http://www.bubuko.com/infodetail-622529.html)

(a + b) % p = (a % p + b % p) % p （1）
(a - b) % p = (a % p - b % p) % p （2）
(a * b) % p = (a % p * b % p) % p （3）
a ^ b % p = ((a % p)^b) % p （4）

应该还有一个（3）的变式
(a * b) % p = (a % p * b) % p （3）



    class Solution {
    public:
        /**
         * @param key: A String you should hash
         * @param HASH_SIZE: An integer
         * @return an integer
         */
        int hashCode(string key,int HASH_SIZE) {
            // write your code here
            long res = 0;
            for (int i = 0; i < key.size(); i++){
                res = 33 * res + (int)key[i];
                res = res % HASH_SIZE;
            }
            return (int)res;
        }
    };
