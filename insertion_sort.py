def insertion_sort(nums):
    n=len(nums)
    for i in range(1,n):
        curr=nums[i]
        j=i-1
        while j>=0 and nums[j]>curr:
            nums[j+1]=nums[j]
            nums[j]=curr
            j=j-1
    return nums
