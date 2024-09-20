#clean the data
import pandas as pd

# Load the DataFrame if not already loaded
df_with_rogue_records = pd.read_csv('rogue_records.csv')

# Define cleaning functions
def clean_missing_customer_name(df):
    # Option 1: Drop records with missing customer names
    #fill missing values
    df = df.assign(customer_name=df['customer_name'].fillna('Unknown Customer'))
    df = df.assign(failure_reason=df['failure_reason'].fillna('None'))
    return df

def clean_invalid_payment_type(df):
    valid_payment_types = ['Card', 'Internet Banking', 'UPI', 'Wallet']
    df = df[df['payment_type'].isin(valid_payment_types)]
    return df

def clean_unrealistic_price(df):
    max_price = 10000  # Define a reasonable upper limit for price
    df.loc[df['price'] > max_price, 'price'] = max_price
    return df
    
def clean_negative_qty(df):
    df.loc[df['qty'] < 0, 'qty'] = 1  # Replace negative quantities with 1 or a valid default
    return df
# Convert 'datetime' to pandas datetime format

# Apply cleaning functions
df_cleaned = df_with_rogue_records.copy()
df_cleaned = clean_missing_customer_name(df_cleaned)
df_cleaned = clean_invalid_payment_type(df_cleaned)
df_cleaned = clean_unrealistic_price(df_cleaned)
df_cleaned = clean_negative_qty(df_cleaned)
df_cleaned['datetime'] = pd.to_datetime(df_cleaned['datetime'], errors='coerce')

# Save the cleaned DataFrame
df_cleaned.to_csv('cleaned.csv', index=False)

print("Data cleaning completed. Cleaned data saved to 'cleaned.csv'.")