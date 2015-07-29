# invert binary tree
>  [http://www.lintcode.com/en/problem/invert-binary-tree](http://www.lintcode.com/en/problem/invert-binary-tree)


递归方法

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
         * @param root: a TreeNode, the root of the binary tree
         * @return: nothing
         */
        void invertBinaryTree(TreeNode *root) {
            // write your code here
            if (root->left == NULL && root->right == NULL) {
                return;
            }
            TreeNode *tmp = root->left;
            root->left = root->right;
            root->right = tmp;
            if (root->left != NULL) invertBinaryTree(root->left);
            if (root->right != NULL) invertBinaryTree(root->right);
        }
    };

非递归方法

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

利用栈先序遍历，对每一个节点都反转

    class Solution {
    public:
        /**
         * @param root: a TreeNode, the root of the binary tree
         * @return: nothing
         */
        void invertBinaryTree(TreeNode *root) {
            // write your code here
            stack<TreeNode*>tmp ;
            if(root != NULL) {
                tmp.push(root);
            }
            while(!tmp.empty()) {
                TreeNode* pNode = tmp.top();
                tmp.pop();
                if (pNode != NULL) {
                    TreeNode* tmpNode = pNode->left;
                    pNode->left = pNode->right;
                    pNode->right= tmpNode;

                    if (pNode->right!=NULL)
                        tmp.push(pNode->right);
                    if (pNode->left!=NULL)
                        tmp.push(pNode->left);
                }
            }
        }
    };
