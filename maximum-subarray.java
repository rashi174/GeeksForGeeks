/*
53. Maximum Subarray / Kadane's Algorithm

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [0]
Output: 0
Example 4:

Input: nums = [-1]
Output: -1
Example 5:

Input: nums = [-100000]
Output: -100000
 

Constraints:

1 <= nums.length <= 3 * 104
-105 <= nums[i] <= 105
 

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

*/

/*

ALGORITHM

1. Maintain two variables one for current sum other for the maximum sum globally.
2. If current sum is greater than maxsum than update maxsum.
3. If current sum is less than 0 then update it to 0 as adding -ve to sum will make it smaller only.

*/


class Solution {
    public int maxSubArray(int[] nums) {
        int maxsum=Integer.MIN_VALUE;
        int currsum=0;
        for(int i=0;i<nums.length;i++)
        {
            currsum+=nums[i];
            
            if (currsum>maxsum)
                {
                    maxsum=currsum;
                }
            if (currsum<0)
            {
                currsum=0;
            }
        }
        return maxsum;
    }
}
