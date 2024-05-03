todos = []

while True:
  user_action = input("Type add, show, or exit: ")
  match user_action.strip():  # .strip() removes trailing spaces
    case "add":
      todo = input("Enter a todo: ")
      todos.append(todo.strip())
      pass
    case "show" | "display":
      #print(todos)
      for item in todos:
        print(item.title())
      pass
    case "exit":
      exit(0)
    case _:
      print("Not a valid command.")


