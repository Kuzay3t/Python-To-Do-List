# This code is for task 1
# to build a to-do list application

to_do = []

def addTask():
    """Add a task"""
    task = input("Enter a task: \n")
    to_do.append(task)
    print(f'Task "{task}" added to the list')
    
        
def listTask():
    if not to_do:
        print("There are no tasks currently")
    else:
        print("Here are the tasks")
        for index,task in enumerate(to_do):
            print(f"Task {index}.{task}")
    
    
def deleteTask():
    listTask()
    try:
        taskToDelete = int(input("Enter the number you want to delete: "))
        if taskToDelete >=0 and taskToDelete < len(to_do):
            to_do.pop(taskToDelete)
            print(f"Task '{taskToDelete} has been removed")
        else:
            print(f"Task '{taskToDelete}' was not found")
    except:
        print("Invalid Input")
        
    
    
#task = input("Please enter a task to delete: \n")
    
       
def line():
    print('_' * 50)
    
if __name__ == "__main__":
    """Create a loop to run the app"""
    print("Welcome to the To-Do List App")
    line()
    while True:
       print("Please select one of the following options: ")
       print("""
             1. Add a task
             2. Delete a task
             3. View tasks
             4. Exit""")
       choice = int(input("Enter your choice as a number: "))
       if choice == 1:
           addTask()
       elif choice == 2:
           deleteTask()
       elif choice == 3:
           listTask()
       elif choice == 4:
              break
       else:
           print("Invalid Input, Please try again. ")
           break

           