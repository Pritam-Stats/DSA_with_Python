# a = int(input("a= "))
# b = int(input("b= "))
# print("bin a =", bin(a)[2:])
# print("bin b =", bin(b)[2:])
# print(a&b)
# print(a|b)
# print(a^b)
# print(~a)

A = [1, 2, 4, 4]
B = [1, 2, 3, 4]

#and of A
ans = A[0]
for i in range(1, len(A)):
    ans &= A[i]

print(ans)