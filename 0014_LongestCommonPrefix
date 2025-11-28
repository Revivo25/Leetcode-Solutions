class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        prefix = strs[0] #prefix is now "Flower" for example 1
        
        for s in strs[1:]: #not including first string because we took it as prefix
            while s[:len(prefix)] != prefix:
                prefix = prefix[:-1]
                if not prefix: ##if prefix is now empty
                    return ""
        return prefix


  # Prefix = "flower"
# 1st iteration for s loop:
# s[:len(prefix)] = s[0:6] = "flow"
# but prefix = "flower" != "flow" so cut off last char:
# prefix = "flowe", s[:5] = "flow"
# prefix = "flow", s[:4] = "flow"
# prefix found, continue

     
