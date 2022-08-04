class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        return [lst for lsts in [list(combinations(nums,i)) for i in range(n+1)] for lst in lsts]