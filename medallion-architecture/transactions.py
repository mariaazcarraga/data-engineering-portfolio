import pandas as pd
import numpy as np

np.random.seed(42)

n = 1000

transaction_ids = np.arange(1, n + 1)
customer_ids = np.random.randint(1000, 1100, size=n)
amounts = np.round(np.random.uniform(5, 500, size=n), 2)
currencies = np.random.choice(["CAD", "USD", "EUR", "GBP", "MXN"], size=n)
countries = np.random.choice(["Canada", "USA", "Spain", "UK", "Mexico"], size=n)
channels = np.random.choice(["Online", "In-Store", "Mobile"], size=n)
merchant_categories = np.random.choice(
    ["Grocery", "Electronics", "Restaurant", "Travel", "Fashion", "Pharmacy"],
    size=n
)
statuses = np.random.choice(["Completed", "Declined", "Refunded", "Pending"], size=n)

dates = pd.date_range("2024-01-01", periods=60)
transaction_dates = np.random.choice(dates, size=n)

df = pd.DataFrame({
    "transaction_id": transaction_ids,
    "customer_id": customer_ids,
    "amount": amounts,
    "currency": currencies,
    "transaction_date": transaction_dates,
    "country": countries,
    "channel": channels,
    "merchant_category": merchant_categories,
    "status": statuses
})

df.to_csv("transactions.csv", index=False)