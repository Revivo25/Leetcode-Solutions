class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        pairs = {')': '(', ']': '[', '}': '{'}
        stack=[]
        for char in s:
            if char in pairs.values():
                stack.append(char)
            else:
                if not stack or stack[-1] != pairs[char]:
                    return False
                stack.pop()
        return len(stack) == 0
        #הרעיון הוא שאם הא סוגר פתוח אז נכנס לתור של FIFO
        #ולאחר מכן בודקים אם זה סגור סוגר אז חייב להתאים לסגור הפותח האחרון ב STACK
        #נשים לב שבסוף ה STACK חייב להתאפס





        ##"()">> ( [   ( ( ( ( ( 
