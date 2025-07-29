import random

items = ["Pasta", "Meal of the Day", "Panini", "Muffin"]
prices = [45, 60, 40, 20]
inventories = [60, 100, 80, 40]

# simulating customer arrival with 50% purchase chance:
def simulate_customers(customers):
    """
    Simulates customers with a 50% chance of buying an item, 
    if they buy, gets random item name and adds to sales list
    """
    sales = []
    for i in range (customers):
        if random.random < 0.5:
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
    return prof_calc and cost_eod_inv

def profit_report_generator(sales):
    """
    Creates a report showing total costs of unsold inventory EOD
    and the total profit for the day (revenue - costs)
    """
    daily_report(sales)
    prof_calc, eod_costs = profit(sales)
    print(f"cost of unsold inventory: {eod_costs:.2f} DKK")
    print(f"Profit for the day: {prof_calc:.2f} DKK")



