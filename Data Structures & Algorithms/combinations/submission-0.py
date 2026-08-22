class Solution:
    def helper(self, i, k, n, curCom, repComb):
        if len(curCom) == k:
            repComb.append(curCom.copy())
            return
        
        if i > n:
            return
        
        # We select the number
        curCom.append(i)
        self.helper(i + 1, k, n, curCom, repComb)
        curCom.pop()


        # We do not
        self.helper(i + 1, k, n, curCom, repComb)
    
    def combine(self, n: int, k: int) -> List[List[int]]:
        repComb = []
        self.helper(1, k, n, [], repComb)
        return repComb