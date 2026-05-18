import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = {}

        for card in hand:
            count[card] = count.get(card, 0) + 1
        
        for card in sorted(count):
            while count[card] > 0:
                for next_card in range(card, card + groupSize):
                    if next_card not in count or count[next_card] == 0:
                        return False
                    count[next_card] -= 1
        
        return True

            