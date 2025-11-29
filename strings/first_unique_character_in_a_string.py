# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/881/

from collections import Counter

def firstUniqChar(s):
    """
    :type s: str
    :rtype: int
    """
    counter = Counter(s)
    
    for i, char in enumerate(s):
        
        if counter[char] == 1:
            return i
        
    return -1
    
