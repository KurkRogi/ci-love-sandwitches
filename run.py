import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("love_sandwiches")

# sales = SHEET.worksheet('sales')
# data = sales.get_all_values()
# print(data)

def get_sales_data():
    """
    Get sales data from the user
    """
    while True:
        print("Please provade sales data")
        print("6 numbers separated by comas")
        print("e.g.: 12,38,45,12,4,21\n")

        data_str = input("Please enter your numbers and press Enter: ")

        sales_data = data_str.split(",")
        if validate_data(sales_data):
            print("\n*** Data is valid")
            break
    
    return sales_data

def validate_data(values):
    """
    Validates user input data and coverts strings to integers
    in try statemend plus checks if there is 6 datum
    """
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError (
                f"Exactly 6 values are required. You supplied {len(values)}"
            )
    except ValueError as e:
        print(f"Error occured: {e}. Please try again")
        return False
    
    return True

def update_sales_worksheet(data):
    """
    update goodle worksheet inserting new row from data prowided
    as a list
    """

    print(f"*** Updating sales worksheet with data: {data}")

    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(data)

    print("*** Sales worksheet updated.\n")

def calculate_surplus_data(sales_row):
    """
    Compare sales data with stock data and calculate surplus for each item
    """ 
    
    print("*** Calculating suplus data...")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1]
    
    surplus_data = []
    for stock, sales in zip(stock_row, sales_row):
        surplus = int(stock) - sales
        surplus_data.append(surplus)
    
    return surplus_data

def main():
    """
    Run program functions
    """
    data = get_sales_data()
    sales_data = [int(datum) for datum in data]
    update_sales_worksheet(sales_data)
    new_surplus_data = calculate_surplus_data(sales_data)
    print(new_surplus_data)

print("\n"+"-"*42)
print("Welcome to Love Sandwiches Data Automation")
print("-"*42)

main()