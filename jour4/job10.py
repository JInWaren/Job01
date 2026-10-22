def pair_impair(chiffre):
    if chiffre > 0 and chiffre == int(chiffre):
        if chiffre % 2 == 0:
            print("ce chiffre est pair")
        else:
            print("ce chiffre est impair")

pair_impair(7)
pair_impair(3)
pair_impair(2.5)
pair_impair(-4)