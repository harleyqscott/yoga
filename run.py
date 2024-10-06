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

#def update_attendance_worksheet(data):
  #  """
  #  Update attendance worksheet, add new row with the list data provided
  #  """
  #  print("Updating attendance worksheet...\n")
  #  attendance_worksheet = SHEET.worksheet("attendance")
  #  attendance_worksheet.append_row(data)
  #  print("Attendance worksheet updated successfully.\n")


#def update_placesLeft_worksheet(data):
  #  """
  #  Update placesLeft worksheet, add new row with the list data provided
  #  """
  #  print("Updating placesLeft worksheet...\n")
  #  placesLeft_worksheet = SHEET.worksheet("placesLeft")
  # placesLeft_worksheet.append_row(data)
  # print("placesLeft worksheet updated successfully.\n")

def update_worksheet(data, worksheet):
    """
    Recieves a list of user inserted integers to be inserted onto the worksheet.
    Then update particular worksheet
    """
    print(f"Updating {worksheet} worksheet\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated successfully\n")

def calculate_placesLeft_data(attendance_row):
    """
    Compare attendance with placesAvailable and calculate the placesLeft for each yoga type.
    The placesLeft is defined as the attendance figure subtracted from the placesAvaliable.
    """
    print("Calculating placesLeft data...\n")
    placesAvailable = SHEET.worksheet("placesAvailable").get_all_values()
    placesAvailable_row = placesAvailable[-1]
    
    placesLeft_data = []
    for placesAvailable, attendance in zip(placesAvailable_row, attendance_row):
        placesLeft = int(placesAvailable) - attendance
        placesLeft_data.append(placesLeft)
    
    return placesLeft_data

def get_last_5_entries_attendance():
    """
    collect the data (collums) of attendance worksheet, gathering the last 5 entries for each yoga session
    and return the data as a list of lists. 
    """
    attendance = SHEET.worksheet("attendance")
   

    columns = []
    for ind in range(1, 7):
        column = attendance.col_values(ind)
        columns.append(column[-5:])

    return columns
    
def calculate_placesAvailable_data(data):
    """
    calculate average places available for each yoga type
    """
    print("Calculating places available data...\n")
    new_placesAvailable_data = []

    for column in data:
        int_column = [int (num) for num in column]
        average = sum(int_column) / len(int_column)
        placesAvailable_num = average * 1.1
        new_placesAvailable_data.append(round(placesAvailable_num))
    
    return new_placesAvailable_data


def main():
    """
    Run all program functions
    """
    data = get_attendance_data()
    attendance_data = [int(num) for num in data]
    update_worksheet(attendance_data, "attendance" )
    new_placesLeft_data = calculate_placesLeft_data(attendance_data)
    update_worksheet(new_placesLeft_data, "placesLeft")
    attendance_columns = get_last_5_entries_attendance()
    placesAvailable_data = calculate_placesAvailable_data(attendance_columns)
    update_worksheet(placesAvailable_data, "placesAvailable")


print("Welcome to Yoga Data Automation")
main()

