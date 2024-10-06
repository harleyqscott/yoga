# Yoga

## Introduction
I built this program to collect input from user and use that data to calculate the average places I should have in the next market of yoga sessions. To do this, i first had to request the attendance data from the user, then calculate the placesleft data finally calculate the placesAvailable data bases on the averages from the last 5 market enries.

### Google sheets
The sheets are separated into three separate worksheets, attendance, placesAvailable and placesLeft.<br>
<img src="https://github.com/user-attachments/assets/316b38c9-4a6c-415d-ae09-900af7b004a7" width="400" height="500">
<br>Attendance worksheet image<br>

<img src="https://github.com/user-attachments/assets/471e9f73-8fb6-4490-8c99-d6c288c925a8" width="400" height="500">
<br>placesAvailable worksheet image<br>

<img src="https://github.com/user-attachments/assets/dcabfd5c-c6cb-46fc-9631-c3e5e66ded30" width="400" height="500">
<br>placesLeft worksheet image<br>


### How each part works
loops- While loops for example are used to execute a block of code repeatedly as long as a given condition is met. If the condiditon is not met, the block of code will keep repeating. I used this to loop through my code so that when a user inputs their data if it isn't valid then it will ask them to repeat and try again.  <br>

break- Break is used to end a loop once its requirments are met.<br>

return- Return can be used to return whether the statement is true or false for example is the requirements are met return true. Also if an error is thrown in the statement then you can use return to return false. Return can also be used to return a specific set of data. <br>

different defined functions- Functions are building block in python that enable you to organise and reuse code. They can be used for carrying out certain tasks. They are used to accept or not accept an input.<br>

print statements- print statements are used to print messages into the terminal. They can also be used to check you code is working how you want it to, if it works then you can remove it. Can also be used toi give feed back in the terminal. <br>

calling a function(my code example-get_attendance_data())- in python you cannot call a function above the function. A function is called to execute its code. <br>

Try except statement- The except statement will print an error to the terminal if the try statement doesnt work. Within the try statement can go an if statement which you use to determine the next move within the code for example IF the number is correct then do this<br>


### why I used
commented out section and code under it- I commeneted out two specific functions in my code since underneath i refactored the two speices of code that combined the two to make it more concise.<br>

range() (my code example-(1, 7))- I used range in my code to loop through the data six times, 1 through 7. This range was used to access one of the six yoga types. <br>

_row & .col- col stasnds for column. .col is used when you want to access a column. _row was used in my code to access a row.

split() method- This method returns the broken up values as a list. I used split(",") to remove the commas from my list of numbers.<br>

int - Int is short for integer. You would use int when you want to convert a value into an integer for example a string. You can't do mathmatical equations with an integer and a string therefore you need to convert the string into an integer.

len()- This is used to check how many values are in a list. It will return the number of values in it. <br>

raise ValueError- This is used to write your own error message, you can use an f statement to write the message (f"") <br>

f strings(f"")- These provide a concise and intuative way to embed expressions and variables directly into strings.<br>

.append- the append method is used to add something. for example in my code, i used append_row which adds a new row to my spreadsheet. <br>

SHEET.worksheet- The sheet variable is used by implemeting the gspread library. This links to my google sheets so that i can push and pull data from it. using SHEET.worksheet lets the worksheet know that we want to pull data from it. <br>

zip- The zip method allows you to iterate through two iterable lists at the same time. In terms of my code, interate through the placesAvailable and attendance list to get the placesLeft data.<br>

new line character(\n)- \n is used to create an extra space between lines this helps with readability. <br>

docstring- a docstring consists of tripple double quotes split in half with two vertical spaces between them e.g """""". Inbetween these quotes is information describing what the function does. They are used to tell other developers what the function does and why its there. They shopuld always be right under the function name in the function.<br>

pprint()- PPrint needs to be imported before using, this goes at the top of the code(from pprint import pprint). it formats the structure in a way that is easier to read.


### Flowchart
demonstrates how the system should work in words<br>

<img src="![image1](https://github.com/user-attachments/assets/7995cee4-3aac-4349-83d0-9f4a41841dd7)" width="600" height="400">



### End goal
my end goal  for this project is to gather user input and calculate averages for places in future sessions. This is accomplished by calculating how many attended and how many places were left.

### Future goals
In the future I would like to incorperate images so users can usually see how many spaces are left. 
