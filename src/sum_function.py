# add numbers first n natural numbers ❌
result = 0
n = 10000000

# OK code but Slow 🐌
for i in range(1,n+1):
    result = result + i
print(result)

# using builtin sum function ✅ - faster⚡and smaller
print(sum(range(1,n+1)))

# sum() can also be used to calculate sum of list,tuples
print(sum([2,4,6,8,10,23,432]))
