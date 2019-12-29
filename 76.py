`class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not t or not s:
            return ""
        
        lens = len(s)
        lent = len(t)
        dict_t = {}
        for i in t:
            if i not in dict_t:
                dict_t[i] = 1
            else:
                dict_t[i] = dict_t[i] + 1
        required = len(dict_t)
        formed = 0
        window_counts = {}
        l, r = 0, 0
        ans = float("inf"), None, None

        while r < lens:
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed = formed + 1
            while l <= r and formed == required:
                character = s[l]
                if r - l + 1 < ans[0]:
                    ans = r - l + 1, l, r
                window_counts[character] = window_counts[character] - 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed = formed - 1
                
                l = l + 1
            r = r + 1
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]

        


sol = Solution()
s = "ADOBECODBAC"
t = "ABC"
#s = "abaa"
#t = "aba"

print sol.minWindow(s, t)