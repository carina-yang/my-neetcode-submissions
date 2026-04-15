class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        maps = []
        for s in strs:
            s_map = {}
            for i in s:
                if i in s_map:
                    s_map[i] += 1
                else:
                    s_map[i] = 1
            if s_map in maps:
                res[maps.index(s_map)].append(s)
            else:
                res.append([s])
                maps.append(s_map)
        
        return res

