'''
You are given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
two sum problem:
    so, we can assume the list of numbers is unsorted.
    Let's think about datastructures.
    We can initialize a hashmap, where the keys are the numbers from the list, and the values are the indices of corresponding numbers.
    Then we can iterate through the numbers in the list and check, is the target - current_value in the hashmap keys?
        if yes, then fetch the target - current_value's index from the hashmap, append it to our result list, and also append our current index. then return.
        otherwise, add the current value and current index
    if there is no two numbers in the list that sum to target, then return empty list
'''

def twoSumUnsorted(nums, target):
    hashMap = {}
    result = []
    for indx in range(len(nums)):
        if target - nums[indx] in hashMap:
            result.append(hashMap[target-nums[indx]])
            result.append(indx)
            return result
        hashMap[nums[indx]] = indx # no need for else bc if statement returns result
    return [] # if there is no solution

nums = [2,12,7,11,15]
print(twoSumUnsorted(nums, 9))