
dict1 = {'Laptop':65000 , 'Phone': 25000 , 'Mouse' : 800 , 'Keybord' :1200 , 'Monitor': 9000 , 'Speaker': 2500 }
no_of_products = int(input("Enter the no of the Different type of products : "))
subtotal = 0
for i in range(no_of_products):
    name_of_product = input(f"Enter the name products- {i+1}: ").title()
    quantity = int(input(f"Enter the no of {name_of_product}'s needed : "))

    while name_of_product not in dict1 or quantity <= 0:
        if name_of_product not in dict1: 
            name_of_product = input(f"Enter the name product{i+1} which are available ").title()
        if quantity<=0:
             quantity = int(input(f"Enter the no of positive {name_of_product}'s needed : "))


    price_product =quantity*dict1[name_of_product]

    subtotal += price_product

    if i ==0 :
        print("----invoice----")
        print("--"*23)
        print(f"{'product name':<15}| {'Quantity':<8} | {'price'}")
        print("--"*23)

    print(f'{name_of_product:<15} | {quantity:8  } | {price_product}')


print(f"\nsubtotal :{subtotal}")

if subtotal >60000:
    discount = subtotal*15/100
elif subtotal >30000:
    discount = subtotal*10/100
elif subtotal >10000:
    discount = subtotal*5/100

print(f"Discount : {discount}")

final_bill_amount = subtotal - discount

print (f"The bill amount : {final_bill_amount}")
