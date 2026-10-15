class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += "#" + str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        
        i = 0
        while i < len(s):
            if s[i] == "#":
                a = i + 1
                word_len = ""

                while ord("0") <= ord(s[a]) <= ord("9"):
                    word_len += s[a]
                    a += 1

                if s[a] != "#":
                    continue

                res.append(s[a + 1: a + int(word_len) + 1])
                i = a + int(word_len) + 1
        
        return res
            
