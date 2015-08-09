# unique binary search trees


[提供的递归方法](http://blog.csdn.net/zjull/article/details/11711835)，会超时

    class Solution {
    public:
        /**
         * @paramn n: An integer
         * @return: An integer
         */
        int numTrees(int n) {
            // write your code here
            return numTrees(1,n);
        }
        int numTrees(int start, int end)
        {
            if (start >= end)
                return 1;

            int totalNum = 0;
            for (int i=start; i<=end; ++i)
                totalNum += numTrees(start,i-1)*numTrees(i+1,end);
            return totalNum;
        }
    };

非递归的

定义Count[i] 为以[0,i]能产生的Unique Binary Tree的数目，

如果数组为空，毫无疑问，只有一种BST，即空树，

    Count[0] =1
如果数组仅有一个元素{1}，只有一种BST，单个节点

    Count[1] = 1

如果数组有两个元素{1,2}， 那么有如下两种可能

    Count[2] = Count[0] * Count[1]   (1为根的情况)
            + Count[1] * Count[0]  (2为根的情况。

再看一遍三个元素的数组，可以发现BST的取值方式如下：

    Count[3] = Count[0]*Count[2]  (1为根的情况)
               + Count[1]*Count[1]  (2为根的情况)
               + Count[2]*Count[0]  (3为根的情况)

所以，由此观察，可以得出Count的递推公式为

    Count[n+1] = ∑ Count[i] * [ n-i]     0<=i<=n
问题至此划归为一维动态规划

    class Solution {
    public:
        /**
         * @paramn n: An integer
         * @return: An integer
         */
        int numTrees(int n) {
            // write your code here
            vector<int> res(n+1,0);
            res[0] = 1;
            res[1] = 1;
            for(int i=2;i<=n;i++)
            {
                for(int j=0;j<i;j++)
                {
                    res[i] += res[j]*res[i-1-j];
                }
            }
            return res[n];
        }
    };


http://blog.csdn.net/linhuanmars/article/details/24761459
http://fisherlei.blogspot.com/2013/03/leetcode-unique-binary-search-trees.html
