# OK version 🤔 - For loop and append ❌ 
squares = []
for num in range(12):
    squares.append(num ** 2)

# Pythonic version 🐍: Use a list comprehension ✅
squares = [num ** 2 for num in range(12)]

# Bonus Tip 💡: You can also use dictionary, set, and generator comprehensions
squares_dict = {num: num ** 2 for num in range(12)} # dictionary
squares_set = {num ** 2 for num in range(12)}       # set
squares_gen = (num ** 2 for num in range(12))       # generator