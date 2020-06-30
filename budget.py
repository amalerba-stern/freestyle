# Budget
# Alex Malerba (afm433)

import os
import pandas
import plotly
import plotly.graph_objs as go

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    Param: my_price (int or float) like 4000.444444
    Example: to_usd(4000.444444)
    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

# sample input data (want user to input this)
my_spend = [
    {"item":"banana", "category":"food", "price": 1.99, "month": 1},
    {"item":"rent", "category":"housing", "price": 1200, "month": 1},
    {"item":"rent", "category":"housing", "price": 1200, "month": 2},
    {"item":"rent", "category":"housing", "price": 1200, "month": 3},
    {"item":"rent", "category":"housing", "price": 1200, "month": 4},
    {"item":"rent", "category":"housing", "price": 1250, "month": 5},
    {"item":"rent", "category":"housing", "price": 1250, "month": 6},
    {"item":"rent", "category":"housing", "price": 1250, "month": 7},
    {"item":"rent", "category":"housing", "price": 1250, "month": 8},
    {"item":"rent", "category":"housing", "price": 1250, "month": 9},
    {"item":"rent", "category":"housing", "price": 1250, "month": 10},
    {"item":"rent", "category":"housing", "price": 1250, "month": 11},
    {"item":"rent", "category":"housing", "price": 1250, "month": 12},
    {"item":"dinner", "category":"food", "price": 40, "month": 5},
    {"item":"metrocard", "category":"transportation", "price": 150, "month": 5},
    {"item":"gift", "category":"other", "price": 150, "month": 5},
    {"item":"gym", "category":"personal", "price": 50, "month": 5}
]
'''
# Input items
input_item = input("Input your item:")
input_category = input("Input the category:")
input_price = input("Input the price:")
input_date = input("Input the date:")

input_dict = dict({"item":input_item, "category":input_category, 
                   "price": int(input_price), "date":input_date})

my_spend.append(input_dict)
'''
# Create pandas DataFrame from the input data
# https://www.geeksforgeeks.org/different-ways-to-create-pandas-dataframe/
items = [purchase["item"] for purchase in my_spend]
categories = [purchase["category"] for purchase in my_spend]
prices = [purchase["price"] for purchase in my_spend]
months = [purchase["month"] for purchase in my_spend]

data = pandas.DataFrame({"Item": items, "Category": categories,
                         "Price": prices, "Month": months})

# Generate summary statistics

data_by_category = data.groupby("Category").sum().sort_values(by=["Price"], ascending=False)
total = sum(data_by_category["Price"])

data_by_date = data.groupby("Month").sum().sort_values(by=["Month"], ascending=True)

# Generate summary graphs & plots

y = list(data_by_date["Price"])
x = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Oct", "Nov", "Dec"]

line = go.Scatter(x = x, y = y)

layout = go.Layout(title = f"Spending by Month",
                   xaxis = dict({"title" : "Month"}),
                   yaxis = dict({"title" : "Sales (USD)", 
                                 "tickformat":"$.2f"}))

plotly.offline.plot({"data": line, 
                     "layout": layout},
                    filename = "monthly_sales_over_time.html",
                    auto_open = True)

# Pie chart showing spend by category

# Use exceptions in case there are no items in that category
try:
    spend_housing = data_by_category["Price"].loc["housing"]/total
except:
    spend_housing = 0

try:
    spend_food = data_by_category["Price"].loc["food"]/total
except:
    spend_food = 0

try:
    spend_personal = data_by_category["Price"].loc["personal"]/total
except:
    spend_personal = 0

try:
    spend_transportation = data_by_category["Price"].loc["transportation"]/total
except:
    spend_transportation = 0

try:
    spend_other = data_by_category["Price"].loc["other"]/total
except:
    spend_other = 0

pie_data = [
    {"category": "Housing", "spend_pct": spend_housing},
    {"category": "Food", "spend_pct": spend_food},
    {"category": "Personal", "spend_pct": spend_personal},
    {"category": "Transportation", "spend_pct": spend_transportation},
    {"category": "Other", "spend_pct": spend_other}
]

print("----------------")
print("GENERATING PIE CHART...")
print(pie_data) # TODO: create a pie chart based on the pie_data

labels = [pie_data["category"] for pie_data in pie_data]
values = [pie_data["spend_pct"] for pie_data in pie_data]

trace = go.Pie(labels=labels, values=values)
plotly.offline.plot([trace], filename="pie_chart.html", auto_open=True)