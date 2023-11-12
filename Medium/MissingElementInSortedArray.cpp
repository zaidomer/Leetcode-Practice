#include <iostream>
#include <vector>

int numMissing(std::vector<int> &nums, int index){
	return nums[index]-nums[0]-index;
}

int missingElement(std::vector<int> &nums, int k){
	/*
	 * O(n) solution:
	int count = 0;
	int current = nums[0];
	int index = 1;
	while(count < k){
		current++;
		if(index>=nums.size() || nums[index] != current){
			count++;
		}else{
			index++;
		}
		
	}
	
	return current;
	*/

	if(numMissing(nums, nums.size()-1) < k){
		return nums[nums.size()-1] + k-numMissing(nums, nums.size()-1);
	}

	//Binary Search
	int left = 0;
	int right = nums.size()-1;
	//int prevState = numMissing(nums, left+(right-left)/2);

	while(left < right){
		int mid = left+(right-left)/2;

		if(numMissing(nums, mid) < k){
			left = mid+1;
		}else{
			right = mid;
		}	
	}
	return nums[right-1] + k-numMissing(nums, right-1);
		
}

int main(){

	std::vector<int> nums = {4,7,9,10};
	std::cout << missingElement(nums, 1) << std::endl;
	std::cout << missingElement(nums, 3) << std::endl;

	nums.clear();
	nums = {1,2,4};
	std::cout << missingElement(nums, 3) << std::endl;
	
	nums.clear();
	nums = {2,3,4,6,7};
	std::cout << missingElement(nums, 1) << std::endl;
	return 0;
}
