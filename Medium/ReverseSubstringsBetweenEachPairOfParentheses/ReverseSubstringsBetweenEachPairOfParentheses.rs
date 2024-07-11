// https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

use std::collections::VecDeque;

impl Solution {
    pub fn reverse_parentheses(s: String) -> String {
        let chars: Vec<char> = s.chars().collect();
        let mut curr_word = String::from("");
        let mut stack: VecDeque<String> = VecDeque::new();

        for ch in chars.iter() {
            if *ch != '(' && *ch != ')' {
                curr_word.push_str(&ch.to_string());
            } else if *ch == '(' {
                stack.push_back(curr_word);
                curr_word = String::from("");
            } else if *ch == ')' {
                let mut reversed = curr_word.chars().rev().collect();
                match stack.pop_back() {
                    None => {
                        curr_word = reversed;
                    }
                    Some(s) => {
                        curr_word = format!("{}{}", s, reversed);
                    }
                }
            }
        }

        return curr_word;
    }
}
