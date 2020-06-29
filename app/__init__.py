# app/__init__.py

import os
from dotenv import load_dotenv

load_dotenv()

my_spend = [] # initialize list

APP_ENV = os.getenv("APP_ENV", default="development") # use "production" on a remote server
