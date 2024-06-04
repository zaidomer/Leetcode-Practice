// https://leetcode.com/problems/gas-station/

impl Solution {
    pub fn can_complete_circuit(gas: Vec<i32>, cost: Vec<i32>) -> i32 {
        let mut total_gas = 0;
        let mut curr_gas = 0;
        let mut start_index:i32 = 0;

        for i in 0..gas.len(){
            total_gas += gas[i]-cost[i];
            curr_gas += gas[i]-cost[i];
            if curr_gas<0{
                start_index=((i as i32)+1);
                curr_gas=0;
            }
        }
        if total_gas>=0{
            return start_index;
        }
        return -1;
    }
}