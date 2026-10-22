N = int(input("Entrez un entier supérieure à zéro" ))

for table in range(1, N+1):
    print("table de", table,":")
    for i in range(0, 11):
        print(table, "x" , i , "=", (i * table))


def multiplication():
    N = int(input("Entrez un entier supérieure à zéro" ))

    for table in range(1, N+1):
        print("table de", table,":")
        for i in range(0, 11):
            print(table, "x" , i , "=", (i * table))

multiplication()
