class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        f=Counter(s)
        m=Counter(t)
        return f==m