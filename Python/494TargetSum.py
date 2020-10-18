class Solution:
    def ss(self,arr, curr_sum, n,req_sum, dp):
        if n==0:
            if curr_sum==req_sum:
                return 1
            else:
                return 0
        else:
            
            if dp[curr_sum+1000][n]==-1:
                dp[curr_sum+1000][n] = self.ss(arr, curr_sum -arr[n-1], n-1,req_sum, dp) + self.ss(arr, curr_sum+arr[n-1], n-1,req_sum, dp)
                
            return dp[curr_sum+1000][n]
        
        
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        n = len(nums)
        total = sum(nums)
        dp = []
        for _ in range(2001):
            dp.append([-1]*(n+1))
        return self.ss(nums, 0, n, S, dp)