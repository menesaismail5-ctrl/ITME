task = []

def main():
    while True:  
        print("Here is your todo list")
        print(task)
        print("press 1 to add new todo")
        print("press 2 to remove todo")
        print("press 3 to edit your to do list")
        print("press 4 to mark as done")
        print("press 5 to exit!!!")

        t = int(input())
        if t == 1:
            add()
        elif t == 2:
            remove()
        elif t == 3:
            edit()
        elif t == 4:
            mark_done()
        elif t == 5:
            print("Goodbye!")
            break
        else:
          print("invalid input")


def add():
    task.append(input("Enter new task: "))
    print(task)

def remove():
    task.remove(input("Enter task to remove: "))
    print(task)
    
def edit():
    print(task)
    i = int(input("task number to edit: "))
    task[i-1] = input("New value: ")

def mark_done():
    print(task)
    number = int(input("task number to mark as done: "))
    tas[number - 1] = task[number - 1] + " ✔"
    print(task)

def exit_program():
    print("Goodbye!")
    
    

main()
