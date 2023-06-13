class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        '''

        Important thing to note: 

        min heap has the size of number of meeting rooms, it doesn't need to increase as long as the room  with minimum end-time 
        is ending before the start to next meeting, if its not ending, then we need to put 1 more room



        '''

        import heapq
        min_heap=[]
        intervals=sorted(intervals)
        for interval in intervals:
            if min_heap==[] or interval[0]<min_heap[0]:
                heapq.heappush(min_heap,interval[1])
            else:
                heapq.heapreplace(min_heap,interval[1])
        return len(min_heap)


