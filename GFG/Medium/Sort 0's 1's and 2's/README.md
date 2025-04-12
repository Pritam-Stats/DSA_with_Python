
# 🚩 Sort 0s, 1s, and 2s – Dutch National Flag Problem

## 📚 Problem Statement

Given an array `arr[]` consisting of only `0`s, `1`s, and `2`s, the task is to **sort the array in ascending order**.

### 🔒 Constraints

- Only the numbers 0, 1, and 2 are allowed in the array.
- You **cannot** use built-in sorting functions.

---

## ✅ Objective

Transform an unsorted array like:

```
Input:  [2, 0, 1, 2, 1, 0]
Output: [0, 0, 1, 1, 2, 2]
```

---

## 🧠 Approach: Dutch National Flag Algorithm

This is a famous algorithm designed by Edsger Dijkstra. The idea is to sort the array in **one pass** (i.e., only going through the array once) using **three pointers**:

### 🔁 Key Pointers

- `low`: Marks the boundary of `0`s
- `mid`: Scans the array
- `high`: Marks the boundary of `2`s

### 🧮 The Four Regions

During the sorting process, the array is conceptually divided into:

```
[0s zone] [1s zone] [unknown zone] [2s zone]
 ^        ^         ^              ^
 |        |         |              |
start     low       mid            high
```

---

## 🔄 Algorithm Steps

1. Initialize:
   ```python
   low = 0
   mid = 0
   high = len(arr) - 1
   ```

2. Loop while `mid <= high`:
   - If `arr[mid] == 0`:
     - Swap with `arr[low]`
     - Move `low++` and `mid++`
   - If `arr[mid] == 1`:
     - Just move `mid++`
   - If `arr[mid] == 2`:
     - Swap with `arr[high]`
     - Move `high--`
     - **Do NOT move `mid` yet** — re-check the swapped value


---

## 🧪 Example Run

```python
arr = [2, 0, 1, 2, 1, 0]
print(sort012(arr))  # Output: [0, 0, 1, 1, 2, 2]
```

---

## 📌 Why Does It Work?

The algorithm ensures:
- All `0`s are pushed to the beginning.
- All `2`s are pushed to the end.
- All `1`s stay in the middle.

By doing **careful swaps** and **controlling pointer movements**, we correctly sort the array in just **one pass**.

---

## 🏁 Time & Space Complexity

- **Time Complexity:** `O(n)` — one traversal of the array.
- **Space Complexity:** `O(1)` — no extra space used.

