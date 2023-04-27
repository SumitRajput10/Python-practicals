# class Parentheses:
#     def generate(self, n: int) -> list[str]:

#      stack = []
#      res = []

#     def last(open, close):
#         if open == close == n:
#             res.append("".join(stack))
#             return
        
#         if open < n:
#             stack.append("(")
#             last(open + 1, close)
#             stack.pop()

#         if close < open:
#             stack.append(")")
#             last(open, close + 1)
#             stack.pop()

# last(0,0)
# retun res

def parentheses(n, open, close, s, ans):
    
    if(open == n and close == n):
        ans.append(s)
        return
    
    if(open < n):
        parentheses(n, open + 1, close, s+"(",ans)

    if(close < open):
        parentheses(n, open, close + 1, s+")",ans)

try:
    n = int(input("Enter Number : "))
    if n not in range(1, 9):
        raise ValueError
    else:
        ans =[ ]
        parentheses(n, 0, 0, "", ans)
        print(ans)
except ValueError:
    print("Enter Value range between 1 to 8")


