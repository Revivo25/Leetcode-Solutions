class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        if num == 0 or num < 9:
            return num

        if num % 9 == 0:
            return 9 #>> dividable by 9 so we return 9
        return num%9
        

        ##examples: num = 345 >> 3+4+5 = 12 >> 1+2 = 3
                    # 345%9 == 3
                    # num = 90  >> 90%9 = 0 so we return 9 (9+0)
                    # first condition is obvious.
                    