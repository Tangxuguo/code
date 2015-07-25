# convert sorted array to binary search tree with minimal height

>http://www.lintcode.com/en/problem/convert-sorted-array-to-binary-search-tree-with-minimal-height/


二分法，递归，注意是指针，如果函数传参处理起来比较麻烦，直接传的话，函数调用完后就释放了，这里采用返回值的方式

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
         * @param A: A sorted (increasing order) array
         * @return: A tree node
         */
        TreeNode *sortedArrayToBST(vector<int> &A) {
            // write your code here
            TreeNode * root;
            if (A.size() == 0) return NULL;
            root = sortedArrayToBSTHelper(A, 0, A.size()-1);
            return root;
        }

        TreeNode *sortedArrayToBSTHelper(vector<int> &A, int start, int end) {
            if (start <= end) {
                TreeNode * root = new TreeNode();
                int mid = start + (end - start)/2;
                root->val = A[mid];
                root->left = sortedArrayToBSTHelper(A, start, mid-1);
                root->right = sortedArrayToBSTHelper(A, mid + 1, end);
                return root;
            } else {
                return nullptr;
            }
        }
    };



