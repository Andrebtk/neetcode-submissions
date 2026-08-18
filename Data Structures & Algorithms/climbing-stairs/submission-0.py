class Solution:
    def climbStairs(self, n: int) -> int:
        

        def tmp(n, cache):
            if n == 1:
                return 1
            
            if n == 2:
                return 2
            
            if n in cache:
                return cache[n]
            
            cache[n] = tmp(n - 1, cache) + tmp(n - 2, cache)
            return cache[n]
        
        return tmp(n, {})
        