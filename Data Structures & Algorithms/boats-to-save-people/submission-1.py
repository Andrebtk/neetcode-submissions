class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        nb = 0

        L, R = 0, len(people) - 1

        while L <= R:
            if people[L] + people[R] <= limit:
                L += 1
                
            nb += 1
            R -= 1
        
        return nb