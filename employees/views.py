from django.http import Http404
from django.shortcuts import render

# All employee data is stored here in views.py, so no database is needed.
# Each employee is one dictionary inside the list.
employees = [
    {"id": 101, "name": "Rohan Verma", "department": "Engineering",
     "designation": "Senior Software Engineer", "salary": 85000, "experience": 8,
     "city": "Bengaluru", "image": "images/employees/emp1.png", "status": "Active"},
    {"id": 102, "name": "Ananya Singh", "department": "Human Resources",
     "designation": "HR Manager", "salary": 62000, "experience": 6,
     "city": "Bhopal", "image": "images/employees/emp2.png", "status": "Active"},
    {"id": 103, "name": "Karan Patel", "department": "Finance",
     "designation": "Accountant", "salary": 38000, "experience": 4,
     "city": "Indore", "image": "images/employees/emp3.png", "status": "Active"},
    {"id": 104, "name": "Meera Iyer", "department": "Marketing",
     "designation": "Marketing Executive", "salary": 32000, "experience": 3,
     "city": "Pune", "image": "images/employees/emp4.png", "status": "On Leave"},
    {"id": 105, "name": "Vikram Rao", "department": "Engineering",
     "designation": "Backend Developer", "salary": 54000, "experience": 5,
     "city": "Hyderabad", "image": "images/employees/emp5.png", "status": "Active"},
    {"id": 106, "name": "Sneha Joshi", "department": "Design",
     "designation": "UI/UX Designer", "salary": 27000, "experience": 2,
     "city": "Mumbai", "image": "images/employees/emp6.png", "status": "Active"},
    {"id": 107, "name": "Arjun Nair", "department": "Operations",
     "designation": "Operations Associate", "salary": 24000, "experience": 1,
     "city": "Delhi", "image": "images/employees/emp7.png", "status": "On Leave"},
    {"id": 108, "name": "Pooja Desai", "department": "Engineering",
     "designation": "QA Engineer", "salary": 41000, "experience": 4,
     "city": "Raipur", "image": "images/employees/emp8.png", "status": "Active"},
]


# Bonus: find the level of every employee using the salary
for emp in employees:
    if emp["salary"] >= 50000:
        emp["level"], emp["level_class"] = "Senior Level", "senior"
    elif emp["salary"] >= 30000:
        emp["level"], emp["level_class"] = "Mid Level", "mid"
    else:
        emp["level"], emp["level_class"] = "Junior Level", "junior"


# Home page: shows total numbers and 3 featured employees
def home(request):
    context = {
        "total": len(employees),
        "active": len([e for e in employees if e["status"] == "Active"]),
        "departments": len(set(e["department"] for e in employees)),
        "featured": employees[:3],
    }
    return render(request, "employees/home.html", context)


# Employee List page: shows all employees
def employee_list(request):
    return render(request, "employees/employee_list.html", {"employees": employees})


# Employee Details page: emp_id comes from the URL, like /employee/101/
def employee_detail(request, emp_id):
    employee = None
    # Check the employees one by one and find the matching id
    for emp in employees:
        if emp["id"] == emp_id:
            employee = emp
            break
    # If no employee has this id, show the 404 page
    if employee is None:
        raise Http404("Employee not found")
    return render(request, "employees/employee_detail.html", {"employee": employee})


# About page
def about(request):
    return render(request, "employees/about.html")


# Contact page: shows a thank you message after the form is sent
def contact(request):
    sent = False
    if request.method == "POST":
        sent = True
        sender = request.POST.get("name")
        return render(request, "employees/contact.html", {"sent": sent, "sender": sender})
    return render(request, "employees/contact.html", {"sent": sent})
