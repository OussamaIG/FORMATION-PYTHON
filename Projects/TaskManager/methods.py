import random

def showmenu():
    print("--TASK MANAGER--")
    print("1/ Add a new Task")
    print("2/ Update a Task")
    print("3/ Delete a Task")
    print("4/ Search for a Task")
    print("5/ List all Tasks")
    print("6/ List using Filtering")
    print("7/ Show Stats")
    print("8/ Random")
    print("q to quit")

def CreateTask():
    id = random.randint(123465,65689742121)
    name = input("Enter the name: ")
    desr = input("Enter the description: ")
    tag = input("Enter the tag(High/Low): ")
    status = "new"
    task = {"id": id, "name" : name, "des":desr, "tag": tag.lower(), "status":status}
    return task

def UpdateTask(Tasks, name):
    x = 0
    for task in Tasks:
        if task["name"] == name:
            while(x < 1 or x > 4):
                x = int(input("what do you want to update : (1:name, 2:desc, 3:tag, 4:status)"))  
            if x == 1:
                task["name"] = input("Give a new name")
            elif x == 2:
                task["des"] = input("Give a new description")
            elif x == 3:
                if(task["tag"] == "low"):
                    task["tag"] = "high"
                else:
                    task["tag"] = "high"
            elif x == 4:
                task["status"] = "completed"
            return 1
            
    return 0
    
def SearchTask(Tasks, name):
    for t in Tasks:
        if t["name"] == name:
            return t
    return 0

def DeleteTask(Tasks, name):
    if (SearchTask(Tasks, name) != 0):
        Tasks.remove(SearchTask(Tasks, name))
        return 1
    else:
        return 0

def createRandomTask(Tasks, x):
    task = {}
    choices = ["high", "low"]
    for i in range(x):
        task["id"] = random.randint(123465,65689742121)
        task["name"] = "task" + str(i)
        task["desc"] = " "
        task["status"] = "new"
        task["tag"] = random.choice(choices)
        Tasks.append(task)
        task = {}
    return 1
    
def ListTasks(Tasks):
    for task in Tasks:
        print("\n", task)