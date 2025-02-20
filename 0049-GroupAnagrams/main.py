class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = defaultdict(list) # mapping char count to list if anagrams
        
        for string in strs:
            count = [0] * 26 # a .... z i.e. 26 char

            for char in string:
                count[ord(char) - ord("a")] += 1
            
            result[tuple(count)].append(string)
        
        return result.values()