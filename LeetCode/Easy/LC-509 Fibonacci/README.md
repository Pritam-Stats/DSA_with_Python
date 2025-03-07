# Majority Element LC-169

Concepts: Arrays <br>
Difficulty: Easy <br>
Problem Link: https://leetcode.com/problems/majority-element/description/
<br>
Solved Date: March 5, 2025

## The Voting Problem - Majority Element

Given an Array. We have to return the element which occurs the max number of time.

Highest Frequency ⇒ Mode. Or in the question it has given that the max number will **occur more than n/2 times**. This problem assumes there is an unique majority element exist.

**inputs :**

[1,1,2,2,3,3,2] → 2 #this is not a valid input for this problem

[4,4,4,5,7,5] → 4

### One line solution in Python

```python
from statistics import mode
mode(arr)
```

this could have done the job. This also has 0(n) TC.

**But to understand the concept:**

### **General Brute Force**

1. for each value in the array count frequency and return the value which has freq > n/2
2. sort the array. count freq for each value, if freq is not > n/2 leave that value and count for the next value.

## Moore’s Voting Algo

- Iterate over all the numbers
  - for each number have a count
  - and whenever it is the same number increase the count
  - else decrease the count by 1
    - Now why to decrease?
      - See think of each number as a potential _candidate_ to be the majority.
      - So whenever we are getting the same number (imagine each count as a vote) we’re simply increasing the count
      - But if in case of a new candidate (imagine as a competitor) get a vote but if it still has lesser vote than the previous candidate we can just cancel out the votes because one is still has the **Majority.**
      - Now in case if we get back to 0, this means another candidate’s votes are equal and fully canceled out all the votes, then we can simply change the candidate according to the next.
  ```python
  # LC-169
  def majorityElement(nums : list) -> int:
      candidate = None    #no candidate at the beginning | each num is a candidate
      votes = 0   #no votes yet
      for num in nums:
          if votes == 0:  #think like a base case, when the vote became 0 for a candidate, assign a new candidate
              candidate = num
          votes += (1 if num == candidate else -1)    #otherwise when vote is non zero keep on updating the vote

      return candidate    # which will remain at the end

  print(majorityElement(nums = [1,1,2,2,2,3,2]))
  ```
  O(n), O(1)
  ```cpp
  #include <iostream>
  #include <vector>
  using namespace std;

  int majorityElement(vector<int> &nums)
  {
      int candidate = 0; // No candidate initially
      int votes = 0;     // No votes yet

      for (int num : nums)
      {
          if (votes == 0)
          { // When votes drop to 0, assign a new candidate
              candidate = num;
          }
          votes += (num == candidate) ? 1 : -1; // Update votes
      }

      return candidate; // The majority element
  }

  int main()
  {
      vector<int> nums = {1, 1, 2, 2, 2, 3, 2};
      cout << "Majority Element: " << majorityElement(nums) << endl;
      return 0;
  }
  ```
