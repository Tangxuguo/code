# find the connected component in the undirected graph


和找小岛个数差不多，也是用DFS的方法，需要记住每个节点是否已经访问过，当全部节点访问完了，跳出

    /**
     * Definition for Undirected graph.
     * struct UndirectedGraphNode {
     *     int label;
     *     vector<UndirectedGraphNode *> neighbors;
     *     UndirectedGraphNode(int x) : label(x) {};
     * };
     */
    class Solution {
    public:
        /**
         * @param nodes a array of Undirected graph node
         * @return a connected set of a Undirected graph
         */
        vector<vector<int>> connectedSet(vector<UndirectedGraphNode*>& nodes) {
            // Write your code here
            unordered_set<UndirectedGraphNode*> visit;
            vector<vector<int>> res;
            vector<int> path;
            for (auto &n : nodes) {
                if (visit.find(n) == visit.end()) {
                    path.clear();
                    dfs(nodes, path, visit, n);
                    sort(path.begin(), path.end());
                    res.push_back(path);
                }
            }
            return res;
        }

        void dfs(vector<UndirectedGraphNode*> &nodes, vector<int> &path,
            unordered_set<UndirectedGraphNode*> &visit, UndirectedGraphNode* n) {
            visit.insert(n);
            path.push_back(n->label);
            for (auto &nn : n->neighbors)
                if (visit.find(nn) == visit.end()) {
                    dfs(nodes, path, visit, nn);
                }
        }
    };
