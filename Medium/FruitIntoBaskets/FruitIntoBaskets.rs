// https://leetcode.com/problems/fruit-into-baskets/

use std::cmp;

impl Solution {
    pub fn total_fruit(fruits: Vec<i32>) -> i32 {
        let mut result = 0;
        let mut basket_one_fruit = fruits[0];
        let mut basket_two_fruit = -1;

        let mut start = 0;
        let mut next_start = fruits.len();

        //find second fruit type (for first iteration)
        for i in 1..fruits.len() {
            if basket_two_fruit == -1 && fruits[i] != basket_one_fruit {
                basket_two_fruit = fruits[i];
                next_start = i;
            }
        }

        //check all possibilities
        for i in next_start + 1..fruits.len() {
            if fruits[i] == basket_one_fruit {
                next_start = i;
                let temp = basket_one_fruit;
                basket_one_fruit = basket_two_fruit;
                basket_two_fruit = temp;
            } else if fruits[i] != basket_one_fruit && fruits[i] != basket_two_fruit {
                result = cmp::max(result, i - start);
                start = next_start;
                basket_one_fruit = basket_two_fruit;
                basket_two_fruit = fruits[i];
                next_start = i;
            }
        }

        result = cmp::max(result, fruits.len() - start);
        return result as i32;
    }
}
