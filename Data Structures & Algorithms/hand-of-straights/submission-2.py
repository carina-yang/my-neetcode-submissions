import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = {}

        for card in hand:
            if card not in count:
                count[card] = 0
            count[card] += 1
        
        unique_hand = list(set(hand))
        heapq.heapify(unique_hand)

        cur_group = []

        while unique_hand:
            val = heapq.heappop(unique_hand)

            if cur_group and val != cur_group[-1] + 1:
                return False

            count[val] -= 1
            cur_group.append(val)

            if len(cur_group) == groupSize:
                for i in cur_group:
                    if count[i] > 0:
                        heapq.heappush(unique_hand, i)
                cur_group = []
            
        if cur_group:
            return False

        return True
            