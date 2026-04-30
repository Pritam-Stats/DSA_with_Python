Quick Revision Notes


1. Mathematics

Modular Arithmetic

* (a + b) % m = ((a % m) + (b % m)) % m
* (a - b) % m = ((a % m) - (b % m) + m) % m
* (a * b) % m = ((a % m) * (b % m)) % m
* Fast exponentiation: O(log n)

def mod_exp(a, b, m):
    res = 1
    a %= m
    while b:
        if b & 1:
            res = (res * a) % m
        a = (a * a) % m
        b >>= 1
    return res

Modular Inverse

* Fermat (m prime): a^(m-2) % m

GCD / LCM

* gcd(a, b)
* lcm(a, b) = (a * b) // gcd(a, b)

Prime Numbers

* Sieve: O(n log log n)
* Prime factorization: O(sqrt(n))

⸻

2. Bit Manipulation

* Check power of 2: n & (n-1) == 0
* Lowest set bit: n & -n
* Count set bits: builtin or loop
* XOR properties:
    * a ^ a = 0
    * a ^ 0 = a

⸻

3. Arrays & Prefix Sum

* Prefix sum: O(n)
* Range sum: prefix[r] - prefix[l-1]

⸻

4. Sliding Window / Two Pointer

* Fixed window: O(n)
* Variable window: expand + shrink

⸻

5. Binary Search

* Condition-based search
* Mid = l + (r - l) // 2
* Time: O(log n)

⸻

6. Sorting

* Built-in: O(n log n)
* Custom comparator / key

⸻

7. Recursion & Backtracking

* Base case + choice + backtrack

⸻

8. Dynamic Programming

* Top-down (memoization)
* Bottom-up (tabulation)
* State definition is key

Common patterns:

* Knapsack
* LIS
* LCS

⸻

9. Graphs

BFS

* Shortest path (unweighted)
* Queue

DFS

* Components, cycles

Dijkstra

* Weighted shortest path
* Priority queue

Union Find (DSU)

* Path compression + union by rank

⸻

10. Trees

* DFS traversal: inorder, preorder, postorder
* Height, diameter

⸻

11. Strings

* KMP: pattern matching O(n)
* Z-algorithm

⸻

12. Complexity Cheatsheet

* O(1): constant
* O(log n): binary search
* O(n): linear scan
* O(n log n): sorting
* O(n^2): nested loops

⸻

13. STL / Python Builtins

* heapq (priority queue)
* bisect (binary search)
* collections (Counter, deque)

⸻

14. Common Tricks

* Coordinate compression
* Meet in the middle
* Greedy choice property

⸻

---








---

# Data Structures

This folder contains all major data structures required for technical interviews, competitive programming, and advanced problem solving.

Each structure is studied in three layers:

1. **Concept** – How it works internally
2. **Operations** – Core manipulations
3. **Problem Patterns** – How it appears in interview questions

Mastery requires both understanding and implementation discipline.

---

# Folder Structure

```
structures/
│
├── Arrays/
├── Strings/
├── Linked-List/
├── Stack/
├── Queue/
├── Hashing/
├── Heap/
├── Trees/
├── Graphs/
├── Trie/
├── Disjoint_set/
├── Segment_tree/
└── DP/
```

---

# 1️⃣ Arrays

## Introduction

Arrays store elements in contiguous memory and allow constant-time indexing.
They form the foundation of most interview problems.

## Learning Plan

### Stage 1 – Basics

* Traversal
* Reverse array
* In-place updates
* Subarrays

### Stage 2 – Core Techniques

* Two Pointers
* Sliding Window (fixed & variable)
* Prefix Sum
* Binary Search
* Kadane’s Algorithm
* Hashing with arrays

### Stage 3 – Advanced Patterns

* Monotonic Stack
* Heap on arrays
* Greedy with sorting
* Binary search on answer

---

# 2️⃣ Strings

## Introduction

Strings are character arrays with pattern-matching and frequency-based constraints.

## Learning Plan

### Stage 1 – Basics

* Character frequency
* Palindromes
* Substrings

### Stage 2 – Techniques

* Sliding Window
* Two Pointers
* Hashing
* Anagram detection

### Stage 3 – Advanced

* KMP
* Rolling Hash
* String DP problems

---

# 3️⃣ Linked List

## Introduction

Linked lists connect nodes via pointers instead of contiguous memory.

## Learning Plan

### Stage 1 – Basics

* Node structure
* Traversal
* Reverse list

### Stage 2 – Pointer Techniques

* Fast & Slow Pointer
* Cycle detection
* Merge two lists
* Middle node

### Stage 3 – Advanced

* LRU Cache concept
* Linked list sorting
* Deep copy with random pointer

---

# 4️⃣ Stack

## Introduction

Stack follows LIFO (Last In, First Out).

## Learning Plan

### Stage 1 – Basics

* Push / Pop
* Valid parentheses

### Stage 2 – Applications

* Next Greater Element
* Stock Span
* Expression evaluation

### Stage 3 – Advanced

* Monotonic stack
* Largest rectangle in histogram

---

# 5️⃣ Queue

## Introduction

Queue follows FIFO (First In, First Out).

## Learning Plan

### Stage 1 – Basics

* Enqueue / Dequeue

### Stage 2 – Applications

* BFS
* Level order traversal
* Sliding window maximum (deque)

### Stage 3 – Advanced

* Circular queue
* Double-ended queue applications

---

# 6️⃣ Hashing

## Introduction

Hashing provides average O(1) lookup using hash functions.

## Learning Plan

### Stage 1 – Basics

* Frequency maps
* Duplicate detection

### Stage 2 – Array Integration

* Two Sum
* Subarray sum = K
* Longest consecutive sequence

### Stage 3 – Advanced

* Custom hashing
* Hash collisions (conceptual)

---

# 7️⃣ Heap (Priority Queue)

## Introduction

Heap is a complete binary tree used to efficiently retrieve min/max elements.

## Learning Plan

### Stage 1 – Basics

* Min heap / Max heap
* Heap operations

### Stage 2 – Applications

* Top K elements
* Kth largest
* Merge K sorted lists

### Stage 3 – Advanced

* Heap + Greedy
* Scheduling problems

---

# 8️⃣ Trees

## Introduction

Trees are hierarchical structures with parent-child relationships.

## Learning Plan

### Stage 1 – Basics

* Binary Tree traversal (DFS/BFS)
* Height / Depth

### Stage 2 – Binary Search Tree

* Insert / Delete
* Validate BST
* LCA

### Stage 3 – Advanced

* Diameter
* Tree DP
* Path sum problems

---

# 9️⃣ Graphs

## Introduction

Graphs represent relationships between entities.

## Learning Plan

### Stage 1 – Basics

* Graph representation
* BFS
* DFS

### Stage 2 – Core Algorithms

* Topological Sort
* Cycle detection
* Connected components
* Union-Find

### Stage 3 – Advanced

* Dijkstra
* Bellman-Ford
* Minimum Spanning Tree

---

# 🔟 Trie

## Introduction

Trie is a tree-like structure used for prefix-based search.

## Learning Plan

* Insert
* Search
* Prefix queries
* Word search problems

---

# 1️⃣1️⃣ Disjoint Set (Union-Find)

## Introduction

Data structure for tracking connected components.

## Learning Plan

* Union
* Find
* Path compression
* Cycle detection in graphs

---

# 1️⃣2️⃣ Segment Tree / Fenwick Tree (Advanced / CP)

## Introduction

Used for efficient range queries and updates.

## Learning Plan

* Build tree
* Range sum query
* Range update
* Lazy propagation (advanced)

---

# 1️⃣3️⃣ Dynamic Programming (Problem Structure Category)

## Introduction

Technique for solving overlapping subproblems using stored results.

## Learning Plan

### Stage 1 – Basics

* Fibonacci
* Climbing stairs

### Stage 2 – Classic Patterns

* 0/1 Knapsack
* LIS
* LCS
* Subset sum

### Stage 3 – Advanced

* DP on trees
* Bitmask DP
* Matrix chain multiplication

---

# How To Study Each Structure

For every structure:

1. Understand internal working
2. Implement from scratch
3. Learn standard algorithms
4. Solve representative problems
5. Maintain short summary in README
6. Track common mistakes

---

# Interview Priority Order

High Priority:

* Arrays
* Strings
* Hashing
* Stack
* Binary Search
* Trees
* Graph BFS/DFS
* Basic DP

Advanced / CP-Focused:

* Trie
* Segment Tree
* Advanced graph algorithms

---

# Goal

* Recognize patterns quickly
* Implement efficiently
* Avoid common edge-case mistakes
* Build structured thinking

Mastery of these structures ensures strong performance in interviews and competitive programming.

---
