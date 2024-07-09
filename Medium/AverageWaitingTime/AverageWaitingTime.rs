// https://leetcode.com/problems/average-waiting-time/

impl Solution {
    pub fn average_waiting_time(customers: Vec<Vec<i32>>) -> f64 {
        let mut curr = 0_i64;
        let mut totalWaitTimes = 0_i64;
        for customer in customers.iter() {
            let prep_time = customer[1] as i64;
            let arrival = customer[0] as i64;

            if arrival > curr {
                totalWaitTimes += prep_time;
                curr = arrival + prep_time;
            } else {
                curr += prep_time;
                totalWaitTimes += curr - arrival;
            }
        }

        return ((totalWaitTimes as f64) / (customers.len() as f64));
    }
}
