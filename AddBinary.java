//https://leetcode.com/problems/add-binary/

class Solution {
    public String addBinary(String a, String b) {
        String small = "";
        String large = "";
        String result = "";

        if(a.length() < b.length()){
            small = a;
            large = b;
        }else{
            small = b;
            large = a;
        }

        int index = small.length()-1;
        int carry = 0;
        for(int i = large.length()-1; i >= 0; i--){
            int temp = 0;
            if(index >= 0){
                temp = small.charAt(index)-'0' +  large.charAt(i)-'0' + carry;
            }else{
                temp = large.charAt(i)-'0' + carry;
            }
                       
            
            if(temp < 2){
                result=Integer.toString(temp)+result;
                carry = 0;
            }else if(temp == 2){
                result="0"+result;
                carry = 1;
            }else{
                result="1"+result;
                carry = 1;
            }
            index--;
        }

        if(carry==1){
            result = "1" + result;
        }
        return result;
    }
}