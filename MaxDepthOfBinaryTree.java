//https://leetcode.com/problems/maximum-depth-of-binary-tree/

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int maxDepth(TreeNode root) {
        if(root == null){
            return 0;
        }else if((root.left != null) && (root.right != null)){
            return 1 + Math.max(maxDepth(root.right), maxDepth(root.left));
        }else if(root.left != null){
            return 1 + maxDepth(root.left);
        }else if(root.right != null){
            return 1 + maxDepth(root.right);
        }else{
            return 1;
        }
    }
}