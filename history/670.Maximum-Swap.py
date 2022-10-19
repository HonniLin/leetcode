class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        :desc
        Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. 
        Return the maximum valued number you could get.
        :way
        We can also get an O(N) solution. 
        At each digit, if there is a larger digit that occurs later, 
        we want the swap it with the largest such digit that occurs the latest.

        """
        A = map(int, str(num))
        print A #[2, 7, 3, 6]
        last = {x: i for i, x in enumerate(A)}
        print last #{2: 0, 3: 2, 6: 3, 7: 1}
        for i, x in enumerate(A):
            for d in xrange(9, x, -1):
                if last.get(d, None) > i:
                    A[i], A[last[d]] = A[last[d]], A[i]
                    return int("".join(map(str, A)))
        return num