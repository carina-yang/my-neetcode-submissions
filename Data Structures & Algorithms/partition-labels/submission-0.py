class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        track = [set(s[0])]
        seen = set(s[0])
        result = [1]
        for i in range(1, len(s)):
            if s[i] in seen:
                j = len(track) - 1
                while s[i] not in track[j]:
                    a = result.pop()
                    b = track.pop()
                    result[-1] += a
                    track[-1] = track[-1] | b
                    j -= 1
                result[-1] += 1
            else:
                track.append(set(s[i]))
                result.append(1)
                seen.add(s[i])
        return result