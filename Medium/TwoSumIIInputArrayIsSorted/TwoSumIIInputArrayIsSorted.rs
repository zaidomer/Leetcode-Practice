// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

impl Solution {
    pub fn two_sum(numbers: Vec<i32>, target: i32) -> Vec<i32> {
        let mut result = Vec::new();
        for i in 0..numbers.len(){
            let number2 = target-numbers[i];
            let mut number2_index = Self::binary_search(&numbers, number2);
            if number2_index!=-1{
                if number2_index==(i as i32) && number2_index>0 && numbers[((number2_index-1) as usize)]==number2{
                    number2_index-=1;
                }else if number2_index==(i as i32) && number2_index<((numbers.len()-1) as i32) && numbers[((number2_index+1) as usize)]==number2{
                    number2_index+=1;
                }

                if number2_index!=(i as i32){
                    result.push((i as i32)+1);
                    result.push(number2_index+1);
                    return result;
                }
            }
        }
        return result;
    }

    pub fn binary_search(numbers: &Vec<i32>, target: i32) -> i32{
        let mut left:i32 = 0;
        let mut right:i32 = ((numbers.len()-1)as i32);

        while left<=right{
            let mut mid:i32 = left+(right-left)/2;
            if numbers[mid as usize]==target{
                return mid;
            }else if numbers[mid as usize]>target{
                right = mid-1;
            }else{
                left = mid+1;
            }
        }
        return -1;
    }
}

// //ALSO VALID 2 POINTER APPROACH
// impl Solution {
//     pub fn two_sum(numbers: Vec<i32>, target: i32) -> Vec<i32> {
//         let mut left:usize = 0;
//         let mut right:usize = numbers.len()- 1;
//         let vec = Vec::new();
//         while left < right {
//             if numbers[left] + numbers[right] == target {
//                 return vec![left as i32 + 1, right as i32 + 1]
//             } else if numbers[left] + numbers[right] > target {
//                 right -= 1;
//             } else {
//                 left += 1;
//             }
//         }

//         vec
//     }
// }

