class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i ,j in zip(nums[:n],nums[n:]) :
            res += i,j
        return res

# another solution
        ans = []
        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[i+n])
        return ans
