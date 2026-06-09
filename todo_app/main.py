def get_todo():
    with open("todo.txt","r") as file:
        todos_l = file.readlines()
    return todos_l


def update_todo(todos_l):
    with open("todo.txt","w") as file:
            file.writelines(todos_l)


while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip() # trim the white space

    if user_action.startswith('add'):
        todo = user_action[4:]

        # file = open("todo.txt","r")
        # todos = file.readlines()
        # file.close()
        #  optimization with "with context manager"

        todos = get_todo()

        todos.append(todo + '\n')

        update_todo(todos)
  
    elif user_action.startswith('show'):
        
        todos = get_todo()

        # list comprehension 
        # new_todos = [items.strip('\n') for items in todos] 
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
            
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todo()
            
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            update_todo(todos)
            
        except ValueError:
            print("Your command is not vaild")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            
            todos = get_todo()
            index = number -1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            update_todo(todos)

            print(f"Todo '{todo_to_remove}' was removed from the list")
        except IndexError:
            print("there is no item with that number")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("Command is not vaild.")

print("Bye")
