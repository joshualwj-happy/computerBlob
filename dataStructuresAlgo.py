#Data Structures: objecs, arrays, 3d arrays
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9] # can only store letters OR numbers not two of them
#itterable means it can go trought multiple data one by one

def twoSum(nums: list[int], target: int):
    result = []
    for number in nums:
        for i in range(nums.index(number) + 1, len(nums)):
            if number + nums[i] == target:
                result.append(nums.index(number))
                result.append(i)
                return result

nums = [2,7,11,15]
target = 9

print(twoSum(nums, target))