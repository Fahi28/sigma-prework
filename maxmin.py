def max_min(nums):
    nums.sort()
    min = nums[0]
    max = nums[len(nums) - 1]
    return [min, max]


print(max_min([2, 4, 1, 0, 2, -1]))
print(max_min([20, 50, 12, 6, 14, 8]))
print(max_min([100, -100]))
