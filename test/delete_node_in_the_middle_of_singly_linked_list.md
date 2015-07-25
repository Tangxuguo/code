# delete node in the middle of singly linked list

思路是把后面的值移到要删除的节点上就可以了，删除后面的节点，连接，其他不变

    /**
     * Definition of ListNode
     * class ListNode {
     * public:
     *     int val;
     *     ListNode *next;
     *     ListNode(int val) {
     *         this->val = val;
     *         this->next = NULL;
     *     }
     * }
     */
    class Solution {
    public:
        /**
         * @param node: a node in the list should be deleted
         * @return: nothing
         */
        void deleteNode(ListNode *node) {
            // write your code here
            ListNode *tmp;
            node->val = node->next->val;
            tmp = node->next;
            node->next = node->next->next;
            delete(tmp);
        }
    };
