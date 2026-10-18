class Solution(object):
    def topKFrequent(self, nums, k):

        count = {}

        temp = []

        result = []


        for i in range(len(nums)): 

            count[nums[i]] = count.get(nums[i], 0) - 1

        
        for num, freq in count.items():
            temp.append((freq, num))

        heapq.heapify(temp)

        for i in range(k):

            freq, num = heapq.heappop(temp)

            num = num * (-1)
            
            result.append(-num)

        return result











            


        