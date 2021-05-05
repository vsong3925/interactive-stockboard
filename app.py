import json
from flask import Flask, render_template, jsonify
import pandas as pd
import os
import re
#%%
# Heroku
is_heroku = False
if 'IS_HEROKU' in os.environ:
    is_heroku = True
# Config variables
# Import your config file(s) and variable(s)
if is_heroku == True:
    # if IS_HEROKU is found in the environment variables, then use the rest
    # NOTE: you still need to set up the IS_HEROKU environment variable on Heroku (it is not there by default)
    api_key = os.environ.get('api_key')
else:
    # use the config.py file if IS_HEROKU is not detected
    from config import api_key
#%%
app = Flask(__name__)

#%%
@app.route("/")
def index():
    return render_template("index.html")

#%%
@app.route("/tickerlist")
def tickerlist(): 
    
    cwd = os.getcwd()
    
    tickerlist = pd.read_csv("static/data/tickerlist_industries.csv")
    tickerlist_json = tickerlist.to_json(orient='records')   #orient='columns'
    
    return tickerlist_json
#%%
if __name__ == "__main__":
    app.run(debug=True)
#%%
