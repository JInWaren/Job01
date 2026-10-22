"""
L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

maximum = L[0]

for nombre in L:
    if nombre > maximum:
        maximum = nombre

minimum = L[0]

for nombre in L:
    if nombre < minimum:
        minimum = nombre

print(f"la valeur max est : {maximum}")
print(f"la valeur min est : {minimum}")
"""



L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

maximum = L[0]

minimum = L[0]

for nombre in L:
    if nombre > maximum:
        maximum = nombre
    elif nombre < minimum:
        minimum = nombre


print(f"la valeur max est : {maximum}")
print(f"la valeur min est : {minimum}")


def max_min():
    L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

    maximum = L[0]

    minimum = L[0]

    for nombre in L:
        if nombre > maximum:
            maximum = nombre
        elif nombre < minimum:
            minimum = nombre


    print(f"la valeur max est : {maximum}")
    print(f"la valeur min est : {minimum}")

max_min()