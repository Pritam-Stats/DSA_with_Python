def addBinary(s1, s2):
    # Initialize two pointers at the end of each string
    i, j = len(s1) - 1, len(s2) - 1

    # This will keep track of carry from previous addition
    carry = 0

    # List to store result bits (we'll reverse it later)
    result = []

    # Loop until all bits are processed or there's a carry
    while i >= 0 or j >= 0 or carry:
        total = carry  # Start with the carry from previous addition

        # If s1 still has bits left, add to total
        if i >= 0:
            total += int(s1[i])
            i -= 1  # Move to the next bit (left)

        # If s2 still has bits left, add to total
        if j >= 0:
            total += int(s2[j])
            j -= 1  # Move to the next bit (left)

        # total % 2 gives the current result bit (either 0 or 1)
        result_bit = str(total % 2)

        # Update carry for next iteration (can be 0 or 1)
        carry = total // 2

        # Print the internal state for debugging
        # print(f"Adding: total={total}, bit={result_bit}, carry={carry}")

        # Append current bit to the result
        result.append(result_bit)

    # Reverse the result list and join it into a string
    final_result = ''.join(reversed(result))

    # Remove any leading zeros (e.g., "00101" → "101")
    final_result = final_result.lstrip('0')

    # If the result becomes empty (like "0000"), return "0"
    return final_result if final_result else "0"


print(addBinary("11", "1"))          # Output: 100
print(addBinary("1010", "1011"))     # Output: 10101
print(addBinary("0000", "0000"))     # Output: 0
print(addBinary("0011", "0001"))     # Output: 100
print(addBinary("111", "111"))       # Output: 1110
print(addBinary("0", "0"))           # Output: 0
print(addBinary("1", "111111"))      # Output: 1000000
print(addBinary("100", "110010"))    # Output: 110110
print(addBinary("101", "11001"))     # Output: 11110
print(addBinary("000001", "000011")) # Output: 100