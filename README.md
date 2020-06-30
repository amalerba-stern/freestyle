# Freestyle project

## Environment Setup

Create and activate a new Anaconda virtual environment:

```sh
conda create -n budget-env python=3.7 # (first time only)
conda activate budget-env
```

From within the virual environment, run the requirements.txt file which will install any required packages:

```sh
pip install -r requirements.txt
```
From within the virtual environment, run the Python script from the command-line:

```sh
python budget.py
```

## Program Overview

There are two ways to run the program which the user will be prompted to select upon running the Python script:

> CSV: Import an existing CSV file. This file must be saved in the directory as budget.csv and must have columns titled "item", "category", "price", and "month". 

> MANUAL: Manually enter each time you spent money, including the item, category, price, and month. 

For both formats, items and categories should be in text format; prices and months should be in number format (with price > $0 and month between 1 and 12, inclusive).

When done, the program will output two graphs/charts:

> SPENDING OVER TIME: This is a line graph showing spend over the 12 month time period.

> SPENDING BY CATAEGORY: This is a pie chart showing spend by four pre-defined categories (food, housing, personal, and transportation) and one catch-all category (other).