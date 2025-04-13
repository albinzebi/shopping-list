# Shopping list

print("You are shopping for some products. What are those products?")

shopping_list = []

# using while loop to create the shopping list
while True:

    item = input("Enter an item (or 'q' to quit): ")
    
    if item == 'q':
        break
    # using try - except statements to catch errors when not inserting a number when asking for the price
    try:
        price = int(input("Enter the price ($) of the item: "))
    except ValueError as e:
        print("error:", e)
        print("The price you entered is not a number. Retry inserting the item again.")
        continue

    shopping_list.append((item, price))

# using for loop to print each item, price and calculating the total price
total = 0

for item, price in shopping_list:
    print(f"{item} - ${price}")
    total += price

print(f"Total price: ${total}")