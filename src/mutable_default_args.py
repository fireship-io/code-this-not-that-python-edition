# Mutable default arguments 💩:  Wrong way  ❌
def append_element(elem, L=[]):
    L.append(elem)
    return L

L1 = append_element(21) # [21]
L2 = append_element(42) # [21, 42] - Oops..


# Correct way 🔥: Use None ✅
def better_append(elem, L=None):
    if L is None:
        L = []
    L.append(elem)
    return L

L1 = better_append(21) # [21]
L2 = better_append(42) # [42]