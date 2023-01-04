class Solution:
    def twoSum(self, nums, target: int):

        # nums is list of given numbers
        # target is the given sum which is to be find
        # seen is a dictonary we have created to store data

        seen = {}

        # for loop to iterate to each array

        for i, value in enumerate(nums):
            remaining = target - nums[i]
            # we find ramaining and check it is in seen or not
            if remaining in seen:
                # if find then return current index and index of remaining
                return [i, seen[remaining]]
            # otherwise add it in seen
            seen[value] = i

            # print(seen)
            # print(remaining)


sol = Solution()
nums = [2, 7, 11, 15]
print(sol.twoSum(nums, 9))
nums1 = [3, 2, 4]
print(sol.twoSum(nums1, 6))
nums2 = [3, 3]
print(sol.twoSum(nums2, 6))
