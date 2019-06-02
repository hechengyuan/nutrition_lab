from django.urls import path, re_path
from .views import homepage, login, food_database, patient, assessment_all, assessment_detail, recipe_all, recipe_detail



app_name = "website"
urlpatterns = [
    path("",homepage, name="homepage"),
    path("login/", login, name="login"),
    path("lab/database/", food_database, name="food_database"),
    path("lab/patient/", patient, name="patient"),
    path("lab/assessment/", assessment_all, name="assessment_all"),
    path("lab/assessment/<int:assessment_id>/", assessment_detail, name="assessment_detail"),
    path("lab/recipe/", recipe_all, name="recipe_all"),
    path("lab/recipe/<int:recipe_id>/", recipe_detail, name="recipe_detail"),
]
