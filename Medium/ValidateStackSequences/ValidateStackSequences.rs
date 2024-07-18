// https://leetcode.com/problems/validate-stack-sequences/

use std::collections::VecDeque;

impl Solution {
    pub fn validate_stack_sequences(pushed: Vec<i32>, popped: Vec<i32>) -> bool {
        let mut stack = Vec::new();
        let mut pop_index = 0;

        for i in 0..pushed.len() {
            stack.push(pushed[i]);

            while !stack.is_empty() && stack.last() == popped.get(pop_index) {
                stack.pop();
                pop_index += 1;
            }
        }
        return stack.is_empty();
    }
}
