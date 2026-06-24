class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        track = {}

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1
            
            count = tuple(count)

            if count in track:
                track[count].append(s)
            else:
                track[count] = [s]
        
        res = []
        for count in track:
            res.append(track[count])
        
        return res
