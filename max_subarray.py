def max_subarray(nums):
    high = len(nums) - 1
    low = 0
    
    if low == high:
        return low, high, nums[low]
    
    else:
        mid = (high - low + 1) // 2
        left = nums[:mid]
        right = nums[mid:]
        left_low, left_high, left_sum = max_subarray(left)
        right_low, right_high, right_sum = max_subarray(right)
        cross_low, cross_high, cross_sum = max_cross(nums)
        
        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        
        else:
            return (cross_low, cross_high, cross_sum)
            
            
        
def max_cross(nums):
    low = 0
    high = len(nums) - 1
    mid = len(nums) // 2
    max_left=0
    left_sum = float('-inf')
    sum = 0
    for i in range(mid - 1, -1, -1):
        sum = sum + nums[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
            
    max_right=0
    right_sum = float('-inf')
    sum = 0
    for i in range(mid, high, 1):
        sum = sum + nums[i]
        if sum > right_sum:
            right_sum = sum
            max_right = i
    return (max_left, max_right, left_sum + right_sum)
