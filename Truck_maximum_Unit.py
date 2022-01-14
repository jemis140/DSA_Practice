class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda box: box[1])
        print(boxTypes)
        ans = 0
        while truckSize > 0 and boxTypes:
            box, unit = boxTypes.pop()
            print(box,unit)
            taken = min(box, truckSize)
            ans += unit * taken
            truckSize -= taken
        return ans