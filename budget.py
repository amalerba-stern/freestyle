# Budget
# Alex Malerba (afm433)

import os
import pandas

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    Param: my_price (int or float) like 4000.444444
    Example: to_usd(4000.444444)
    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

my_spend = [
    {"item":"banana", "category":"food", "price": 1.99, "date": "May 2020"}
]

# Input items
input_item = input("Input your item:")
input_category = input("Input the category:")
input_price = input("Input the price:")
input_date = input("Input the date:")

input_dict = dict({"item":input_item, "category":input_category, 
                   "price": int(input_price), "date":input_date})

my_spend.append(input_dict)

print(my_spend)