# binary tree zigzag level order traversal


记录当前所在的层数，如果是偶数则反转

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
         * @return: A list of lists of integer include
         *          the zigzag level order traversal of its nodes' values
         */
    public:
        vector<vector<int>> zigzagLevelOrder(TreeNode *root) {
            // write your code here
            vector<int> path;
            vector<vector<int>> res;
            if (root == NULL) return res;
            queue<TreeNode *> nodeQueue;
            nodeQueue.push(root);
            int currNum = 1; //num of nodes left in current level
            int nextNum = 0; //num of nodes in next level
            int level = 1;
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
                    if (level%2 == 0) {
                        reverse(path.begin(), path.end());
                    }
                    res.push_back(path);
                    path.clear();
                    currNum = nextNum;
                    nextNum = 0;
                    level++;
                }
            }
            return res;
        }
    };
