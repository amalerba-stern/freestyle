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

# Create or input pandas DataFrame from the input data
# https://www.geeksforgeeks.org/different-ways-to-create-pandas-dataframe/
while True:
    input_method = input("What is your input method? ('csv' or 'manual'):")
    print("1")
    if input_method == "csv":
        data = pandas.read_csv("budget.csv", engine='python')
        data["price"] = [int(p) for p in data["price"]]
        break
    elif input_method == "manual":
        my_spend = []
        done = "No"
        while done == "No":
            input_item = input("Input your item:")
            input_category = input("Input the category:")
            input_price = input("Input the price:")
            input_month = input("Input the month (as a number):")
            input_done = input("Are you done entering your spending? ('Yes' or 'No'):")
            input_dict = dict({"item":input_item, "category":input_category, 
                            "price": int(input_price), "month":input_month})
            my_spend.append(input_dict)
            if input_done == "Yes":
                done = "Yes"
                break
        items = [purchase["item"] for purchase in my_spend]
        categories = [purchase["category"] for purchase in my_spend]
        prices = [int(purchase["price"]) for purchase in my_spend]
        months = [purchase["month"] for purchase in my_spend]

        data = pandas.DataFrame({"item": items, "category": categories,
                                "price": prices, "month": months})
    else:
        print("Invalid entry. You must select either 'csv' or 'manual.")

# Generate summary statistics

data_by_category = data.groupby("category").sum().sort_values(by=["price"], ascending=False)
total = sum(data_by_category["price"])

data_by_date = data.groupby("month").sum().sort_values(by=["month"], ascending=True)

# Generate summary graphs & plots

y = list(data_by_date["price"])
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
    spend_housing = data_by_category["price"].loc["housing"]/total
except:
    spend_housing = 0

try:
    spend_food = data_by_category["price"].loc["food"]/total
except:
    spend_food = 0

try:
    spend_personal = data_by_category["price"].loc["personal"]/total
except:
    spend_personal = 0

try:
    spend_transportation = data_by_category["price"].loc["transportation"]/total
except:
    spend_transportation = 0

try:
    spend_other = data_by_category["price"].loc["other"]/total
except:
    spend_other = 0

pie_data = [
    {"category": "housing", "spend_pct": spend_housing},
    {"category": "food", "spend_pct": spend_food},
    {"category": "personal", "spend_pct": spend_personal},
    {"category": "transportation", "spend_pct": spend_transportation},
    {"category": "other", "spend_pct": spend_other}
]

print("----------------")
print("GENERATING PIE CHART...")
print(pie_data) # TODO: create a pie chart based on the pie_data

labels = [pie_data["category"] for pie_data in pie_data]
values = [pie_data["spend_pct"] for pie_data in pie_data]

trace = go.Pie(labels=labels, values=values)
plotly.offline.plot([trace], filename="pie_chart.html", auto_open=True)