from functools import reduce
import math

class Solution:
    def reduce_to_list(self, list1, list2):
        zipped_lists = list(zip(list1,list2))
        return list(reduce(lambda x, y: x + y, zipped_lists))

    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        if not deck:
            return None
        len_deck = len(deck)
        if len_deck in (1,2):
            return deck
        deck_even = True if len_deck % 2 == 0 else False
        idx = math.ceil(len_deck/2)

        sorted_deck = sorted(deck)            
        left = sorted_deck[:idx]
        right = sorted_deck[idx:] if deck_even else sorted_deck[idx-1:]

        split_right = self.deckRevealedIncreasing(right)
        if deck_even:
            return self.reduce_to_list(left, split_right)
        output = self.reduce_to_list(left[:-1], split_right[1:])
        output.append(left[-1])
        return output