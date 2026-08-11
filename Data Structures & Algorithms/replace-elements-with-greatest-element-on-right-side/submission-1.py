class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = []
        max_right = arr[-1]
        ans.insert(0, -1)

        for rev_ind in range(-2, -len(arr) - 1, -1):
            ans.append(max_right)    

            if arr[rev_ind] > max_right:
                max_right = arr[rev_ind]
        
        ans.reverse()
        return ans