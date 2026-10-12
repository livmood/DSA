
'''
A dictionary ticket_sales is used to map ticket type to number of tickets sold. Return the total number of tickets of all types sold.

def total_sales(ticket_sales):
    pass
Example Usage:

ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

print(total_sales(ticket_sales))
Example Output:

4500

Input: dictionary of ticket sales (key: date, value: number of sales)
Output: sum of all ticket sales

Edge Cases:
1. if dictionary is empty
2. negative ticket sales
3. if number of tickets is too big

Plan
1. for loop ticket_type, ticket_sold in ticket_sales dict
2. for each iteration increment the total by the ti cket_sales 
3. return total
'''
def total_sales(ticket_sales):
    sum = 0

    for ticket_type in ticket_sales:
        sum += ticket_sales.get(ticket_type)
    
    return sum

ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

print(total_sales(ticket_sales))
