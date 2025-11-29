# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/879/

def reverseString(self, s):
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """
    i = 0
    j = len(s) - 1
    
    half = round(len(s)/2)
    
    while i != half:
        aux = s[i]
        s[i] = s[j]
        s[j] = aux
        
        i += 1
        j -= 1
    
    return s
            
