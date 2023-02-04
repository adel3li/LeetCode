class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        d, n ,m ,s = collections.Counter(nums), min(nums), max(nums), []
        for i in range(n, m+1):
            s.extend([i]*d[i])
        return s
