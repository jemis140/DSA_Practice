# You are assigned to put some amount of boxes onto one truck.
# You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:

# numberOfBoxesi is the number of boxes of type i.
# numberOfUnitsPerBoxi is the number of units in each box of the type i.
# You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck.
# You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.

# Return the maximum total number of units that can be put on the truck.


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        sortedBoxTypes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        totalUnits = 0
        for box in sortedBoxTypes:
            if truckSize == 0:
                break
            if truckSize - box[0] > 0:
                truckSize -= box[0]
                totalUnits += box[0] * box[1]
            else:
                totalUnits += truckSize * box[1]
                truckSize = 0
            print(totalUnits)
        return totalUnits


# class Solution {
# public:
#     int maximumUnits(vector<vector<int>>& boxTypes, int truckSize) {
#         priority_queue<vector<int>, vector<vector<int>>, Comparator> queue;
#         for (auto boxType : boxTypes) {
#             queue.push(boxType);
#         }
#         int unitCount = 0;
#         while (!queue.empty()) {
#             vector<int> top = queue.top();
#             queue.pop();
#             int boxCount = min(truckSize, top[0]);
#             unitCount += boxCount * top[1];
#             truckSize -= boxCount;
#             if(truckSize == 0)
#                 break;
#         }
#         return unitCount;
#     }

#     struct Comparator {
#         bool operator()(vector<int> const& p1, vector<int> const& p2) {
#             return p1[1] < p2[1];
#         }
#     };
# };
