
# [Bubble Sort](/bubble-sort.py)
- we take (n-1) turns.
- in each turn we move the large element to the end by swapping with the adjacent value
    <p align="center">
        <img src="BubbleSort.png" style="width: 50%; height: auto; border-radius: 10px;">
    </p>
- Dry run the code, it'll get more clear.
- TC: O$(n^2)$
- SC: O$(1)$

---

# [Selection Sort](/selection-sort.py)
- It's kind of opposite to Bubble Sort. Here we try to push the smallest to the beginning of the array.
- We imagine two parts of the array, `Unsorted` and `Sorted` part. in the beginning we have complete unsorted array.
- we pick the smallest from the unsorted array and swap with the sorted part of the array
  - So we have to find the min value from the unsorted part in each turn
- So in each turn we shrink our unsorted array.
- TC: O$(n^2)$
- SC: O$(1)$
---


---
> Note: We are not supposed to use these algorithms in problems, but we mainly study this to know the logic and code of the algorithms and these can be asked as a direct interview questions.