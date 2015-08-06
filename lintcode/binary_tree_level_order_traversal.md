# binary tree level order traversal

这个和题minimum depth of binary tree类似

需要一个栈保存所有节点，针对每层加一个计数器

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
        /**
         * @param root: The root of binary tree.
         * @return: Level order a list of lists of integer
         */
    public:
        vector<vector<int>> levelOrder(TreeNode *root) {
            // write your code here
            vector<int> path;
            vector<vector<int>> res;
            if (root == NULL) return res;
            queue<TreeNode *> nodeQueue;
            nodeQueue.push(root);
            int currNum = 1; //num of nodes left in current level
            int nextNum = 0; //num of nodes in next level

            while (!nodeQueue.empty()) {
                TreeNode * pNode = nodeQueue.front();
                path.push_back(pNode->val);
                nodeQueue.pop();
                currNum--;
                if(pNode->left != NULL) {
                    nodeQueue.push(pNode->left);
                    nextNum++;
                }
                if(pNode->right != NULL) {
                    nodeQueue.push(pNode->right);
                    nextNum++;
                }
                if(currNum == 0) {
                    res.push_back(path);
                    path.clear();
                    currNum = nextNum;
                    nextNum = 0;
                }
            }
            return res;
        }
    };


