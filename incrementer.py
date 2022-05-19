''' https://www.codewars.com/kata/590e03aef55cab099a0002e8/train/python '''

def incrementer(nums):
    for i in range(1, len(nums)+1):
        if nums[i-1] + i > 9:
            nums[i-1] = int(str(nums[i-1]+i)[-1])
        else:
            nums[i-1] = nums[i-1] + i
    return nums






print(incrementer([4, 6, 7, 1, 3]))