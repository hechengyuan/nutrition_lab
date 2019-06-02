from django.urls import path, re_path
from .api import (login_api, food_list_api, patient_list_api, assessment_list_api,
    food_change_api, patient_change_api, assessment_change_api, get_detail_api, modify_detail_api,
    recipe_list_api, recipe_change_api, get_recipe_detail_api, modify_recipe_detail_api,fake_api,recipe_operation_api)


app_name = "lab"
urlpatterns = [
    path('login/', login_api, name="login_api"),
    re_path(r'^food/$', food_list_api, name="food_list_api"),
    path('food/<id>/', food_change_api, name="food_change_api"),
    re_path(r'^patient/$', patient_list_api, name="patient_list_api"),
    path('patient/<id>/', patient_change_api, name="patient_change_api"),
    re_path(r'^assessment/$', assessment_list_api, name="assessment_list_api"),
    path('assessment/<id>/', assessment_change_api, name="assessment_change_api"),
    path('assessment_detail/<assessment_id>/', get_detail_api, name="get_assessment_detail_api"),
    path('assessment_detail/', fake_api, name="get_assessment_detail_fake_api"),
    path('log_detail/<log_id>/', modify_detail_api, name="modify_assessment_detail_api"),
    path('log_detail/', fake_api, name="modify_assessment_detail_fake_api"),
    re_path(r'^recipe/$', recipe_list_api, name="recipe_list_api"),
    path('recipe/<id>/', recipe_change_api, name="recipe_change_api"),
    path('recipe_detail/<recipe_id>/', get_recipe_detail_api, name="get_recipe_detail_api"),
    path('recipe_detail/',fake_api,name="get_recipe_detail_fake_api"),
    path('recipe_log_detail/<log_id>/', modify_recipe_detail_api, name="modify_recipe_detail_api"),
    path('recipe_log_detail/',fake_api, name="modify_recipe_detail_fake_api"),
    path('recipe_operation/<recipe_id>/',recipe_operation_api,name="recipe_operation_api"),
    path('recipe_operation/',fake_api,name="recipe_operation_fake_api"),
]
