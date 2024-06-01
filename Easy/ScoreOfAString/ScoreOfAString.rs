// https://leetcode.com/problems/score-of-a-string/

impl Solution {
    pub fn score_of_string(s: String) -> i32 {
        let mut result = 0;
        let chars: Vec<char> = s.chars().collect();
        for i in 0..s.len()-1{
            result += ((chars[i] as i32) - (chars[i+1] as i32)).abs();
        }
        return result;
    }
}