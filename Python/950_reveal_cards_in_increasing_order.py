from functools import reduce
import math

def reduce_to_list(list1, list2):
    zipped_lists = list(zip(list1,list2))
    return list(reduce(lambda x, y: x + y, zipped_lists))
    
def splitDeck(deck):
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

    split_right = splitDeck(right)
    if deck_even:
        return reduce_to_list(left, split_right)
    output = reduce_to_list(left[:-1], split_right[1:])
    output.append(left[-1])
    return output

for i in range(1,12):
    input = list(range(1,i))
    output = splitDeck(input)
    print("{0} --> {1}".format(input,output))


input = [17,13,11,2,21,3,5,7,19,8,10,16,14]
print(splitDeck(input))
# Output: [2,19,3,13,5,17,7,14,8,21,10,16,11]