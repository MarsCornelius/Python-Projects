############################################################################
#                                                                          #
#                          Created By: Kibwe Gooding                       #
#                               Date: July 1st 2023                        #
#                            A Simple Task Manager                         #
############################################################################

import mysql.connector

database = mysql.connector.connect(host='', port=3306, database='', user='', password='')

if database.is_connected():
    print("Connection Successful..")

mycursor = database.cursor()

print("|-----------------------------------|")
print("|            Task Manager           |")
print("|-----------------------------------|")

print("\n-------------------------------------")
print("Commands: ")
print("1. Add")
print("2. Remove")
print("3. Edit")
print("4. View")
print("5. Exit")
print("-------------------------------------")

while True:
    option = int(input("\nSelect an option: "))
    print("\n")
    match option:
        case 1:
            task = input("Enter task: ")
            desc = input("Enter description: ")
            sql = "INSERT INTO tasks (task, description) VALUES (%s, %s)"
            entry = (task.capitalize(), desc.capitalize())
            mycursor.execute(sql, entry)

            database.commit()

            print("\ntask saved.")

        case 2:
            task = int(input("Delete task: "))
            sql = "DELETE FROM tasks where task_id = %s"
            task_id = (task,)
            mycursor.execute(sql, task_id)

            database.commit()

            print("task removed/completed.")

        case 3:
            task = int(input("Edit task: "))
            name = input("Enter new name: ")
            desc = input("Enter new description: ")

            sql = "UPDATE tasks SET task = %s, description = %s WHERE task_id = %s"

            task_info = (name, desc, task)

            mycursor.execute(sql, task_info)

            database.commit()

            print("task updated.")

        case 4:
            sql = "SELECT task_id, task, description from tasks"
            mycursor.execute(sql)

            my_tasks = mycursor.fetchall()

            for row in my_tasks:
                task_id, task, description = row
                print(f"{task_id}) {task}: {description}")
                print("-------------------------------------------------------")
        case 5:
            print("Saving tasks...done!")
            exit()
