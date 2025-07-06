def evalRPN(tokens):
    stack = []

    for token in tokens:
        if token in "+-*/":
            b = stack.pop() #second operand
            a = stack.pop() #first operand

            if token == '+':
                stack.append(a+b)
            elif token == '-':
                stack.append(a-b)

            elif token == '*':
                stack.append(a*b)

            else:
                stack.append(int(a/b))

        else:
            stack.append(int(token))
    return stack[-1]




if __name__ == "__main__":
    print(evalRPN(["2","1","+","3","*"]))   #9
    print(evalRPN(["4","13","5","/","+"]))  #6