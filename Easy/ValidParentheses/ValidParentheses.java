package ValidParentheses;
//https://leetcode.com/problems/valid-parentheses/

class Solution {
    public boolean isValid(String s) {
        Stack<Character> brackets = new Stack<Character>();
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                brackets.push(')');
            } else if (s.charAt(i) == '[') {
                brackets.push(']');
            } else if (s.charAt(i) == '{') {
                brackets.push('}');
            } else if (brackets.empty() || s.charAt(i) != brackets.pop()) {
                return false;
            }
        }

        return brackets.empty();
    }
}