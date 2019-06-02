from django.contrib import admin
from .models import Food, Assessment, Patient, AssessmentUse, Recipe, RecipeUse

# Register your models here.

admin.site.register(Food)
admin.site.register(Assessment)
admin.site.register(Patient)
admin.site.register(AssessmentUse)
admin.site.register(Recipe)
admin.site.register(RecipeUse)
