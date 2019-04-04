class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        flipped = map(lambda x: [x[i-1] for i in range(len(x),0,-1)], A)
        inverted = map(lambda x: [abs(a-1) for a in x], flipped)
        return list(inverted)
    
    # """
    #        for row in A:
    #         for i in xrange((len(row) + 1) / 2):
    #             """
    #             #In Python, the shortcut row[~i] = row[-i-1] = row[len(row) - 1 - i]
    #             #helps us find the i-th value of the row, counting from the right.
    #             """
    #             row[i], row[~i] = row[~i] ^ 1, row[i] ^ 1
    #     return A
    # """