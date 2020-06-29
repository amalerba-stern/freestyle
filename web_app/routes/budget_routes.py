# web_app/routes/budget_routes.py

from flask import Blueprint, render_template, request

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

    print("MY SPEND:", my_spend)
    return render_template("budget_input_received.html", item=item, 
                            category=category, price=price, month=month)

@budget_routes.route("/budget/table")
def budget_table():
    print("VISITED THE BUDGET FORM...")
    return render_template("budget_table.html", tables=[df.to_html(classes='data', header="true")])

@budget_routes.route("/budget/display", methods=["POST"])
def budget_display():
    print("GENERATING A BUDGET DISPLAY...")
    return render_template("budget_display.html")