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

    print(f"Data provided: {data_str}\n")

get_sales_data()