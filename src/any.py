# Checking for negative values in a list
nums = [1, 2, 3, 4, 5, -42, 6, 7, 8]

# Inefficinet way 🤔 - Using a for loop and a flag ❌
contains_neg = False # flag
for num in nums:
    if num < 0:
        contains_neg = True


# Pythonic way 🐍 - Using the built-in "any" function ✅
contains_neg = any(num < 0 for num in nums) # True

# Bonus Tip 💡: Python also has a built-in "all" function ✅
contains_neg = not all(num >= 0 for num in nums) # True