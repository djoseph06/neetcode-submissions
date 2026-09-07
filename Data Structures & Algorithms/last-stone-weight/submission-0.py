class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) >= 2:
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)

            if x == y:
                break
            
            elif x < y:
                leftover = y - x
                heapq.heappush(heap, -leftover)

            
        if len(heap) == 1:
            return -heap[0]
        
        return 0








       


        