import gspread
from google.oauth2.service_account import Credentials

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
    print("\n"+"-"*10)
    print("Please provade sales data")
    print("6 numbers separated by comas")
    print("e.g.: 12,38,45,12,4,21\n")

    data_str = input("Please enter your numbers and press Enter: ")
    print("\n")

    sales_data = data_str.split(",")
    validate_data(sales_data)

def validate_data(values):
    """
    Validates user input data and coverts strings to integers
    in try statemend plus checks if there is 6 datum
    """
    try:
        if len(values) != 6:
            raise ValueError (
                f"Exactly 6 values are required. You supplied {len(values)}"
            )
    except ValueError as e:
        print(f"Error occured: {e}\n")


get_sales_data()