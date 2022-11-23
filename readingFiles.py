

employees_file = open("employees.txt", "r")

for employee in employees_file.readlines():
    print(employee)

# print(employees_file.readlines()[1])

employees_file.close()





