<img src="K-thFactor.png" alt="Your long page image" style="max-width: 100%; border-radius: 10%; display: block; margin-left: auto; margin-right: auto;">

Link: https://codeforces.com/group/4vcXCPx8NY/contest/676977/problem/H
Solution: [K-th Factor](returnK-thFactor.py)

## Brute
- run a O(n) loop store the factors and return the k-th
  - But O(N) TC won't be accepted here since $n <= 10^12$

## Better
- Run a loop till $\sqrt{n}$, $ d \in [1, \sqrt{n}]$, store the factors as ${d}$ and $n//d$
- Sort the factors array
- return the k-th factor
- TC: O$(\sqrt{n} + m \log_{2} m)$
- SC: O(m)

## Optimal
- TC: O$(\sqrt{n})$
- SC: O(1)
- Run the first half the loop in forward, let for n == 12; store the factors d, as 1, 2, 3
- Then run a second O$(\sqrt{n})$ loop in backward order from, $d \in [\sqrt{n}, 1]$ and the factors will be $n//d$.
- Don't store the factors but keep a counter; when counter reach k return d if in the first loop or n//d if in the second loop