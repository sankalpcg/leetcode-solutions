class Solution:
    def isValid(self, s: str) -> bool:
        L = []
        for i in s:
            if i in "([{":
                L.append(i)
            else:
                if not L:  # empty stack -> invalid
                    return False
                if (i == ")" and L[-1] == "(") or (i == "]" and L[-1] == "[") or (i == "}" and L[-1] == "{"):
                    L.pop()
                else:
                    return False
        return not L
