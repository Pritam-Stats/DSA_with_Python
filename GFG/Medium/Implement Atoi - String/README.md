# Implement Atoi (String to Integer Conversion)

## 🧠 Problem Summary
Convert a given string to a 32-bit signed integer similar to `atoi()` in C/C++.

## ✅ Key Steps
1. **Skip leading whitespaces**
2. **Handle optional sign (`+` or `-`)**
3. **Convert numeric characters into integer**
4. **Stop parsing at non-digit**
5. **Clamp result within 32-bit signed int range** (`[-2^31, 2^31 - 1]`)

## 🔍 Things to Remember
- You can use `s[idx].isdigit()` instead of `'0' <= s[idx] <= '9'` for readability.
- `ord(char)` gives the ASCII value of a character.
  - So `ord('5') - ord('0') = 5` — a low-level way to convert character to digit.
- Use `int(s[idx])` in Python for clean and direct conversion.

## ⏱️ Time & Space Complexity
- **Time:** O(n)
- **Space:** O(1)

## 💡 C++ Version

```cpp
int myAtoi(string s) {
    int i = 0, n = s.length(), sign = 1;
    long res = 0;

    // Skip whitespaces
    while (i < n && s[i] == ' ') i++;

    // Sign check
    if (i < n && (s[i] == '+' || s[i] == '-')) {
        sign = (s[i] == '-') ? -1 : 1;
        i++;
    }

    // Convert digits
    while (i < n && isdigit(s[i])) {
        res = res * 10 + (s[i] - '0');

        if (res > INT_MAX)
            return (sign == 1) ? INT_MAX : INT_MIN;

        i++;
    }

    return sign * res;
}