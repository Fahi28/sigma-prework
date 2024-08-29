def max_min(nums):
    min = nums[0]
    max = nums[0]
    for num in nums:
        if num < min:
            min = num
        if num > max:
            max = num
    return [min, max]


print(max_min([2, 4, 1, 0, 2, -1]))
print(max_min([20, 50, 12, 6, 14, 8]))
print(max_min([100, -100]))
