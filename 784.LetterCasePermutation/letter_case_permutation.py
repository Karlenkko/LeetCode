class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        result = []
        size = len(S)
        self.__recAdd(S, result, size, 0)
        result = set(result)
        result.add(S)
        result = list(result)
        return result


    def __recAdd(self, S: str, l: List[str], size, index) :
        if index == size :
            return 0
        if S[index].isalpha() :
            l.append(S)
            temp = list(S)
            temp[index] = chr(ord(S[index]) ^ (1 << 5))
            temp = ''.join(temp)
            l.append(temp)
            self.__recAdd(temp, l, size, index + 1)
        self.__recAdd(S, l, size, index + 1)
