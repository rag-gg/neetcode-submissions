class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            num = nums[i]
            req = target - num

            if req in hashmap:
                return [hashmap[req], i]
            hashmap[num] = i
            

