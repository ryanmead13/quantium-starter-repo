import pandas as pd
sales_df_0 = pd.read_csv("data/daily_sales_data_0.csv")
sales_df_1 = pd.read_csv("data/daily_sales_data_1.csv")
sales_df_2 = pd.read_csv("data/daily_sales_data_2.csv")

dataFrames = [sales_df_0, sales_df_1, sales_df_2]


for i in range(len(dataFrames)):
    df = dataFrames[i]

    # Filter product field
    df = df.loc[df['product'] == 'pink morsel'].copy()

   # Update price column to be numeric
    df['price'] = df['price'].str.replace("$", "").astype(float)

   # Create new column sales, then remove quantity, product and price columns
    df['sales'] = df['price'] * df['quantity']
    df = df.drop(['price', 'quantity', 'product'], axis=1)

    dataFrames[i] = df

# Combine dfs and write to new csv
combined_df = pd.concat(dataFrames)
combined_df.to_csv("data/combined_pink_morsel_sales_data.csv", index=False)

print("Combined sales data saved to data/combined_pink_morsel_sales_data.csv")