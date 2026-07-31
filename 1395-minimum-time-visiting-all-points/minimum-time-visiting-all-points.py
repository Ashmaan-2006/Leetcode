class Solution(object):
    def minTimeToVisitAllPoints(self, points):

        counter = 0

        for i in range(len(points) - 1):
    
            x1, y1 = points[i]
            x2, y2 = points[i + 1]

            each_time = max( (abs(x2 - x1)), (abs(y2 - y1)) )

            counter += each_time

            #assuming there are 3 points, this is would be 0, 1 ,2, need it from 0 to 1 and 1 to 2, not 2 to 3

        return counter
        