//https://leetcode.com/problems/roman-to-integer/

class Solution {
    // public int romanToInt(String s) {
    //     int i = 0;
    //     int num = 0;
    //     while(i < s.length()){
    //         if(((i < s.length()-1) && (s.charAt(i)=='I') && ((s.charAt(i+1) == 'V') || (s.charAt(i+1) == 'X')))
    //         || ((i < s.length()-1) && (s.charAt(i)=='X') && ((s.charAt(i+1) == 'L') || (s.charAt(i+1) == 'C')))
    //         || ((i < s.length()-1) && (s.charAt(i)=='C') && ((s.charAt(i+1) == 'D') || (s.charAt(i+1) == 'M')))){
    //             num += conversion(s.charAt(i+1)) - conversion(s.charAt(i));
    //             i+=2;
    //         }else{
    //             num += conversion(s.charAt(i));
    //             i++;
    //         }
    //     }
    //     return num;
    // }

    // public int conversion(char c){
    //     if(c == 'I'){
    //         return 1;
    //     }else if(c == 'V'){
    //         return 5;
    //     }else if(c == 'X'){
    //         return 10;
    //     }else if(c == 'L'){
    //         return 50;
    //     }else if(c == 'C'){
    //         return 100;
    //     }else if(c == 'D'){
    //         return 500;
    //     }else{
    //         return 1000;
    //     }
    // }
    public int romanToInt(String s) {
        int currVal = 0;
        int prevVal = 0;
        int res = 0;
        for(int i = s.length() - 1; i >= 0; i--) {
            switch(s.charAt(i)) {
                case 'I' :
                    currVal = 1;
                    break;
                case 'V' :
                    currVal = 5;
                    break;
                case 'X' :
                    currVal = 10;
                    break;
                case 'L' :
                    currVal = 50;
                    break;
                case 'C' :
                    currVal = 100;
                    break;
                case 'D' :
                    currVal = 500;
                    break;
                case 'M' :
                    currVal = 1000;
                    break;
            }
            if(currVal < prevVal) {
                res -= currVal;
            } else {
                res += currVal;
            }
            prevVal = currVal;
        }
        return res;
    }
}