
'''
If the nums list is sorted, we can use the two pointer method instead to efficiently scan the list one time
    have a left and right pointer
        left pointer starts at the leftmost side
        right pointer starts at the rightmost side
        while the left is less than the right pointer, we add the nums[left] and nums[right] and
            compare the sum to the target
            if the sum is less than the target, then we increment the left pointer
            if the sum is more than the target, then we decrement the right pointer
            if the sum is equal to the target we return a list containing left and right
'''
def twoSumSorted(nums, target):
    left = 0
    right = len(nums)-1
    while(left < right):
        if(nums[left]+nums[right] == target):
            return [left, right]
        if(nums[left]+nums[right] < target):
            left+=1
        else:
            right-=1
    return []

nums = [2,4,7,11,15]
print(twoSumSorted(nums, 9))