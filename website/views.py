from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request, "website/homepage.html", context={})

def login(request):
    return render(request, "website/login.html", context={})

def food_database(request):
    return render(request, "website/food_database.html", context={})

def patient(request):
    return render(request, "website/patient.html", context={})

def assessment_all(request):
    return render(request, "website/assessment_all.html", context={})

def assessment_detail(request, assessment_id):
    return render(request, "website/assessment_detail.html", context={"assessment_id": assessment_id})

def recipe_all(request):
    return render(request, "website/recipe_all.html", context={})

def recipe_detail(request, recipe_id):
    return render(request, "website/recipe_detail.html", context={"recipe_id": recipe_id})
