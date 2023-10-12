//https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution {
    public int lengthOfLongestSubstring(String s) {
        // Set<Character> set = new HashSet<>();
        // int longest = 0;
        // StringBuilder current = new StringBuilder();
        // for(int i = 0; i < s.length(); i++){
        // if(set.contains(s.charAt(i))){
        // current.delete(0,current.indexOf(Character.toString(s.charAt(i)))+1);
        // }
        // set.add(s.charAt(i));
        // current.append(s.charAt(i));
        // if(current.length()>longest){
        // longest = current.length();
        // }
        // }
        // return longest;
        int maxLength = 0;
        int[] charIndex = new int[128];
        Arrays.fill(charIndex, -1);
        int left = 0;

        for (int right = 0; right < s.length(); right++) {
            if (charIndex[s.charAt(right)] >= left) {
                left = charIndex[s.charAt(right)] + 1;
            }
            charIndex[s.charAt(right)] = right;
            maxLength = Math.max(maxLength, right - left + 1);
        }

        return maxLength;
    }
}