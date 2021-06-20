def pairs(open,close):
    if open =='[' and close==']':
        return True
    if open =='(' and close==')':
        return True
    if open =='{' and close=='}':
        return True
    return False

def balance(A):
    stack=[]
    for i in range(len(A)):
        if A[i]=='[' or A[i]=='{' or A[i]=='(':
            stack.append(A[i])
        elif A[i]==']' or A[i]=='}' or A[i]==')':
            if pairs(stack[-1],A[i] or len(stack)!=0):
                stack.pop()
            else:
                    return False
    if len(stack)==0:
        return True
    else:
        return False
                


A=input("Enter the parenthesis:")
print(balance(A))
