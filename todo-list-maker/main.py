from asyncio import Task
from datetime import date 

quit_value = True

while quit_value:

    user = input("Hello, what is your name?: ")
    print("Hello: ", user)
    current_date = date.today()
    print("Today is: ", current_date)
    current_task = input("What would you like to do today?: ")
    current_task = current_task.lower()
    current_priority = input("What is the numerical priority value of this task?: ")
    current_priority_input = []
    current_priority_input = current_priority_input.append(current_priority)
    output_statement = print("Task: ", current_task, " Date: ", current_date, " Priority: ", current_priority)

    check_keep_going = input("Would you like to keep going? Type 'Y' or 'N': ")
    check_keep_going = check_keep_going.lower()
    if check_keep_going == 'y':
        quit_value = True
    else:
        quit_value = False


    
