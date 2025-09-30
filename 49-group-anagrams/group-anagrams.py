class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l = []
        key = []
        used = set()   # better than a list for lookup O(1)

        # store string version of sorted word
        for i in strs:
            key.append("".join(sorted(i)))

        for i in range(len(key)):
            if i in used:   # skip if already grouped
                continue
            temp = [strs[i]]
            used.add(i)

            for j in range(i + 1, len(key)):
                if key[i] == key[j] and j not in used:
                    temp.append(strs[j])
                    used.add(j)

            l.append(temp)
        return l
