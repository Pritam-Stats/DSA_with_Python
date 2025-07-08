def decodeStr(s: str) -> str:
    stack = []
    for ch in s:
        if ch != "]":
            stack.append(ch)
        else:
            decodeStr = ''
            while stack[-1] != '[':
                decodeStr = stack.pop() + decodeStr
            stack.pop()

            num = ''
            while stack and stack[-1].isdigit():
                num = stack.pop() + num

            stack.append(int(num) * decodeStr)

    return ''.join(stack)
            





if __name__ == "__main__":
    print(decodeStr(s = "3[a2[c]]"))    #accaccacc
    print(decodeStr(s = "3[a]2[bc]"))    #aaabcbc
    print(decodeStr(s = "2[abc]3[cd]ef"))    #"abcabccdcdcdef"