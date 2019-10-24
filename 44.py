'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-10-24 20:25:43
@LastEditTime: 2019-10-24 21:15:15
@LastEditors: Please set LastEditors

字符串的模板匹配，实质为字符串之间的比较。当我们比较s[i]和p[j]是否能够匹配时，可以通过s[0..i-1]与p[0..j-1]的匹配关系来推导。

如果我们已经知道s[0..i-1]和p[0..j-1]的匹配关系时，就可以很容易推导出s[0..i]和p[0..j]的匹配关系。其递推公式为：

当p[j]为*时，由于*可以考虑为0~n个任意字符，因此分为3种不同的情况：

s[i-1]和p[j-1]进行匹配，s[i]和p[j]进行匹配。此时考虑*表示1个字符。
s[i-1]已经和p[j]进行了匹配，s[i]也仍然和p[j]进行匹配。此时考虑*表示n个字符。
s[i]和p[j - 1]进行了匹配，此时考虑*表示0个字符。
当p[j]为?时：

s[i-1]和p[j-1]进行匹配，s[i]和p[j]进行匹配。
当p[j]为字母时：

s[i-1]和p[j-1]进行匹配，s[i]和p[j]进行匹配。
若我们使用f[i][j]表示s[0..i]和p[0..j]是否能够匹配，则上面的递推关系可以表示为：
f[i][j] = f[i-1][j-1] | f[i-1][j] | f[i][j - 1] (p[j] == '*')
f[i][j] = f[i-1][j-1] (p[j] == '?')
f[i][j] = f[i-1][j-1] && p[j] == s[i] (others)

需要注意的是边界条件：
f[i][0] = false;
f[0][0] = true;

但是对于f[0][j]需要特殊处理，当p[j]为*，f[0][j]的值可以等于f[0][j-1]，此时将*考虑为0个字符。
最后根据f[s.size()][p.size()]的值就可以判定s和p是否能够匹配。

https://www.tianmaying.com/tutorial/LC44

做法2：
public boolean isMatch(String s, String p) {
		int i = 0, j = 0, match = 0, star = -1;		// i,j分别表示记录s与p的双指针
		while (i < s.length()) {
			if (j < p.length() && (p.charAt(j) == '?' || s.charAt(i) == p.charAt(j))) {  
				i++;
				j++;
			} else if (j < p.length() && p.charAt(j) == '*') { //这里'*'表示0个字符
				star = j; // 记录下此时'*'的位置信息，
				match = i;//此时对应的s的位置信息i
				j++;//继续往后
			} else if (star != -1) {  // 出现不匹配情况，回溯至'*'继续进行匹配  
				j = star + 1;   // 回溯到前面'*'处，继续进行匹配  
				i = ++match;  // 尝试s向前忽略一位，继续进行匹配  
			} else return false;// 完全不匹配情况
		}
		while (j < p.length() && p.charAt(j) == '*') j++;
		return j == p.length();
	}
'''
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        slen, plen = len(s), len(p)
        #print "**", slen, plen
        dp = [[ False for j in range(plen + 1)] for i in range(slen + 1)]
        dp[0][0] = True

        for i in range(1, plen + 1):
            if p[i-1] == '*':
                dp[0][i] = dp[0][i - 1]
            else:
                dp[0][i] = False

        #now = 0
        for i in range(1, slen+1):
            #dp[i-1][0] = False
            for j in range(1, plen+1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i-1][j-1] or dp[i][j-1] or dp[i-1][j]
                elif p[j - 1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                else:
                    #print i, j
                    dp[i][j] = dp[i-1][j-1] and (s[i - 1] == p[j - 1])
                
        return dp[slen][plen]

if __name__ == '__main__':
    s = 'acdcb'
    p = '*a*?b'
    sol = Solution()
    print sol.isMatch(s, p)