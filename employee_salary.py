import pandas as pandas
import matplotlib.pyplot as plt
from pathlib import Path

#Read employee data from csv file
folder = Path(_file_).parent
df = pd.read_csv(folder/"employee.csv")

#Display employee names,departments, and salarieas
print("Employee Details:")
print(df[["Name", "Departmenr", "Salary"]])

#Calculate avaerage salary for each department
avg_salary=
df.groupby("Department")
["Salary"].mean()

print("\nAverage Salary by Deapartment:")
print(avg_salary)

#Plot average salary by department
avg_salary.plot(kind="bar", color="skyblue")

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.tight_layout()
plt.show()
