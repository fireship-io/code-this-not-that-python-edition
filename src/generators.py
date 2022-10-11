from sys import getsizeof 

# Inefficent way 💩: Using a list ❌
L = [n for n in range(42_000)]
sum(L) # 881979000
getsizeof(L) # 351064 bytes

# Efficient way 🔥: Use a generator ✅
G = (n for n in range(42_000))
sum(G) # 881979000
getsizeof(G) # 112 bytes
