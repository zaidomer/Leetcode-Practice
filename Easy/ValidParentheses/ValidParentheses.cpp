class Solution {
public:
    bool isValid(string s) {
        std::stack<char> stack;
        for(int i = 0; i < s.length(); i++){
            if(s[i] == '(' || s[i] == '[' || s[i] == '{'){
                stack.push(s[i]);
            }else if(stack.empty()){
                return false;
            }else{
                const auto& last_element = stack.top();
                if(s[i] == ')' && last_element != '(')
                    return false;
                else if(s[i] == ']' && last_element != '[')
                    return false;
                else if(s[i] == '}' && last_element != '{')
                    return false;
                stack.pop();
            }
        }
        return stack.empty();
    }
};