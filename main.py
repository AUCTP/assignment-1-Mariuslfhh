import random

items = ["Pasta", "Meal of the Day", "Panini", "Muffin"]
prices = [45, 60, 40, 20]
inventories = [60, 100, 80, 40]
inv_backup = inventories.copy()

def simulate_customers(customers):
    """
    Simulates the stated amount of customers and give a 50% chance of purchase
    If customer makes a purchase, picks a random item from items to sell
    """
    sales = []
    for i in range (customers):
        if random.random() < 0.5:
            item_name = random.randint(0, (len(items)) - 1)
            if inventories[item_name] > 0:
                inventories[item_name] -= 1
                sales.append(item_name)
    return sales

def sales_list(sales):
    '''
    returns the total revenue by matching item with their 
    corresponding price and summing all amounts
    '''
    revenue = sum(prices[item_name] for item_name in sales)
    return revenue

def daily_report(sales):
    """
    Generates the daily report, showing total revenue for the day
    and leftover inventory at the end of the day
    """
    revenue = sales_list(sales)
    print (f"Total revenue for today: {revenue:.2f}DKK\n")
    print ("EOD Inventory:")
    for i in range(len(items)):
        print(f"{items[i]}: {inventories[i]}")

def profit(sales):
    """
    Calculates total cost of the leftover inventort EOD
    and returns the profit (revenue - costs)
    """
    revenue = sales_list(sales)
    cost_eod_inv = sum((inventories[i] * (prices[i] / 2)) for i in range (len(items)))
    prof_calc = revenue - cost_eod_inv
    return prof_calc, cost_eod_inv

def profit_report_generator(sales):
    """
    Creates a report showing total costs of unsold inventory EOD
    and the total profit for the day (revenue - costs)
    """
    daily_report(sales)
    prof_calc, eod_costs = profit(sales)
    print(f"cost of unsold inventory: {eod_costs:.2f} DKK")
    print(f"Profit for the day: {prof_calc:.2f} DKK")

sale_record = []

while True:
    print("\nChoose what you would like to do:")
    print("1: Choose amount of customers to simulate")
    print("2: Reset sales & inventory")
    print("3: Show leftover inventory")
    print("4: Show daily revenue report")
    print("5: Show daily report with profit")
    print("6: Terminate program")

    choice = int(input(""))

    if choice == 1:
        number = int(input("How many customers would you like to simulate?: "))
        salesN = simulate_customers(number)
        buyers = len(salesN)
        sale_record.extend(salesN)
        count = [0] * len(items)
        for i in salesN:
            count[i] += 1
        print(f"You simulated {number} customers")
        print(f"{buyers} customers made a purchase")
        print("They bought this amount of items:")
        for i in range(len(items)):
            print(f"{items[i]}: {count[i]}")
    
    elif choice == 2:
        inventories = inv_backup.copy()
        sale_record.clear()
        print("You have reset inventory and sale list")

    elif choice == 3:
        leftover_inv = inventories
        print("Leftover inventory: ")
        for i in range(len(inventories)):
            print(f"{items[i]}: {leftover_inv[i]}")

    elif choice == 4:
        if sale_record == 0:
            print("The sales list is empty")
        else:
            daily_report(sale_record)
    
    elif choice == 5:
        if sale_record == 0:
            print("There has been no sales yet")
        else:
            profit_report_generator(sale_record)

    elif choice == 6:
        print("Terminating program, see ya! 😎")
        break

    else:
        print("Please enter a valid number between 1 - 6")


    


