import methods

Tasks = []

while True:
    methods.showmenu()
    option = input("Which operation would like to run :")
    if int(option) == 1:
        t = methods.CreateTask()
        if t:
            Tasks.append(t)
            print("Task created successfully")
    elif int(option) == 2:
        x = input("Give the name of the task you want to update: ")
        if(methods.UpdateTask(Tasks, x) == 1):
            print("Task updated successfully")
        else : 
            print("Invalid Task name")
    elif int(option) == 3:
        x = input("Give the name of the task you want to delete: ")
        if(methods.DeleteTask(Tasks, x) == 1):
            print("Task deleted successfully")
        else : 
            print("Invalid Task name")
    elif int(option) == 4:
        x = input("Give the name of the task you want to search for: ")
        if(methods.SearchTask(Tasks, x) != 0):
            print("Task Found")
        else :
            print("Task does not exist")
    elif int(option) == 8:
        x = int(input("Give the name of the tasks you want to create: "))
        if(methods.createRandomTask(Tasks, x) == 1):
            print("Tasks created sucessfully")
        else :
            print("There was an error")
    elif int(option) == 5:
        methods.ListTasks(Tasks)
    