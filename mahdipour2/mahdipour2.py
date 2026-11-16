salary = float(input("Enter monthly salary: "))

if salary <= 10000000:
    tax = 0

elif salary <= 25000000:
    tax = (salary - 10000000) * 0.10

else:
    tax = (15000000 * 0.10) + (salary - 25000000) * 0.20

child = input("Does the employee have a child? (yes/no): ")

if child == "yes":
    tax = tax - 500000

if tax < 0:
    tax = 0

net_salary = salary - tax

print("Monthly Salary:", salary)
print("Tax:", tax)
print("Net Salary:", net_salary)