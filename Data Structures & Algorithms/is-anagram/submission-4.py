class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_track = {}
        t_track = {}
        N = len(s)

        for i in range(N):
            s_track[s[i]] = s_track.get(s[i], 0) + 1
            t_track[t[i]] = t_track.get(t[i], 0) + 1

        return s_track == t_track
        