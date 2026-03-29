import pandas as pd

# Load dataset
df = pd.read_csv('../datasets/sales_data.csv')

# Show dataset
print("Dataset:")
print(df)

# Total sales
total_sales = df['Sales'].sum()
print("\nTotal Sales:", total_sales)

# Average sales
avg_sales = df['Sales'].mean()
print("Average Sales:", avg_sales)

# High performers
high_sales = df[df['Sales'] > 150]

print("\nHigh Performers:")
print(high_sales)
