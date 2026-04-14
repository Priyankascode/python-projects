def twoSum(nums: list[int], target: int) -> list[int]:

        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in nums and nums.index(remainder) != i:
                return [i, nums.index(remainder)]
        return []

indexlist = twoSum([2, 7, 11, 15], 9)
print(indexlist)