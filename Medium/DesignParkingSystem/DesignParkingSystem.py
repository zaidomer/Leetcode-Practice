# https://leetcode.com/problems/design-parking-system/

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.spots = {1:big, 2:medium, 3:small}
        

    def addCar(self, carType: int) -> bool:
        self.spots[carType]-=1
        return self.spots[carType]>=0


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
