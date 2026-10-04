class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])
        output = [intervals[0]]

        for i in range(1, len(intervals)):
            lastEnd = output[-1][1]
            start = intervals[i][0]

            if start <= lastEnd:
                output[-1][1] = max(output[-1][1], intervals[i][1])
            else:
                output.append(intervals[i])
        return output

                
