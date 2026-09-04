class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        nbWhiteMin = 0

        L = 0
        for i in range(k):
            if blocks[i] == 'W':
                nbWhiteMin += 1
        
        curWindowNbW = nbWhiteMin
        for R in range(k, len(blocks), 1):
            
            if blocks[R] == 'W':
                curWindowNbW += 1

            if blocks[L] == 'W':
                curWindowNbW -= 1

            nbWhiteMin = min(nbWhiteMin, curWindowNbW)

            L += 1
        
        return nbWhiteMin
              