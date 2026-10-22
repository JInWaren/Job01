compteur = 0 

L = [8, 24, 48, 2, 16]

for nombre in L:
    if nombre % 3 == 0:
        compteur = compteur + 1
print(f"Dans la liste il y a {compteur} multiple de 3")



def compteur():
    compteur = 0 

    L = [8, 24, 48, 2, 16]

    for nombre in L:
        if nombre % 3 == 0:
            compteur = compteur + 1
    print(f"Dans la liste il y a {compteur} multiple de 3")

compteur()