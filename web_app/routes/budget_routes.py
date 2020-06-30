# web_app/routes/budget_routes.py

from flask import Blueprint, render_template, request
import plotly
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import json
import numpy as np

budget_routes = Blueprint("budget_routes", __name__)

@budget_routes.route("/budget/form")
def budget_form():
    print("VISITED THE BUDGET FORM...")
    return render_template("budget_form.html")

@budget_routes.route("/budget/input-received", methods=["POST"])
def budget_input_received(my_spend=[]):
    print("RECEIVED YOUR BUDGET FORM INPUTS...")
    if request.method == 'POST':
        print("FORM DATA:", dict(request.form))
        item = request.form['item']
        category = request.form['category']
        price = request.form['price']
        month = request.form['month']

        input_dict = dict({"item":item, "category":category, 
                   "price": price, "month":month})
        try:
            my_spend.append(input_dict)
        except:
            my_spend = []
            my_spend.append(input_dict)

    #plotly.offline.plot({"data": line, "layout": layout}, 
    #                     filename = "monthly_sales_over_time.html",
    #                     auto_open=True) %}


    print("MY SPEND:", my_spend)
    #return render_template("budget_input_received.html", item=item, 
    #                        category=category, price=price, month=month)

@budget_routes.route("/budget/table")
def budget_table():
    print("VISITED THE BUDGET FORM...")
    return render_template("budget_table.html", tables=[df.to_html(classes='data', header="true")])

@budget_routes.route("/budget/display")#, methods=["POST"])
def budget_display():
    print("GENERATING A BUDGET DISPLAY...")

    y = [99, 101, 98, 98, 96, 94, 102, 99, 100, 101, 102, 96]
    x = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Oct", "Nov", "Dec"]

    # line = go.Scatter(x = x, y = y)
    data = [dict(x=x, y=y, type='scatter')]

    layout = go.Layout(title = f"Spending by Month",
                       xaxis = dict({"title" : "Month"}),
                       yaxis = dict({"title" : "Sales (USD)", 
                       "tickformat":"$.2f"}))

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template("index.html", plot=graphJSON)

def create_plot():
    y = [99, 101, 98, 98, 96, 94, 102, 99, 100, 101, 102, 96]
    x = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Oct", "Nov", "Dec"]
    data = go.Bar(x=x, y=y)

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

@budget_routes.route('/graph')
def line():
    count = 500
    xScale = np.linspace(0, 100, count)
    yScale = np.random.randn(count)
 
    # Create a trace
    trace = go.Scatter(
        x = xScale,
        y = yScale
    )
 
    data = [trace]
    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('index.html',
                               graphJSON=graphJSON)