import pandas as pd
from datetime import timedelta

filepath = "./customers-100000.csv"

customers = pd.read_csv(filepath)

customers.head()

# Subscription Date -> convert to datetime
customers["Subscription Date"] = pd.to_datetime(customers["Subscription Date"])

print(f'# Subscription Date')
print(f'📅 Newest subscription date: {customers["Subscription Date"].max()}')
print(f'📅 Latest subscription date: {customers["Subscription Date"].min()}')
print()

current_date = customers["Subscription Date"].max()
print(f'# Unique Customer')
print(f'📊 Total Unique Customer           : {customers["Customer Id"].nunique()}')
print(f'📊 Subscribed within last 6 months : {len(customers[customers["Subscription Date"] > (current_date - timedelta(days=182))])}')
print(f'📊 Subscribed within last 1 year   : {len(customers[customers["Subscription Date"] > (current_date - timedelta(days=365))])}')
print(f'📊 Subscribed within last 2 years  : {len(customers[customers["Subscription Date"] > (current_date - timedelta(days=720))])}')
print(f'📊 Subscribed within last 3 years  : {len(customers[customers["Subscription Date"] > (current_date - timedelta(days=365*3))])}')

print()
print(f'# Unique Countries')
print(f'📊 Found {len(customers["Country"].unique())} unique countries')
print(f'🔍 Countries sample: {list(customers["Country"].unique())[:10]}')
print(f'🔍 Top 5 Country: {list(customers["Country"].value_counts().keys())[:5]}')