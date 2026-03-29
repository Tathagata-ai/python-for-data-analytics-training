import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('../datasets/sales_data.csv')

# Sort data
df = df.sort_values(by='Sales', ascending=False)

# Top performer
top = df.iloc[0]
print("Top Performer:")
print(top)

# Plot
plt.bar(df['Name'], df['Sales'])
plt.title("Sales Performance")
plt.xlabel("Name")
plt.ylabel("Sales")

plt.show()
