salaries = [30000, 45000, 60000, 80000]

salaries = list(map(lambda s: (s*0.10),salaries))

print(salaries)
# Expected output:
#[3000.0, 4500.0, 6000.0, 8000.0]

employees = [
    {"name": "Asha", "salary": 50000},
    {"name": "Ravi", "salary": 60000},
    {"name": "Priya", "salary": 70000}
]

employees = list(map(lambda e: e["name"],employees))

print(employees)
# Expected output:
#["Asha", "Ravi", "Priya"]
