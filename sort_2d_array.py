emps = [
    ('Asha', 'IT', 90000),
    ('Ravi', 'HR', 60000),
    ('Neha', 'IT', 90000),
    ('Om', 'HR', 75000)
]

emps.sort(key=lambda e: (e[1], -e[2], e[0]))

result = {}
for name, dept, salary in emps:
    if dept not in result:
        result[dept] = (name, dept, salary)

print(list(result.values()))
