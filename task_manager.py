# Compulsory Task

from datetime import datetime
from datetime import date
import pandas as pd # Pandas was installed using pip
import os.path

# NOTE: Jinja2 was installed using pip
# NOTE: The date format as given in tasks.txt was adopted as the standard for this task. Any other date formats will not be accepted by gen_reports() function.

# Set pandas options to display all data (by default only the first and last column are displayed if the dataset is large
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

valid = False
while valid == False:
    # While the username in password is not one of those in user.txt, prompt the user for a valid username and password
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    with open('user.txt', 'r') as u:
        for line in u:
            line_list = []
            line_list = line.split(',') # Now line_list is a list with 2 items: the line's username and password
            valid_username = line_list[0]
            valid_password = line_list[1].strip()
            if username == valid_username and password == valid_password: # Only if the username and password entered match the strings in user.txt exactly
                valid = True
# Note: The file user.txt is now closed

# Set up a function that displays the main menu
# All along we do checks to ensure that all inputs are valid, otherwise the user is prompted again
def main_menu(username): # Here username is a local variable
    valid_choice = False
    while valid_choice == False:
        if username == 'admin':
            choice = input("Please select one of the following options: \nr - register user \na - add task \nva - view all tasks \nvm - view my tasks \ngr - generate reports \nds - view statistics \ne - exit \n")
            choice = choice.strip()
            choice = choice.lower()
            if choice == 'r' or choice == 'a' or choice == 'va' or choice == 'vm' or choice == 'gr' or choice == 'ds' or choice == 'e':
                valid_choice = True
        else:
            choice = input("Please select one of the following options: \nr - register user \na - add task \nva - view all tasks \nvm - view my tasks \ne - exit \n")
            choice = choice.strip()
            choice = choice.lower()
            if choice == 'r' or choice == 'a' or choice == 'va' or choice == 'vm' or choice == 'e':
                valid_choice = True
    return choice

# Show menu to user and prompt them for a choice
choice = main_menu(username) # Here username is a global variable
# When a menu item is selected, the relevant function is called

# Build the functions for each option/functionality in main menu

def reg_user():
    confirm = False
    exists = False
    while confirm == False:
        new_username = input("Please enter a new username: ")
        usernames = get_usernames() # Call the function that returns a list of all usernames
        for i in usernames:
            if i == new_username:
                print("The username you have entered already exists.")
                exists = True
                break # Terminate for-loop the moment that the username entered already exists. This will take us straight to the 'continue' statement which will skip to the next iteration of the while-loop to prompt for a different new username.
            else:
                exists = False
        if exists == True:
            continue # If the new username entered already exists the current iteration of the while-loop must be terminated and the loop must start from the top
        new_password = input("Please enter a new password: ")
        confirm_password = input("Please enter the password again: ")
        if new_password == confirm_password:
            confirm = True
        if confirm != True:
            print("You did not enter the same password. Please enter a new username and password again.")
    with open('user.txt', 'a') as u:
        u.write("\n" + new_username + ", " + new_password)

# Also add a function that generates a list of all usernames for easy access
# Other functions may use this function as it returns the list of all registered users
def get_usernames():
    usernames = []
    with open('user.txt', 'r') as u:
        for line in u:
            line_list = []
            line_list = line.split(',')
            usernames.append(line_list[0])
    return usernames
    
def add_task():
    usernames = get_usernames() # Call the function that returns a list of all usernames
    match = False
    while match == False:
        user = input("Please enter the username of the person responsible for this task: ")
        for i in range(0, len(usernames)):
            if user == usernames[i]:
                match = True
        if match == False: # If the username entered is not in the list of usernames
            print("User was not found.")
    task = input("Please enter the title of the task: ")
    description = input("Please enter a description of the task: (Note that this description may not include commas) ")
    date_assigned = date.today()
    date_due = input("Please enter the day on which this task is due. Take note that dates must be entered in the format '23 Jan 2018' for example: ")
    complete = "No" # Default
    with open('tasks.txt', 'a') as t:
        t.write("\n" + user + ", " + task + ", " + description + ", " + str(date_assigned) + ", " + date_due + ", " + complete)

# Also add a function that generates lists of different components of all tasks for easy access
# Other functions may use this function as it returns a list of lists
def get_tasks():
    task_counter = 1
    tasks = []
    task_numbers = []
    task_usernames = []
    task_titles = []
    task_descriptions = []
    assigned_dates = []
    due_dates = []
    task_complete = []
    with open('tasks.txt', 'r') as t:
        for line in t:
            if line != "\n":
                line_list = []
                line_list = line.split(',')
                task_numbers.append(task_counter)
                task_usernames.append(line_list[0]) # Add all usernames to first list inside list
                line_list[1] = line_list[1].strip()
                task_titles.append(line_list[1]) # Add all task names to second list inside list
                line_list[2] = line_list[2].strip()
                task_descriptions.append(line_list[2]) # Add all task descriptions to third list inside list
                line_list[3] = line_list[3].strip()
                assigned_dates.append(line_list[3]) # Add all assignment dates to fourth list inside list
                line_list[4] = line_list[4].strip()
                due_dates.append(line_list[4]) # Add all due dates to fifth list inside list
                line_list[5] = line_list[5].strip()
                task_complete.append(line_list[5]) # Add all completion indicators to sixth list inside list
                task_counter += 1
    # Now create a list of all these lists
    tasks.append(task_numbers)
    tasks.append(task_usernames) # The second list inside the list is usernames corresponding to tasks
    tasks.append(task_titles) # The third list inside the list is names of all tasks
    tasks.append(task_descriptions) # The fourth list inside the list is all descriptions of tasks
    tasks.append(assigned_dates) # The fifth list inside the list is dates on which all tasks were assigned
    tasks.append(due_dates) # The sixth list inside the list is due dates of all tasks
    tasks.append(task_complete) # The seventh list inside the list is 'No's' and 'Yes's' that indicate whether each task is complete
    # Now each task has a unique index in each list, containing a different component of the task, inside the big list
    return tasks

def view_all():
    list_of_tasks = get_tasks() # Call the function that returns a list of lists with all task information
    # We can use specific indices without a loop since the tasks will always be in a specific format from the input file
    tasks = {'Person responsible': list_of_tasks[1],
             'Task title': list_of_tasks[2],
             'Description of task': list_of_tasks[3],
             'Date assigned': list_of_tasks[4],
             'Date due': list_of_tasks[5],
             'Is this task complete?': list_of_tasks[6]}
    df = pd.DataFrame(tasks)
    print(df) # What is not displayed is each task's unique number

def view_mine():
    all_tasks = get_tasks()
    task_counter = 1
    task_to_edit = 0
    nums_of_tasks = []
    num_of_task_all = []
    my_task_usernames = []
    my_task_titles = []
    my_task_descriptions = []
    my_assigned_dates = []
    my_due_dates = []
    my_task_complete = []
    edit_indices = []
    for i in range(0, len(all_tasks[1])):
        if all_tasks[1][i] == username: # If the task correspeonds to the username, we add the details of the task to it's corresponding list (Note: This list is temporary and gets overwritten everytime the function is called)
            num_of_task_user = task_counter
            # The below block works similarly to that of the get_tasks() function
            num_of_task_all.append(all_tasks[0][i])
            nums_of_tasks.append(num_of_task_user)
            my_task_usernames.append(all_tasks[1][i])
            my_task_titles.append(all_tasks[2][i])
            my_task_descriptions.append(all_tasks[3][i])
            my_assigned_dates.append(all_tasks[4][i])
            my_due_dates.append(all_tasks[5][i])
            my_task_complete.append(all_tasks[6][i])
            # Later we will need a variable containing indices, that associate the number of a specific user's task with that task in the list of ALL tasks
            edit_indices.append((i, task_counter)) # List of tuples with the first entry being the index of the task in the global list, and the second being the task number in the specific user's list
            task_counter += 1 # Everytime that a task occurs for a particular user, the number of the next task should be increased by 1
    my_tasks = {'Number of task': nums_of_tasks,
                'Task title': my_task_titles,
                'Description of task': my_task_descriptions,
                'Date assigned': my_assigned_dates,
                'Date due': my_due_dates,
                'Is this task complete?': my_task_complete}
    df2 = pd.DataFrame(my_tasks)
    df2.style.set_table_styles([{'selector' : '',
                            'props' : [('border',
                                        '10px solid yellow')]}])
    print(df2)
    choice2 = input("Please type a task number you wish to edit or type -1 to return to the main menu: ")
    if choice2 == str(-1):
        main_menu(username)
    else:
        for i in nums_of_tasks:
            if int(choice2) == int(i):
                task_to_edit = int(choice2)
    # Allow user to edit the task
    if choice2 != str(-1):
        index = 0
        for i in edit_indices:
            if int(choice2) == i[1]:
                index = i[0] # Now index contains the index of the task to be edited in the GLOBAL list of tasks
        # APPLY CHANGES
        edit = input("Please enter 1 if you wish to mark the task as complete or enter 2 if you wish to edit the task: ")
        if int(edit) == 1:
            with open('tasks.txt', "r") as t:
                list_of_lines = t.readlines()
                list_of_lines[index] = my_task_usernames[task_to_edit - 1] + ", " + my_task_titles[task_to_edit - 1] + ", " + my_task_descriptions[task_to_edit - 1] + ", " + str(my_assigned_dates[task_to_edit - 1]) + ", " + my_due_dates[task_to_edit - 1] + ", " + "Yes" + "\n"
            with open('tasks.txt', "w") as t:
                t.writelines(list_of_lines)
        elif int(edit) == 2:
            if my_task_complete[task_to_edit - 1] == "No":
                edit2 = input("Please enter 1 if you wish to change the person responsible for the task or enter 2 if you wish to change the due date: ")
                if int(edit2) == 1:
                    new_person = input("Please enter the new person responsible for the task: ")
                    with open('tasks.txt', "r") as t:
                        list_of_lines = t.readlines()
                        list_of_lines[index] = new_person + ", " + my_task_titles[task_to_edit - 1] + ", " + my_task_descriptions[task_to_edit - 1] + ", " + str(my_assigned_dates[task_to_edit - 1]) + ", " + my_due_dates[task_to_edit - 1] + ", " + my_task_complete[task_to_edit - 1] + "\n"
                    with open('tasks.txt', "w") as t:
                        t.writelines(list_of_lines)
                elif int(edit2) == 2:
                    new_date = input("Please enter the new due date of the task: ")
                    with open('tasks.txt', "r") as t:
                        list_of_lines = t.readlines()
                        list_of_lines[index] = my_task_usernames[task_to_edit - 1] + ", " + my_task_titles[task_to_edit - 1] + ", " + my_task_descriptions[task_to_edit - 1] + ", " + str(my_assigned_dates[task_to_edit - 1]) + ", " + new_date + ", " + my_task_complete[task_to_edit - 1] + "\n"
                    with open('tasks.txt', "w") as t:
                        t.writelines(list_of_lines)   
            else:
                print("You cannot edit a task that has been completed.")

def gen_reports():
    # Initiate variables to store overall task data
    total_num_tasks = 0
    completed = 0
    uncompleted = 0
    overdue = 0
    # The following 3 variables will store the indices of completed, uncompleted and overdue tasks respectively (inidces are from the list of ALL tasks)
    completed_indices = []
    uncompleted_indices = []
    overdue_indices = []
    # Initiate variables to store specific user's data
    tuples_num_tasks_assigned = [] # Will contain tuples with the first element of each tuple being the user and the second element being the number of tasks assigned to them 
    tuples_percent_tasks_assigned = [] # Similarly for the following tuple lists but for different attributes of tasks
    tuples_percent_tasks_completed = []
    tuples_percent_tasks_uncompleted = []
    tuples_percent_tasks_overdue = []
    
    all_tasks = get_tasks()
    all_users = get_usernames()

    # Gather all info regarding all tasks
    total_num_tasks = len(all_tasks[0])
    total_num_users = len(all_users)
    for i in range(0, len(all_tasks[6])):
        if all_tasks[6][i] == "Yes":
            completed += 1
            completed_indices.append(i)
        if all_tasks[6][i] == "No":
            uncompleted += 1
            uncompleted_indices.append(i)
    for j in range(0, len(all_tasks[5])):
        due = datetime.strptime(all_tasks[5][j], "%d %b %Y") #The lowercase b indicates that the abbreviated month name is used
        present = datetime.now()
        if due.date() < present.date() and all_tasks[6][j] != "Yes":
            overdue += 1
            overdue_indices.append(j)
    percent_incomplete = uncompleted/total_num_tasks*100
    percent_overdue = overdue/total_num_tasks*100

    # Gather all info regarding all users and their specific tasks
    for user in all_users:
        print("new user")
        user_completed = 0
        num_tasks_assigned = 0
        user_uncompleted = 0
        user_overdue = 0
        for i in range(0, len(all_tasks[0])):
            if all_tasks[1][i] == user:
                num_tasks_assigned += 1
        tuples_num_tasks_assigned.append((user, num_tasks_assigned))
        tuples_percent_tasks_assigned.append((user, num_tasks_assigned/total_num_tasks*100))
        print(num_tasks_assigned)
        if num_tasks_assigned != 0:
            for k in range(0, len(completed_indices)):
                if completed_indices[k]+1 == all_tasks[0][completed_indices[k]] and user == all_tasks[1][completed_indices[k]]:
                    user_completed += 1
            tuples_percent_tasks_completed.append((user, user_completed/num_tasks_assigned*100))
            print(user_completed)
            for k in range(0, len(uncompleted_indices)):
                if uncompleted_indices[k]+1 == all_tasks[0][uncompleted_indices[k]] and user == all_tasks[1][uncompleted_indices[k]]:
                    print("executed")
                    user_uncompleted += 1
            tuples_percent_tasks_uncompleted.append((user, user_uncompleted/num_tasks_assigned*100))
            print(user_uncompleted)
            for k in range(0, len(overdue_indices)):
                if overdue_indices[k]+1 == all_tasks[0][overdue_indices[k]] and user == all_tasks[1][overdue_indices[k]]:
                    user_overdue += 1
            tuples_percent_tasks_overdue.append((user, user_overdue/num_tasks_assigned*100))
            print(user_overdue)
        

    
    with open('task_overview.txt', 'a') as to:
        to.write("The total number of tasks that have been generated is " + str(total_num_tasks) + "." + "\n"
                 "The total number of completed tasks is " + str(completed) + "." + "\n"
                 "The total number of uncompleted tasks is " + str(uncompleted) + "." + "\n"
                 "The total number of tasks overdue is " + str(overdue) + "." + "\n"
                 "The percentage of incomplete tasks is " + str(percent_incomplete) + "%." + "\n"
                 "The percentage of tasks overdue is " + str(percent_overdue) + "%." + "\n")
    with open('user_overview.txt', 'a') as uo:
        uo.write("The total number of users registered is " + str(total_num_users) + "." + "\n"
                 "The total number of tasks that have been generated is " + str(total_num_tasks) + "." + "\n")
        for tuples in tuples_num_tasks_assigned:
            uo.write("The total number of tasks assigned to " + tuples[0] + " is " + str(tuples[1]) + "." + "\n")
        for tuples in tuples_percent_tasks_assigned:
            uo.write("The percentage of total tasks assigned to " + tuples[0] + " is " + str(tuples[1]) + "%." + "\n")
        for tuples in tuples_percent_tasks_completed:
            uo.write("The percentage of their tasks completed by " + tuples[0] + " is " + str(tuples[1]) + "%." + "\n")
        for tuples in tuples_percent_tasks_uncompleted:
            uo.write("The percentage of their tasks not yet completed by " + tuples[0] + " is " + str(tuples[1]) + "%." + "\n")
        for tuples in tuples_percent_tasks_overdue:
            uo.write("The percentage of their tasks overdue by " + tuples[0] + " is " + str(tuples[1]) + "%." + "\n")
        
def view_stats(): # Only for admin
    count_users = 0
    count_tasks = 0
    exists = False
    while exists == False: # If the reports don't exist yet, generate them first
        if os.path.isfile('user_overview.txt'):
            exists = True
        else:
            gen_reports()
    with open('user_overview.txt', 'r') as uo:
        for line in uo:
            count_users = line[-3] # The last number in the first line before fullstop in user_overview will always contain the number of users (Note that index -1 is a newline character and -2 is a fullstop)
            break # Do not iterate over all lines, the first one is all we need
    with open('task_overview.txt', 'r') as to:
        for line in to:
            count_tasks = line[-3] # The last number in the first line before fullstop in task_overview will always contain the number of tasks (Note that index -1 is a newline character and -2 is a fullstop)
            break # Do not iterate over all lines, the first one is all we need
    print("The number of users registered is: " + str(count_users))
    print("The number of tasks in progress is: " + str(count_tasks))
    
# Based on the choice by the user, call the relevant function
if choice == 'r' and username == 'admin':
    reg_user()
elif choice == 'r' and username != 'admin':
    print("You are not authorised to use this functionality.")

if choice == 'a':
    add_task()
    
if choice == 'va':
    view_all()

if choice == 'vm':
    view_mine()

if choice == 'gr':
    gen_reports()
   
if choice == 'ds':
    view_stats()
    



