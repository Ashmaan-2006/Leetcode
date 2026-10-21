class Solution(object):
    def carFleet(self, target, position, speed):

        cars = []
        slowest_time = 0
        fleet = 0

        for i in range(len(position)):
            cars.append((position[i], speed[i]))

        cars.sort(reverse=True)

        for position, speed in cars:

            time = float(target - position) / speed

            if time > slowest_time:
                fleet += 1
                slowest_time = time

        return fleet



        
        