def find_missing nums(nums):
	missed_nums = []
for i in range(1, len(nums)):
	if i not in nums:
		missed_nums.append(i)
return missed_nums