def is_monotonic(nums):
	flag = True
  for i in range(len(nums) - 1):
    if nums[0] < nums[-1]:
        if not nums[i] <=nums[i + 1]:
      flag = False
else:
    if not nums[i] >= nums[i+1]:
    flag = False
return flag