class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n & (n-1) == 0:
            return True
        return False
        

        #if n not pow of 2 it'll be like: 1010101010
        #if n ^ 2 >> it will be like 100000000000
        # 1&0 >  0
        # 1&1 > 1
        
