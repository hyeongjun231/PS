class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ''
        if t == s:
            return t

        start, end = 0, 0
        min_length = float('inf')
        letters_set = set(t)
        letters_cnt = defaultdict(int)
        window_cnt = defaultdict(deque)
        
        for c in t:
            letters_cnt[c] += 1

        for i in range(len(s)):
            c = s[i]
            if c in letters_set:
                window_cnt[c].append(i)
                if len(window_cnt[c]) > letters_cnt[c]:
                    window_cnt[c].popleft()

                if self.isValid(letters_cnt, window_cnt):
                    min_start = self.getMinStart(window_cnt)
                    cur_length = i - min_start
                    if min_length > cur_length:
                        start = min_start
                        end = i + 1
                        min_length = cur_length        

        return s[start:end]

    def isValid(self, target, window):
        if len(window.keys()) != len(target.keys()):
            return False

        for key in target.keys():
            if len(window[key]) != target[key]:
                return False
        
        return True
    
    def getMinStart(self, window):
        min_start = float('inf')
        for deq in window.values():
            min_start = min(min_start, deq[0])
        return min_start
