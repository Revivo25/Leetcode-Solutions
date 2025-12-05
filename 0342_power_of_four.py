class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        """
        ##naive approach
        if n == 1:
            return True
        while n > 1: 
            if n%4 != 0:
                return False
            n = n//4
        return n == 1
        """
        return n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555) == n

        """
        explanation:
        ##Bits method approach
        # 4^0= 1 =   000001
        # 4^1 = 4 =  000100
        # 4^2 = 16 = 010000 
        notice that each relevant number (that is 4^num) leads to
        a result which the binary number includes 1 at an even spot
        example:
        # 4^0= 1 =   000001 here 1 is at position 0
        # 4^1 = 4 =  000100 here 1 is at position 2
        # 4^2 = 16 = 010000 here 1 is at position 4
        and so on ...
        """
