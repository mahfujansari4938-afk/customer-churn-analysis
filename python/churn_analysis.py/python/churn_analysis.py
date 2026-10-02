import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/customer_churn.csv")

# Basic information
print("Total Customers:", df["CustomerID"].nunique())

# Churn analysis
churn_count = df["Churn"].value_counts()
print("\nChurn Count:")
print(churn_count)

# Churn percentage
churn_rate = (df["Churn"] == "Yes").mean() * 100
print("\nChurn Rate:", round(churn_rate, 2), "%")

# Average monthly charges
print(
    "\nAverage Monthly Charges:",
    round(df["MonthlyCharges"].mean(), 2)
)

# Average tenure
print(
    "Average Tenure:",
    round(df["Tenure"].mean(), 2),
    "months"
)

# Churn by contract
print("\nChurn by Contract:")
print(pd.crosstab(df["Contract"], df["Churn"]))

# Churn by payment method
print("\nChurn by Payment Method:")
print(pd.crosstab(df["PaymentMethod"], df["Churn"]))

# Churn visualization
df["Churn"].value_counts().plot(kind="bar")

plt.title("Customer Churn Distribution")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig("dashboard/churn_distribution.png")
plt.show()
