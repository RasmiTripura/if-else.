# Write a python program to input basic salary of an employee and calculate its
# Gross salary according to following:Basic Salary <= 10000 : HRA = 20%, DA = 80%
# Basic Salary <= 20000 : HRA = 25%, DA = 90%
# Basic Salary > 20000 : HRA = 30%, DA = 95%

basic_salary=int(input("Enter the basic salary="))
if basic_salary<=10000:
    HRA=basic_salary*0.2
    DA=basic_salary*0.8
    gross=basic_salary+HRA+DA
    print(gross,"is gross salary")
elif basic_salary<=20000:
    HRA=basic_salary*0.25
    DA=basic_salary*0.9
    gross=basic_salary+HRA+DA
    print("Gross salary is",gross)
elif basic_salary>20000:
    HRA=basic_salary*0.3
    DA=basic_salary*0.95
    gross=basic_salary+HRA+DA
    print("Gross salary=",gross)
else:
    print("No salary")