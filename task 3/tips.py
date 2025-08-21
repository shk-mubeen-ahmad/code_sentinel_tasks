import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("tips.csv")

print("Dataset loaded!")
print("Number of rows, columns:", df.shape)
print(df.head())

plt.figure(figsize=(6,4))
sns.barplot(x="day", y="tip", data=df, palette="Set2", estimator="mean")
plt.title("Average Tip by Day")
plt.ylabel("Average Tip ($)")
plt.show()

plt.figure(figsize=(6,4))
sns.histplot(df['total_bill'], bins=20, kde=True, color="skyblue")
plt.title("Distribution of Total Bills")
plt.xlabel("Total Bill ($)")
plt.show()

gender_counts = df['sex'].value_counts()
plt.figure(figsize=(5,5))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%',
        colors=["#66b3ff","#ff9999"])
plt.title("Proportion of Customers by Gender")
plt.show()

plt.figure(figsize=(6,4))
sns.boxplot(x="smoker", y="tip", data=df, palette="pastel")
plt.title("Tip Distribution by Smoking Status")
plt.show()
