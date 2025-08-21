import pandas as pd

df = pd.read_csv("sales.csv")

avg_revenue = df.groupby("Region")["Total Revenue"].mean()
profit_by_item = df.groupby("Item Type")["Total Profit"].sum()
orders_by_channel = df.groupby("Sales Channel")["Order ID"].count()

summary = df.groupby("Region").agg({
    "Units Sold": "sum",
    "Unit Cost": "mean",
    "Total Profit": "sum"
})

print("Average Revenue by Region:\n", avg_revenue, "\n")
print("Total Profit by Item Type:\n", profit_by_item, "\n")
print("Orders by Sales Channel:\n", orders_by_channel, "\n")
print("Summary by Region:\n", summary, "\n")
