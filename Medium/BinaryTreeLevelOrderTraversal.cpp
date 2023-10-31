//https://leetcode.com/problems/binary-tree-level-order-traversal/description/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        if(root==nullptr){
            return {};
        }
        std::vector<vector<int>> answer;
        answer.push_back({root->val});

        std::vector<TreeNode*> currentLevel;
        currentLevel.push_back(root);

        while(currentLevel.size()>0){
            updateLevel(currentLevel, answer);
        }
        return answer;
    }

    void updateLevel(vector<TreeNode*> &currentLevel, vector<vector<int>> &answer){
        std::vector<int> values;
        int startSize = currentLevel.size();
        for(int i = 0; i < startSize; i++){
            if(currentLevel[i]->left != nullptr){
                currentLevel.push_back(currentLevel[i]->left);
                values.push_back(currentLevel[i]->left->val);
            }
            if(currentLevel[i]->right != nullptr){
                currentLevel.push_back(currentLevel[i]->right);
                values.push_back(currentLevel[i]->right->val);
            }
        }

        currentLevel.erase(currentLevel.begin(), currentLevel.begin() + startSize);

        if(values.size()>0){
            answer.push_back(values);
        }
    }
};