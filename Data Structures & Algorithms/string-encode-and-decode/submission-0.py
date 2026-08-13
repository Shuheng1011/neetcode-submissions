class Solution:

    def encode(self, strs: List[str]) -> str:
        string =''
        for i in range(len(strs)):
            length = len(strs[i])
            string = string + str(length) + '#' + strs[i]
        return string
    def decode(self, s: str) -> List[str]:
        decoded = []
        while len(s) != 0:
            # get number
            num = ''
            while s[0] != '#':
                num = num + s[0]
                s = s[1:]
            num = int(num)

            s = s[1:]

            decoded_wrd = ''
            for i in range(num):
                decoded_wrd = decoded_wrd + s[0]
                s = s[1:]

            decoded.append(decoded_wrd)
            decoded_wrd = ''

        return decoded
