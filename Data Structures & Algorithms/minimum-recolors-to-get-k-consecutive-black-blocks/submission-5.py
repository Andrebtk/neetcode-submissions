class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        nb_W  = 0
        
        for i in range(k):
            if blocks[i] == 'W':
                nb_W += 1
        
        L = 0

        res = nb_W
        for R in range(k, len(blocks)):
            
            res = min(res, nb_W)

            if blocks[R] == 'W':
                nb_W += 1

            if blocks[L] == 'W':
                nb_W -= 1

            
            L += 1

            
        
        return res