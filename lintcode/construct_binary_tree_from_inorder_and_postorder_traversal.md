# construct binary tree from inorder and postorder traversal


根据中序序列和后序序列构造二叉树，后序的最后一个结点一定是根结点，该结点可以把中序序列分成左右两部分，对应于左右子树的中序序列，根据左右两部分中结点的个数又可以把后序序列中除去最后一个结点的序列分成两部分，对应于左右子树的后序序列，这样就可以递归构造左右子树。

1. 递归，注意退出条件，注意返回root
2. 算划分大小的时候，注意size，起止位置



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
         *@param inorder : A list of integers that inorder traversal of a tree
         *@param postorder : A list of integers that postorder traversal of a tree
         *@return : Root of a tree
         */
    public:
        TreeNode *buildTree(vector<int> &inorder, vector<int> &postorder) {
            // write your code here
            return buildTreeHelper(inorder, 0, inorder.size()-1, postorder, 0, postorder.size()-1);
        }
        TreeNode *buildTreeHelper(vector<int> &inorder, int s1, int e1, vector<int> &postorder, int s2, int e2) {
            if (s1 > e1 || s2 > e2) {
                return NULL;
            }
            int rootindex = -1;
            TreeNode * root = new TreeNode(postorder[e2]);
            for (int i = s1; i <= e1; i++) {
                if (inorder[i] == postorder[e2]){
                    rootindex = i;
                    break;
                }
            }
            if(rootindex==-1) return NULL;

            int leftsize = rootindex-1 -s1 +1;
            int rightsize = e1 - (rootindex+1) +1;
            root->left = buildTreeHelper(inorder, s1, rootindex-1, postorder, s2, s2 + leftsize-1);
            root->right = buildTreeHelper(inorder, rootindex+1, e1, postorder, e2-rightsize, e2-1);
            return root;
        }

    };


http://bangbingsyb.blogspot.com/2014/11/leetcode-construct-binary-tree-from_11.html
http://blog.csdn.net/zjull/article/details/11686973
