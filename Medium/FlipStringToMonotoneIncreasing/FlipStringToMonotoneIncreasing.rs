// https://leetcode.com/problems/flip-string-to-monotone-increasing/

use std::cmp;

impl Solution {
    pub fn min_flips_mono_incr(s: String) -> i32 {
        let str_chars: Vec<char> = s.chars().collect();
        let mut result = 0;
        let mut num_ones = 0;

        for ch in str_chars.iter() {
            match ch {
                '0' => {
                    result = cmp::min(result + 1, num_ones);
                }

                _ => {
                    num_ones += 1;
                }
            }
        }

        return result;
    }
}
