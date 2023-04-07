# Null check: OK version 🤔 - Explicit "if x is not None" ❌
n = 42
if n is not None:
    print(f"n exists and is equal to {n}")

# Pythonic version 🐍: Use simplified if ✅
if n:
    print(f"n exists and is equal to {n}")
