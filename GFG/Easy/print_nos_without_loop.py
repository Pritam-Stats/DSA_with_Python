'''
Print numbers from 1 to n without the help of loops. You only need to complete the function printNos() that takes n as a parameter and prints the number from 1 to n recursively.

TC = 0(n), SC = O(n)

1 <= n <= 1000
'''

def printNos(n: int):
    if n == 0:
        return
    printNos(n - 1) #recursion step
    print(n, end = " ") #first time this line will run when n == 0, the code will stop

(printNos(5))





# When we reach the base case, we start returning from each function call in the reverse order (this is the key part of recursion). The function calls resumes one by one which has been waiting for another call

# Time Complexity: O(n) - The function makes n recursive calls, so the execution time grows linearly.

# Space Complexity: O(n) - Each recursive call takes stack space, and there are n calls before returning.


'''
**Dry Run for n = 5**

printNos(5)
    ├── printNos(4)
    │   ├── printNos(3)
    │   │   ├── printNos(2)
    │   │   │   ├── printNos(1)
    │   │   │   │   ├── printNos(0) → returns
    │   │   │   │   ├── print(1)
    │   │   │   ├── print(2)
    │   │   ├── print(3)
    │   ├── print(4)
    ├── print(5)
'''


'''
# Call Stack - Each function call is pushed onto the stack until we reach the base case. Then, the functions start returning one by one, printing n in the correct order.


printNos(5)
├── printNos(4)
│   ├── printNos(3)
│   │   ├── printNos(2)
│   │   │   ├── printNos(1)
│   │   │   │   ├── printNos(0)  <-- Base case, stops recursion

---------------------------------------------------------------------------------------------

printNos(1) → prints "1"
printNos(2) → prints "2"
printNos(3) → prints "3"
printNos(4) → prints "4"
printNos(5) → prints "5"

'''

'''
def printNosReverse(n: int):
    if n == 0:
        return
    print(n, end=" ")  # Print first before recursive call
    printNosReverse(n - 1)
'''