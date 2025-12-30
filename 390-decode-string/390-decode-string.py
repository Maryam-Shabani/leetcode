class Solution:
    def decodeString(self, s: str) -> str:
        decoded_string = []
        i = 0
        while i < len(s):
            if s[i].isalpha():
                decoded_string.append(s[i])
                i +=1
            elif s[i].isdigit():
                k = [s[i]]
                i += 1
                while s[i].isdigit():
                    k.append(s[i])
                    i += 1
                decoded_string.append(''.join(k))
            elif s[i] ==']':
                j = -1
                repeated_string = []
                while not decoded_string[j].isnumeric():
                    repeated_string.append(decoded_string.pop())
                k = int(decoded_string.pop())
                rstring = ''.join(repeated_string[j] for j in range(-1, -len(repeated_string)-1, -1))
                decoded_string.append(rstring * k)
                i += 1
            else:
                i += 1
        return ''.join(decoded_string)