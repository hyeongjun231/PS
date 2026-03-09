class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)
        if window_size > len(s2):
            return False
        target = [0] * 26
        window_letters = [0] * 26
        
        for c in s1:
            target[ord(c) - ord('a')] += 1

        for i in range(window_size):
            window_letters[ord(s2[i]) - ord('a')] += 1
        
        for i in range(window_size - 1, len(s2)):
            if i != window_size - 1:
                window_letters[ord(s2[i - window_size]) - ord('a')] -= 1
                window_letters[ord(s2[i]) - ord('a')] += 1
            
            if self.isPermu(target, window_letters):
                return True
        
        return False
        
    def isPermu(self, l1, l2):
        for i in range(26):
            if l1[i] != l2[i]:
                return False
        return True
        
        

