
- **Problem Link** : [205. Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/)
- **Solved** : July 20, 2025 | 10:38 PM
- **Topic** : [[Strings]]
- **Difficulty** : #Easy

---

### Summary Description:

- Determine whether two strings `s` and `t` are isomorphic — meaning there exists a one-to-one mapping between characters of `s` and `t` that preserves order and uniqueness.
- No two different characters in `s` may map to the same character in `t`, but a character may map to itself.

---

## Strategy & Key Insights

- Iterate through both strings simultaneously.
- Use two hash maps to record mappings `s → t` and `t → s` to enforce bijection.
- At each character position, verify that the current mapping is consistent with the previous mappings.
- If any inconsistency is found (either direction), conclude that the strings are not isomorphic.
- This ensures the mapping is injective and surjective in the context of the given strings.

---

## PseudoCode (Optimal)

```
function isIsomorphic(s, t):
    if length of s != length of t:
        return False

    create empty map s_to_t
    create empty map t_to_s

    for each pair of characters (c1, c2) in s and t:
        if c1 is already mapped in s_to_t:
            if s_to_t[c1] != c2:
                return False
        else:
            s_to_t[c1] = c2

        if c2 is already mapped in t_to_s:
            if t_to_s[c2] != c1:
                return False
        else:
            t_to_s[c2] = c1

    return True
```
