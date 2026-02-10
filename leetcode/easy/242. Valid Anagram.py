class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        ana_map1, ana_map2 = defaultdict(int), defaultdict(int)

        for (c1, c2) in zip(s, t):
            ana_map1[c1] += 1
            ana_map2[c2] += 1
        
        for key in ana_map1.keys():
            if ana_map1[key] != ana_map2[key]:
                return False
        
        return True
