import pandas as pd
import random
from datetime import datetime, timedelta

# Function to generate random dates
def random_date(start, end):
    return start + timedelta(seconds=random.randint(0, int((end - start).total_seconds())))


# Function to generate data with rogue records
def generate_data_with_rogue_records(num_records=10000):
    electronics = [
        'Smartphone', 'Laptop', 'Tablet', 'Smartwatch', 'Bluetooth Speaker', 
        'Headphones', 'Gaming Console', 'Camera', 'Drone', 'External Hard Drive', 
        'USB Flash Drive', 'Smart TV', 'Wireless Router', 'Portable Charger', 
        'Projector', 'Fitness Tracker', 'VR Headset', 'Home Theater System', 
        'Monitor', 'Bluetooth Earbuds'
    ]
    
    stationery = [
        'Pens', 'Pencils', 'Eraser', 'Notebook', 'Stapler', 
        'Paper Clips', 'Markers', 'Highlighters', 'Ruler', 'Glue Stick', 
        'Scissors', 'Sticky Notes', 'Tape', 'Calculator', 'File Folder', 
        'Binder', 'Whiteboard Markers', 'Pencil Sharpener', 'Letter Opener', 'Paper Cutter'
    ]
    
    books = [
        'Fiction', 'Non-fiction', 'Biography', 'Science Fiction', 'Fantasy', 
        'Mystery', 'Historical Fiction', 'Self-Help', 'Cookbooks', 'Comics', 
        'Graphic Novels', 'Poetry', 'Travel Books', 'Thrillers', 'Horror', 
        'Children\'s Books', 'Young Adult', 'Classics', 'Textbooks', 'Memoir'
    ]
    
    clothing = [
        'T-Shirts', 'Jeans', 'Jackets', 'Sweaters', 'Hoodies', 
        'Dresses', 'Shorts', 'Skirts', 'Suits', 'Blouses', 
        'Coats', 'Pants', 'Socks', 'Underwear', 'Swimwear', 
        'Sportswear', 'Nightwear', 'Shoes', 'Scarves', 'Hats'
    ]
    
    home_kitchen = [
        'Cookware', 'Cutlery', 'Plates', 'Mugs', 'Glasses', 
        'Oven Mitts', 'Kitchen Towels', 'Spatulas', 'Mixing Bowls', 'Food Storage Containers', 
        'Blender', 'Microwave', 'Toaster', 'Coffee Maker', 'Dish Rack', 
        'Chopping Board', 'Measuring Cups', 'Kitchen Scale', 'Air Fryer', 'Pressure Cooker'
    ]

    product_categories = ['Electronics', 'Stationery', 'Books', 'Clothing', 'Home & Kitchen']
    payment_types = ['Card', 'Internet Banking', 'UPI', 'Wallet']
    countries = ['India', 'USA', 'UK', 'Germany', 'Australia']
    cities = {
        'India': ['Mumbai', 'Bengaluru', 'Indore'],
        'USA': ['Boston', 'New York', 'Chicago'],
        'UK': ['London', 'Oxford', 'Manchester'],
        'Germany': ['Berlin', 'Munich', 'Hamburg'],
        'Australia': ['Sydney', 'Melbourne', 'Brisbane']
    }
    websites = ['www.amazon.com', 'www.flipkart.com', 'www.ebay.in', 'www.tatacliq.com']

    # Date range for order dates
    start_date = datetime(2021, 1, 1)
    end_date = datetime(2023, 12, 31)

    records = []

    for i in range(num_records):
        order_id = i + 1
        customer_id = random.randint(100, 200)
        customer_name = random.choice(['John Smith', 'Mary Jane', 'Joe Smith', 'Neo', 'Trinity'])

        product_category = random.choice(product_categories)
        if product_category == 'Electronics':
            product_name = random.choice(electronics)
        elif product_category == 'Stationery':
            product_name = random.choice(stationery)
        elif product_category == 'Books':
            product_name = random.choice(books)
        elif product_category == 'Clothing':
            product_name = random.choice(clothing)
        elif product_category == 'Home & Kitchen':
            product_name = random.choice(home_kitchen)
        product_id = random.randint(200, 300)

        payment_type = random.choice(payment_types)
        qty = random.randint(1, 50)
        price = random.randint(5, 10000)
        order_datetime = random_date(start_date, end_date)

        country = random.choice(countries)
        city = random.choice(cities[country])
        website = random.choice(websites)

        payment_txn_id = random.randint(10000, 99999)
        payment_success = random.choice(['Y', 'N'])
        failure_reason = ''
        if payment_success == 'N':
            failure_reason = random.choice(['Invalid CVV', 'Insufficient Funds', 'Timeout'])

        # Rogue records
        if random.random() < 0.1:
            issue_type = random.choice([
                'missing_customer_name', 'invalid_payment_type', 'unrealistic_price',
                'negative_qty', 'missing_product_id', 'future_order_date'
            ])
            
            if issue_type == 'missing_customer_name':
                customer_name = ""  
            elif issue_type == 'invalid_payment_type':
                payment_type = "Invalid" 
            elif issue_type == 'unrealistic_price':
                price = random.randint(100000, 1000000)  
            elif issue_type == 'negative_qty':
                qty = random.randint(-50, -1)  
            elif issue_type == 'missing_product_id':
                product_id = None  
            elif issue_type == 'future_order_date':
                order_datetime = datetime(2023, 1, 1)  

        records.append([
            order_id, customer_id, customer_name, product_id, product_name, 
            product_category, payment_type, qty, price, order_datetime, 
            country, city, website, payment_txn_id, payment_success, failure_reason
        ])

    df = pd.DataFrame(records, columns=[
        'order_id', 'customer_id', 'customer_name', 'product_id', 'product_name', 
        'product_category', 'payment_type', 'qty', 'price', 'datetime', 
        'country', 'city', 'ecommerce_website_name', 'payment_txn_id', 
        'payment_txn_success', 'failure_reason'
    ])

    return df

# Generate the data with rogue records
df_with_rogue_records = generate_data_with_rogue_records(num_records=10000)

# Save the rogue records to a CSV file
df_with_rogue_records.to_csv('rogue.csv', index=False)