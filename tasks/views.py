from django.shortcuts import render


# Home page that shows links of all tasks
def index(request):
    return render(request, "tasks/index.html")


# ---------- TASK 1: Student Result Portal ----------
def result_portal(request):
    # Student data is stored in a dictionary
    student = {
        "name": "Aarav Mehta",
        "roll_no": "AIDS-2026-014",
        "course": "B.Tech CSE (AI & Data Science)",
        "marks": {
            "Mathematics": 78,
            "Physics": 65,
            "Chemistry": 71,
            "English": 82,
            "Computer Science": 90,
        },
    }

    # Add all the marks and find the percentage
    total = sum(student["marks"].values())
    max_total = len(student["marks"]) * 100
    percentage = round(total / max_total * 100, 2)

    # Send everything to the template
    context = {
        "student": student,
        "total": total,
        "max_total": max_total,
        "percentage": percentage,
    }
    return render(request, "tasks/result.html", context)


# ---------- TASK 2: Online Shopping Product Cards ----------
def shopping(request):
    # List of 8 products, each product is one dictionary
    products = [
        {"name": "Wireless Headphones", "price": 2999, "category": "Electronics",
         "discount": 20, "image": "images/products/p1.png"},
        {"name": "Running Shoes", "price": 3499, "category": "Footwear",
         "discount": 15, "image": "images/products/p2.png"},
        {"name": "Smart Watch", "price": 4999, "category": "Electronics",
         "discount": 25, "image": "images/products/p3.png"},
        {"name": "Laptop Backpack", "price": 1499, "category": "Fashion",
         "discount": 10, "image": "images/products/p4.png"},
        {"name": "Steel Water Bottle", "price": 599, "category": "Home",
         "discount": 5, "image": "images/products/p5.png"},
        {"name": "UV Sunglasses", "price": 1299, "category": "Fashion",
         "discount": 30, "image": "images/products/p6.png"},
        {"name": "Bluetooth Speaker", "price": 2199, "category": "Electronics",
         "discount": 18, "image": "images/products/p7.png"},
        {"name": "LED Desk Lamp", "price": 899, "category": "Home",
         "discount": 12, "image": "images/products/p8.png"},
    ]

    # Final Price = Price - Discount Amount
    for p in products:
        discount_amount = p["price"] * p["discount"] / 100
        p["final_price"] = round(p["price"] - discount_amount, 2)

    return render(request, "tasks/shopping.html", {"products": products})


# ---------- TASK 7: Hotel Room Listing ----------
def hotel_rooms(request):
    # 5 rooms, "available" is True or False
    rooms = [
        {"number": 101, "type": "Standard Room", "price": 2500,
         "available": True, "image": "images/rooms/room1.png"},
        {"number": 204, "type": "Deluxe Room", "price": 4200,
         "available": True, "image": "images/rooms/room2.png"},
        {"number": 305, "type": "Suite", "price": 7800,
         "available": False, "image": "images/rooms/room3.png"},
        {"number": 112, "type": "Family Room", "price": 5600,
         "available": True, "image": "images/rooms/room4.png"},
        {"number": 501, "type": "Executive Suite", "price": 9500,
         "available": False, "image": "images/rooms/room5.png"},
    ]
    return render(request, "tasks/hotel_rooms.html", {"rooms": rooms})


# ---------- TASK 9: Loan Eligibility Checker ----------
def loan_checker(request):
    result = None

    # This part runs only when the form is submitted
    if request.method == "POST":
        try:
            age = int(request.POST.get("age"))
            salary = int(request.POST.get("salary"))
            credit_score = int(request.POST.get("credit_score"))
        except (TypeError, ValueError):
            age = salary = credit_score = 0

        # My own eligibility rules
        if age >= 21 and age <= 60 and salary >= 30000 and credit_score >= 700:
            status, css = "Eligible", "ok"
            message = "Your loan is approved up to Rs. %d." % (salary * 20)
        elif age >= 21 and salary >= 20000 and (credit_score >= 600 or salary >= 50000):
            status, css = "Conditionally Eligible", "warn"
            message = "You need a guarantor and extra document checking."
        else:
            status, css = "Not Eligible", "bad"
            message = "Minimum: age 21+, salary Rs. 20,000+ and credit score 600+."

        result = {"age": age, "salary": salary, "credit_score": credit_score,
                  "status": status, "css": css, "message": message}

    return render(request, "tasks/loan.html", {"result": result})
