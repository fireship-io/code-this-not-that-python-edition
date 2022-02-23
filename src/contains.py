# Check if a value is contained in a list
L = ["JavaScript", "Python", "Ruby", "PHP", "Rust"]
x = "Rust"

# OK version 🤔 - For loop and a equality check ❌
for i in range(len(L)):
    if x == L[i]:
        print(f"{x} is contained in the list")

# Pythonic version 🐍: Use "if x in L" ✅
if x in L:
    print(f"{x} is contained in the list")