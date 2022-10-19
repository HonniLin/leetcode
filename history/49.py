'''
@Author: your name
@Date: 2019-11-04 21:29:11
@LastEditTime: 2019-11-04 22:27:09
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode/49.py
排序后归类
'''
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans, res, ret = [], {}, []
        for s in strs:
            temp = list(s)
            temp.sort()
            ans.append("".join(temp))
        print ans
        for i in range(len(ans)):
            if ans[i] not in res:
                res[ans[i]] = []
            res[ans[i]].append(strs[i])
        for key in res:
            ret.append(res[key])
        return ret
        
if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    #strs = ["hos","boo","nay","deb","wow","bop","bob","brr","hey","rye","eve","elf","pup","bum","iva","lyx","yap","ugh","hem","rod","aha","nam","gap","yea","doc","pen","job","dis","max","oho","jed","lye","ram","pup","qua","ugh","mir","nap","deb","hog","let","gym","bye","lon","aft","eel","sol","jab"]
    sol = Solution()
    print sol.groupAnagrams(strs)