# subtree
>  [http://www.lintcode.com/en/problem/subtree](http://www.lintcode.com/en/problem/subtree)

首先是特殊情况的处理，然后是树的遍历，可以用栈或者递归，对于判断两个树是否相等，用递归的方式，用栈的话需要同时入出栈，比较麻烦


    /**
     * Definition of TreeNode:
     * class TreeNode {
     * public:
     *     int val;
     *     TreeNode *left, *right;
     *     TreeNode(int val) {
     *         this->val = val;
     *         this->left = this->right = NULL;
     *     }
     * }
     */
    class Solution {
    public:
        /**
         * @param T1, T2: The roots of binary tree.
         * @return: True if T2 is a subtree of T1, or false.
         */
        bool isSubtree(TreeNode *T1, TreeNode *T2) {
            // write your code here
            if (!T2) {
                return true;
            } else if (!T1) {  // !T1 && T2
                return false;
            }
            stack<TreeNode*> tmp;
            tmp.push(T1);
            while(!tmp.empty()) {
                TreeNode* pNode = tmp.top();
                if(isSubtreeHelper(pNode, T2))
                    return true;
                tmp.pop();
                if(pNode->right)
                    tmp.push(pNode->right);
                if(pNode->left)
                    tmp.push(pNode->left);
            }
            return false;
        }
        bool isSubtreeHelper(TreeNode *T1, TreeNode *T2) {
            if (!T1 && !T2) {
                return true;
            }
            if (T1 && T2) {
                return T1->val == T2->val &&
                       isSubtreeHelper(T1->left, T2->left) &&
                       isSubtreeHelper(T1->right, T2->right);
            }

            return false;
        }

    };

全部递归的方式

    /**
     * Definition of TreeNode:
     * class TreeNode {
     * public:
     *     int val;
     *     TreeNode *left, *right;
     *     TreeNode(int val) {
     *         this->val = val;
     *         this->left = this->right = NULL;
     *     }
     * }
     */
    class Solution {
    public:
        /**
         * @param T1, T2: The roots of binary tree.
         * @return: True if T2 is a subtree of T1, or false.
         */
        bool isSubtree(TreeNode *T1, TreeNode *T2) {
            // write your code here
            if (!T2) {
                return true;
            } else if (!T1) {  // !T1 && T2
                return false;
            }
            return isSameTree(T1, T2) ||
                       isSubtree(T1->left, T2) ||
                       isSubtree(T1->right, T2);
        }
        bool isSameTree(TreeNode *T1, TreeNode *T2) {
            if (!T1 && !T2) {
                return true;
            }
            if (T1 && T2) {
                return T1->val == T2->val &&
                       isSameTree(T1->left, T2->left) &&
                       isSameTree(T1->right, T2->right);
            }

            return false;
        }

    };

