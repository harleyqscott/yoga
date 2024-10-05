import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]


CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('yoga')

def get_attendance_data():
    """
    Get attendance numbers from the users
    """
    while True:
        print("Please enter attendance data from the last market.")
        print("Data should be six numbers, seperated by commas.")
        print("Example: 1, 2, 3, 4, 5, 6\n")

        data_str = input("Enter your data here: ")
    
        attendance_data = data_str.split(",")
        
        if validate_data(attendance_data):
            print("Data is valid!")
            break

    return attendance_data

def validate_data(values):
    """
    converts all string values into integers.
    Raises valueerror if strings cannot be converted into integers,
    or if they are not precisely 6 numbers.
    """
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Precisely 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Data is invalid: {e}, please try again.\n")
        return False

    return True

def update_attendance_worksheet(data):
    """
    update attendance worksheet, add new row with data the user inputted
    """
    print("Updating attendance worksheet\n")
    attendance_worksheet = SHEET.worksheet("attendance")
    attendance_worksheet.append_row(data)
    print("Attendance worksheet updated successfully.\n")


def calculate_placesLeft_data(attendance_row):
    """
    Compare attendance with placesAvailable and calculate the placesLeft for each yoga type.
    The placesLeft is defined as the attendance figure subtracted from the placesAvaliable.
    """
    print("Calculating placesLeft data...\n")
    placesAvailable = SHEET.worksheet("placesAvailable").get_all_values()
    placesAvailable_row = placesAvailable[-1]
    print(f"placesAvailable row: {placesAvailable_row}")
    print(f"attendance row: {attendance_row}")

def main():
    """
    Run all program functions
    """
    data = get_attendance_data()
    attendance_data = [int(num) for num in data]
    update_attendance_worksheet(attendance_data)
    calculate_placesLeft_data(attendance_data)


print("Welcome to Yoga Data Automation")
main()