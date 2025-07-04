import pandas as pd

# --- Student DataFrame ---
student_data = {
    "name": ["sujal", "parth", "ritvik", "pragathi"],
    "marks": ["11", "20", "30", "40"],
    "grade": ["a", "b", "c", "d"],
    "age": [18, 19, 18, 18]
}
df_students = pd.DataFrame(student_data)
print("Student DataFrame:\n", df_students)

# --- Employee DataFrame ---
employee_data = {
    'EmployeeID': [101, 102, 103, 104, 105],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'HR'],
    'Salary': [50000, 60000, 55000, 65000, 52000],
    'JoinDate': ['2020-01-15', '2019-07-23', '2021-02-10', '2018-05-19', '2022-03-01'],
    'FullTime': [True, True, False, True, False]
}

df_employees = pd.DataFrame(employee_data)

# Drop 'JoinDate' column
df_employees.drop("JoinDate", axis=1, inplace=True)

# Rename 'EmployeeID' to 'ID'
df_employees.rename(columns={"EmployeeID": "ID"}, inplace=True)

print("\nEmployee DataFrame (after modifications):\n", df_employees)
