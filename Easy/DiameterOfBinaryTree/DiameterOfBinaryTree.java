package DiameterOfBinaryTree;
//https://leetcode.com/problems/diameter-of-binary-tree/

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode right;
 * TreeNode() {}
 * TreeNode(int val) { this.val = val; }
 * TreeNode(int val, TreeNode left, TreeNode right) {
 * this.val = val;
 * this.left = left;
 * this.right = right;
 * }
 * }
 */
class Solution {
    // public int diameterOfBinaryTree(TreeNode root) {
    // int max = 0;

    // if(root==null){
    // return 0;
    // }else if((root.left != null) && (root.right!=null)){
    // max = 2 + help(root.right) + help(root.left);
    // }
    // else if(root.right!=null){
    // max = 1 + help(root.right);
    // }else if(root.left!=null){
    // max = 1 + help(root.left);
    // }

    // max = Math.max(max, diameterOfBinaryTree(root.right));
    // max = Math.max(max, diameterOfBinaryTree(root.left));
    // return max;
    // }

    // public int help(TreeNode root){
    // if((root.left != null) && (root.right != null)){
    // return 1 + Math.max(help(root.left), help(root.right));
    // }else if(root.left != null){
    // return 1 + help(root.left);
    // }else if(root.right != null){
    // return 1 + help(root.right);
    // }else{
    // return 0;
    // }
    // }

    public int diameterOfBinaryTree(TreeNode root) {

        // Create an array to hold the diameter of the tree
        int diameter[] = new int[1];

        // Recursively calculate the height of the tree and update the diameter array
        height(root, diameter);

        // Return the diameter of the tree
        return diameter[0];
    }

    public int height(TreeNode root, int diameter[]) {

        // Base case: if the root is null, the height is 0
        if (root == null) {
            return 0;
        }

        // Recursively calculate the height of the left and right subtrees
        int left = height(root.left, diameter);
        int right = height(root.right, diameter);

        // Update the diameter array by taking the maximum diameter that passes through
        // the current node
        diameter[0] = Math.max(diameter[0], left + right);

        // Return the maximum depth of the current node by adding 1 to the maximum depth
        // of its deepest subtree
        return Math.max(left, right) + 1;
    }

}