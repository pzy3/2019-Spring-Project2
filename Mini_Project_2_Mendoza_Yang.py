# 100 small chocolate chip cookies = 1 cup of sugar + 16 tbs of butter + 1 cup of brown sugar
# + 2 eggs + 1 tsp vanilla + 2.5 cups of Oats + 2 cups of flour + 1 tsp of baking powder
# + 1 tsp of baking soda + 0.5 tsp of salt + 2 cups of chocolate chips 
def main():
    # Ask user what is needed to make 100 cookies
    print("What do you need to make a batch of 100 chocolate chip cookies?\n>")

    # List the ingredients and approximate prices
    print("1 cup of sugar, approximately $0.17")
    print("16 tbs of butter, approximately $1.28")
    print("1 cup of brown sugar, approximately $0.15")
    print("2 eggs, approximately $0.14")
    print("1 tsp vanilla , approximately $0.13")
    print("2.5 cups of Oats, approximately $0.50")
    print("2 cups of flour, approximately $0.24")
    print("1 tsp of baking powder, approximately $0.03")
    print("1 tsp of baking sodar, approximately $0.01")
    print("0.5 tsp of salt, approximately $0.01")
    print("2 cups of chocolate chips, approximately $2.19")

    # Ask user the number of cookies
    # Store anser(cookies)
    cookies = float(input("How many chocolate chip cookies do you want to make?\n>"))

    #ask price for each item
    sugar = float(input("Enter the price of sugar: "))
    butter = float(input("Enter the price of butter: "))
    bsugar = float(input("Enter the price of brown sugar: "))
    eggs = float(input("Enter the price of eggs: "))
    vanilla = float(input("Enter the price of vanilla: "))
    oats = float(input("Enter the price of oats: "))
    flour = float(input("Enter the price of flour: "))
    bpowder = float(input("Enter the price of baking powder: "))
    bsoda = float(input("Enter the price of baking soda: "))
    salt = float(input("Enter the price of salt: "))
    choco_chips = float(input("Enter the price of chocolate chips: "))

    # Calculate the subtotal of 11 items
    subTotal = (sugar + butter + bsugar + eggs + vanilla + oats + flour + bpowder + bsoda + salt + choco_chips)

    # Calculate the tax
    salesTax = (subTotal*0.0725)

    # Calculate total
    total = (subTotal + salesTax)

    #display subTotal, salesTax, total
    print("\nSub Total: $" + format(subTotal, ",.2f"), "Tax amount: $" + \
          format(salesTax, ",.2f"), "Total: $" + format(total, ",.2f"), \
          sep = "\n")

    #if statment of self made cookies vs store bought
    total = 5.20
    scookies = 4.58
    if total > scookies:
        print("total of self made cookies is greater than store cookies.")
    else:
        print("It's cheaper to get store bought cookies.")

    #Instructions for making cookies
    print("Instructions for making cookies: ")
    print("1. Pre-heat oven to 350 degree.")
    print("2. Mix the butter with both the sugar.")
    print("3. Add eggs and vanilla and mix until combined.")
    print("4. Depending on the kind of oats you have and how big you want them,")
    print("you can use as-is or chop them in a food processor until they're fine powder.")
    print("5. All all the dry ingredients to the wet mixture and mix until combined.")
    print("6. Add the chocolate chip.")
    print("7. Form dough into one-inch balls and place on a cookie sheet.")
    print("8. Flatten the cookies with the palm of your hand.")
    print("9. Bake for 13-17 minutes (usually 15 minutes) or until lightly golden brown.")
    print("10. Remove from oven and let it cool down.")
    print("Enjoy!")


# Run program
main()
