// https://leetcode.com/problems/diameter-of-binary-tree/

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
    int help(TreeNode* root, int &count){
        if(root==nullptr){
            return 0;
        }
        int left = help(root->left, count);
        int right = help(root->right, count);
        count = max(count, left+right);
        return 1 + max(left, right);
    }

    int diameterOfBinaryTree(TreeNode* root) {
        int result = 0;
        help(root, result);
        return result;
    }

};