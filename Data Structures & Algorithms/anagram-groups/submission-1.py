class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sublist = []
        while len(strs) != 0:
            i = 0
            if len(sublist) == 0:
                sublist.append([strs[i]])
                strs = strs[1:]
                continue

            for j in range(len(sublist)):
                inserted = False
                if self.isAnagrams(sublist[j][0], strs[i]):
                    sublist[j].append(strs[i])
                    inserted = True
                    break

            if inserted == False:
                sublist.append([strs[i]])

            strs = strs[1:]

        return sublist

    def isAnagrams(self, str1: str, str2: str) -> bool:
        if len(str1) != len(str2):
            return False

        sorted1 = sorted(str1)
        sorted2 = sorted(str2)
         
        if (sorted1 == sorted2):
            return True

        else: 
            return False

