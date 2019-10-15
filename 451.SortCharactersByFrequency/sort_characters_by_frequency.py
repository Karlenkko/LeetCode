class Solution:
    def frequencySort(self, s: str) -> str:
        mydict = dict()
        result = ''
        for item in s :
            if item in mydict :
                mydict[item] += 1
            else :
                mydict[item] = 1
        mydict = sorted(mydict.items(), key = lambda x: x[1], reverse = True)
        for key , value in mydict :
                result += key * value
        return result        
