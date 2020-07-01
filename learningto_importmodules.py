def make_pizza(size, *toppings):
    print("Making a pizza with " + str(size) + " inch and having following topppings : ")
    for topping in toppings:
        print(" - " + topping)