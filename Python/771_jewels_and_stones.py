"""
Decompose:
1. check how many in charcters in S match with characters in J

Data:
1. strings J and S

Pattern:
1. for a given character in J, find number of times a matching character
    is found in S
2. from a given string, built a list of tuples with value and number of                   occurrences
"""
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        dict_S = {value: S.count(value) for value in S}
        counter = 0
        for k, v in dict_S.items():
            if k in J:
                counter += v
        return counter