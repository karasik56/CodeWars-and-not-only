def two_sum(numbers, target):
	count_index = -1
	for i in numbers:
		count_index += 1
		for k in range(len(numbers)):
			if i + numbers[k] == target and count_index != k:
				return count_index, k


print(two_sum([2,2,3], 4)) # ---> (0, 2)