class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        nb = 0

        L, R = 0, len(people) - 1

        while L <= R:
            w = people[L] + people[R]
            if w <= limit:
                nb += 1
                L += 1
                R -= 1
            else:
                nb += 1
                R -= 1
        
        return nb