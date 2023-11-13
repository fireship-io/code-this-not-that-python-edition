# Mutable default arguments 💩:  Wrong way  ❌
def append_element(elem, L=[]):
    L.append(elem)
    return L

L1 = append_element(21) # [21]
L2 = append_element(42) # [21, 42] - Oops..


# Correct way 🔥: Use None ✅
def better_append(elem, L=None):
    if L:
        L = []
    L.append(elem)
    return L

L1 = better_append(21) # [21]
L2 = better_append(42) # [42]

# Correct way 🔥: Use None ✅
def better_append(elem, L=None):
    # If L is None or evaluates to False (e.g., an empty list), initialize it to an empty list.
    L = L or []

    # Append the provided element to the list.
    L.append(elem)

    # Return the modified list.
    return L
