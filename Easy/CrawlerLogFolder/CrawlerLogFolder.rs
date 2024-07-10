// https://leetcode.com/problems/crawler-log-folder/

use std::cmp;

impl Solution {
    pub fn min_operations(logs: Vec<String>) -> i32 {
        let mut dir_level: i32 = 0;
        for operation in logs.iter() {
            match operation.as_str() {
                "../" => {
                    dir_level = cmp::max(0, dir_level - 1);
                }

                "./" => {}

                _ => {
                    dir_level += 1;
                }
            }
        }
        return dir_level;
    }
}
