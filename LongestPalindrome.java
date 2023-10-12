//https://leetcode.com/problems/longest-palindrome/

class Solution {
    public int longestPalindrome(String s) {
        Map<Character, Integer> map = new HashMap<>();

        int odd = 0;
        for(int i = 0; i < s.length(); i++){
            map.put(s.charAt(i), map.getOrDefault(s.charAt(i), 0)+1);
            if(map.get(s.charAt(i))%2!=0){
                odd++;
            }else{
                odd--;
            }
        }

        if(odd>0){
            return s.length()-odd+1;
        }
        return s.length();

    }
}