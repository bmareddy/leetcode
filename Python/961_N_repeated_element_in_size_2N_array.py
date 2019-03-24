class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        counter = 0
        N = len(A) / 2
        for a in A:
            a_count = A.count(a)
            if a_count == N:
                return a
            counter += a_count
            if counter == N:
                return A[0]
            else:
                A.remove(a)