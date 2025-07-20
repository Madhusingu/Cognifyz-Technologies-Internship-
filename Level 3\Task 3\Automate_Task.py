import pandas as pd

# Load data
df = pd.read_csv(r"C:\Users\madhu\OneDrive\Desktop\Cognifyz intern\Level 3\Task 3\leveltsk3.csv")

# Optional: Clean column names
df.columns = df.columns.str.strip().str.title()

# Clean data
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

# Convert 'Sales' to numeric if needed
df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')
df.dropna(subset=['Sales'], inplace=True)

# Calculate overall stats
total_sales = df['Sales'].sum()
average_sales = df['Sales'].mean()

# Grouped summaries
sales_by_region = df.groupby('Region')['Sales'].sum()
sales_by_product = df.groupby('Product')['Sales'].sum()

# Print to console
print("===== Sales Summary Report =====")
print(f"Total Sales: ${total_sales:.2f}")
print(f"Average Sales: ${average_sales:.2f}")
print("\nSales by Region:")
print(sales_by_region)
print("\nSales by Product:")
print(sales_by_product)

# Save summary to CSV
summary = {
    'Total Sales': [total_sales],
    'Average Sales': [average_sales]
}
summary_df = pd.DataFrame(summary)
summary_df.to_csv("sales_summary_report.csv", index=False)

# Save grouped data to separate CSV reports
sales_by_region.to_csv("sales_by_region.csv")
sales_by_product.to_csv("sales_by_product.csv")

print("\n✅ Reports generated successfully!")
