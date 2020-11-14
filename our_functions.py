import pandas as pd
import numpy as np
import time
import missingno as msno 
import gc
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import re
import our_functions

# Function to calculate average price of products sold by brand
def avg_price_brand(data):
    # Provide the brand
#     brand ="auto"
    print("Type the desired category:")
    category = input()
    # Get the category
    data["category"] = data.category_code.str.extract(r'([^.]+)', expand = True)

    data = data[(data['event_type'] == 'purchase') & (data['category'] == category)]
    if data.shape[0]>0:
        # Group to get average price of products sold by the brand
        grouped = pd.DataFrame(data.groupby(['brand']).price.mean()).rename(columns={'price' : 'mean_price'}).reset_index().sort_values(by = ['mean_price'],ascending=False).head(20)
        # Plot average price of products sold by the category
        fig = px.bar(grouped, x="brand", y="mean_price", width=800, height=400,  title="Average price of products sold by " + category,labels={"mean_price": "Mean price of products"})
        fig.show()
    else:
        print("The brand does not exist...")
        
        
        
# Function to calculate profit by month fot a given brand
def profit_by_month_brand(data, brand):
    # Provide the brand
#     brand ="nexpero"
    data = data[data['brand'] == brand]
    if data.shape[0]>0:
        # Group to get number of purchases by year.month and brand
        grouped = pd.DataFrame(data.groupby([data.event_time.dt.to_period('M').astype(str),'brand']).price.sum()).rename(columns={'price' : 'my_sum'}).reset_index()
        
        return(grouped)
        
    else:
        print(brand)
        print("The brand does not exist...")
        grouped = pd.DataFrame()
        return(grouped)