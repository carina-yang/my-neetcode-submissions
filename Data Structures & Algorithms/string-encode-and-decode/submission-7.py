class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += '*' + str(len(s)) + '*' + s
        return res

    def decode(self, s: str) -> List[str]:
        print(s)
        res = []
        i = 0
        while i < len(s):
            print(i)
            if s[i] == '*':
                i += 1
                num = ""
                while s[i] != '*':
                    num += s[i]
                    i += 1
                length = int(num)
                res.append(s[i+1:i+1+length])
                i = i + 1 + length
        return res
