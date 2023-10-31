//https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        std::stack<int> stack;
        int num2;
        int num1;
        for(int i = 0; i < tokens.size(); i++){
            if(tokens[i].length()==1 && (int)((tokens[i])[0]) < (int)'0'){
                num2 = stack.top();
                stack.pop();
                num1 = stack.top();
                stack.pop();

                stack.push(operate((tokens[i])[0], num1, num2));
            }else{
                stack.push(stoi(tokens[i]));
            }
        }
        return stack.top();
    }

    int operate(char op, int num1, int num2){
        if(op=='+'){
            return num1+num2;
        }else if(op=='-'){
            return num1-num2;
        }else if(op=='*'){
            return num1*num2;
        }else{
            return num1/num2;
        }
    }
};