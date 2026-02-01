class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ["+","-","*","/"]
        for i in range(len(tokens)):
            if tokens[i] in ops:
                a = int(stack.pop(len(stack)-2))
                b = int(stack.pop(len(stack)-1))
                if(tokens[i] == "+"):
                    res = a+b
                elif(tokens[i]=="-"):
                    res=a-b
                elif(tokens[i]=="*"):
                    res=a*b
                else:
                    res=a/b
                stack.append(res)
            else:
                stack.append(tokens[i])
        return int(stack[0])
