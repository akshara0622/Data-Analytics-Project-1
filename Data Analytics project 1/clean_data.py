import pandas as pd


df = pd.read_excel("Dataset for Data Analytics.xlsx", engine="openpyxl")


print("Missing Values:")
print(df.isnull().sum())


df = df.drop_duplicates()


df["CouponCode"] = df["CouponCode"].fillna("No Coupon")


df.to_excel("Cleaned_Dataset.xlsx", index=False)

print("Cleaning completed successfully!")
print("\nDuplicate Rows:", df.duplicated().sum())
print("Missing Values After Cleaning:")
print(df.isnull().sum())