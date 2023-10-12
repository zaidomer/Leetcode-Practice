//https://leetcode.com/problems/valid-anagram/

class Solution {
    public boolean isAnagram(String s, String t) {
        // if(s.length() != t.length()){
        // return false;
        // }

        // Map<Character, Integer> map = new HashMap<>();
        // for(int i = 0; i < s.length(); i++){
        // map.put(s.charAt(i), map.getOrDefault(s.charAt(i), 0)+1);
        // }

        // for(int i = 0; i < t.length(); i++){
        // map.put(t.charAt(i), map.getOrDefault(t.charAt(i), 0)-1);
        // }

        // for(int val : map.values()){
        // if(val != 0){
        // return false;
        // }
        // }

        // return true;

        char[] arr1 = s.toCharArray();
        char[] arr2 = t.toCharArray();

        Arrays.sort(arr1);
        Arrays.sort(arr2);

        return (Arrays.equals(arr1, arr2));
    }
}