import tasks

task_list = []

while True :
    print("add or remove item to list, else type done")
    user_input = input()

    if user_input == str("done"):
        break

    if task_list.__contains__(user_input):
        task = user_input
        tasks.remove_task(task_list, task)
    else :
        task = user_input
        tasks.add_task(task_list, task)


    print(task_list)
        



