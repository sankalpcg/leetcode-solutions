class Solution:
    def convert(self, s: str, numRows: int) -> str:
            if numRows == 1: return s

            rows = [""] * numRows
            controller = True
            tracker = 0

            for letter in s:
                rows[tracker] += letter
                if tracker == numRows - 1: controller = False
                if tracker == 0: controller = True
                if controller: tracker += 1
                else: tracker -= 1

            converted_string = ""

            for word in rows:
                converted_string += word
                
            return converted_string