// https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree

class Solution {
public:
    int sumOfGreater = 0;

    TreeNode* bstToGst(TreeNode* root) {
        if(root != nullptr){
            bstToGst(root->right);
            sumOfGreater+=root->val;
            root->val=sumOfGreater;
            bstToGst(root->left);
        }
        return root;
    }
};
