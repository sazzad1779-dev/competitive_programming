
 


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        ref = 0
        common = set()
        for i in range(len(s)):
            print(i)
            f = s[i]
            if f in s[i+1:] or f in common:
                common.add(f)
                continue
            else:
                ref=1
            if ref==0:
                return -1
            else:
                return i
        return -1
s =Solution() 
print(s.firstUniqChar("sazzzvbn bskskadd"))  
