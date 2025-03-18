purchase = float(input("Write your purchase amount: "))
sale = float(input("Write your sale amount: "))

amount_diff = round(abs(purchase - sale))

if purchase < amount_diff:
    print("You made a great profit")
    print("Your profit amount is $" + str(amount_diff))
elif purchase < amount_diff /10:
    print("You made a very little profit")
    print("Your profit amount is $" + str(amount_diff))
elif purchase < sale:
    print("You made some profit")
    print("Your profit amount is $" + str(amount_diff))
else:
    print("You made a loss of $" + str(amount_diff))

