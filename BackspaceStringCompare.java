//https://leetcode.com/problems/backspace-string-compare/

class Solution {
    public boolean backspaceCompare(String s, String t) {
        return compute(s).equals(compute(t));
    }

    public String compute(String s) {
        StringBuilder ans = new StringBuilder();
        int skip = 0;
        for (int i = s.length() - 1; i >= 0; i--) {
            if (s.charAt(i) == '#') {
                skip++;
            } else if (skip > 0) {
                skip--;
            } else {
                ans.append(Character.toString(s.charAt(i)));
            }
        }
        return ans.toString();
    }
}