## **📁 Complete File (Copy-Paste Ready)**
```python
# DAY 3: Contains Duplicate
def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

print(containsDuplicate([1,2,3,1]))  # True
print(containsDuplicate([1,2,3,4]))  # False

# DAY 4: Valid Anagram
def isAnagram(s, t):
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)

print(isAnagram("anagram", "nagaram"))  # True
print(isAnagram("rat", "car"))         # False
