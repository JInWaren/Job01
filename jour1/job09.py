name = "wassim"
price_unity = 15
quantity_in_stock = 5

print(name, price_unity, quantity_in_stock)

quantity_in_stock = input("saisir la quantité de produits que vous souhaitez ")
print("la quantité de produit de", quantity_in_stock) 

percentage_increase = 10

price_unity_after_infaltion = price_unity * (1 + percentage_increase  / 100)
print("la nouvelle valeur est", price_unity_after_infaltion,"€")



def produit():
    name = "wassim"
    price_unity = 15
    quantity_in_stock = 5

    print(name, price_unity, quantity_in_stock)

    quantity_in_stock = int(input("saisir la quantité de produits que vous souhaitez "))
    print("la quantité de produit de", quantity_in_stock) 

    percentage_increase = 10

    price_unity_after_infaltion = price_unity * (1 + percentage_increase  / 100)
    print("la nouvelle valeur est", price_unity_after_infaltion,"€")


produit()