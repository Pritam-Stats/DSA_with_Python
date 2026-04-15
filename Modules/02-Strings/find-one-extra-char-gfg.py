

'''
    Problem: https://practice.geeksforgeeks.org/contest/code-catalyst/problems
'''

'''
// User function Template for javascript

class Solution {
    extraChar(s1, s2) {
        // write your code here
        const freq = new Map();

        for (let ch of s1) {
            freq.set(ch, (freq.get(ch) || 0) + 1);
        }

        for (let ch of s2) {
            if (!freq.has(ch) || freq.get(ch) === 0) {
                return ch;
            }

            freq.set(ch, freq.get(ch) - 1);
        }

    }
}

'''

def extraChar(s1, s2):
    freq = {}
    for ch in s1:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in s2:
        if ch not in freq or freq[ch] == 0:
            return ch

        freq[ch] -= 1


