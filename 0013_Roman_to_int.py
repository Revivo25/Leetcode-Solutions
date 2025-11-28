class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        result = 0
        k = 0
        while k < len(s):
            if s[k: k+2] in roman:
                result += roman[s[k: k+2]]
                k += 2
            else:
                result += roman[s[k]]
                k += 1

        return result