class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        current = [0, 0, 0]

        def isTripletEqual(a, b):
            if a[0] == b[0] and a[1] == b[1] and a[2] == b[2]:
                return True
            return False

        for triplet in triplets:
            if triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                print(triplet[0])
                current = [max(current[0], triplet[0]), max(current[1], triplet[1]), max(current[2], triplet[2])]

            print(current)

            if isTripletEqual(current, target):
                return True
        
        return False
    