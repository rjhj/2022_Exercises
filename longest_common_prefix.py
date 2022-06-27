# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

class Solution:

    def findShortestWord(self, strs):
        shortestLength = len(strs[0])
        shortestWordIndex = 0
        numberOfStrings = len(strs)
        i = 1
        while i < numberOfStrings:
            if shortestLength > len(strs[i]):
                shortestLength = len(strs[i])
                shortestWordIndex = i
            i += 1
        return shortestWordIndex, shortestLength
          
    def longestCommonPrefix(self, strs: list[str]) -> str:
        shortestWordIndex, shortestLength = self.findShortestWord(strs)
        shortestWord = strs[shortestWordIndex]
        strs.pop(shortestWordIndex)
        prefixLength = 0
        indexOfLetters = 0
        numberOfWords = len(strs)
        while indexOfLetters < shortestLength:
            indexOfWords = 0
            while indexOfWords < numberOfWords:
                 if shortestWord[indexOfLetters] != strs[indexOfWords][indexOfLetters]:
                    return shortestWord[0:indexOfLetters]
                 indexOfWords += 1
            indexOfLetters += 1
        return shortestWord[0:indexOfLetters]




solver = Solution()

# Test data
testList = [["flower","flow","flight"], ["dog","racecar","car"], ["milk","milk","m"], ["12345678","123456","1234567"]]
expectedResult = ["fl", "", "m", "123456"]

i = 0
lenOfTestList = len(testList)
while i < lenOfTestList:
    result = solver.longestCommonPrefix(testList[i])
    print(result == expectedResult[i])
    i += 1