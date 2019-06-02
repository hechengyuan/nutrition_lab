from django.db import models


# Create your models here.

class Food(models.Model):

    food_name = models.CharField(max_length=30)
    TYPE_CHOICES = [(1,"谷类"),(2,"肉类"),(3,"蛋类"),(4,"奶类"),(5,"豆类"),(6,"鱼及海产"),
        (7,"蔬菜"),(8,"水果"),(9,"坚果及零食"),(10,"调味品"),(11,"食用油"),(12,"腌制食物"),(13,"其他"),]
    type = models.IntegerField(choices=TYPE_CHOICES)
    calorie = models.DecimalField(max_digits=4, decimal_places=1)
    carbohydrate = models.DecimalField(max_digits=3, decimal_places=1, null=True)
    protein = models.DecimalField(max_digits=3, decimal_places=1, null=True)
    fat = models.DecimalField(max_digits=3, decimal_places=1, null=True)
    sodium = models.DecimalField(max_digits=6, decimal_places=1, null=True)
    fiber = models.DecimalField(max_digits=3, decimal_places=1, null=True)
    sugar = models.DecimalField(max_digits=3, decimal_places=1, null=True)
    calcium = models.DecimalField(max_digits=6, decimal_places=1, null=True)
    iron = models.DecimalField(max_digits=6, decimal_places=1, null=True)
    phosphorus = models.DecimalField(max_digits=6, decimal_places=1, null=True)
    potassium = models.DecimalField(max_digits=6, decimal_places=1, null=True)
    zinc = models.DecimalField(max_digits=6, decimal_places=1, null=True)
    vc = models.DecimalField(max_digits=6, decimal_places=1, null=True)
    thiamin = models.DecimalField(max_digits=6, decimal_places=1, null=True)
    riboflavin = models.DecimalField(max_digits=6, decimal_places=1, null=True)
    niacin = models.DecimalField(max_digits=6, decimal_places=1, null=True)
    va = models.DecimalField(max_digits=6, decimal_places=1, null=True)
    ve = models.DecimalField(max_digits=6, decimal_places=1, null=True)
    cholesterol = models.DecimalField(max_digits=6, decimal_places=1, null=True)

    def __str__(self):
        return self.food_name



class Patient(models.Model):

    name = models.CharField(max_length=30)
    index = models.CharField(max_length=30, blank=True)
    age = models.IntegerField()
    GENDER_CHOICES = [(1, "male"), (2, "female")]
    gender = models.IntegerField(choices=GENDER_CHOICES)
    height = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    weight = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    disease = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Assessment(models.Model):

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    index = models.IntegerField()
    generated_time = models.DateTimeField(auto_now=False, auto_now_add=True)
    generated_person = models.CharField(max_length=30, blank=True)
    foods = models.ManyToManyField(Food, through='AssessmentUse', through_fields=('assessment','food'))

    def __str__(self):
        return "{} {}".format(self.patient.name, self.generated_time)



class AssessmentUse(models.Model):

    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    use_weight = models.DecimalField(max_digits=4, decimal_places=1, null=False)
    MEAL_TYPE_CHOICE = [(1, "breakfast"), (2, "lunch"), (3, "dinner"), (4, "snacks"),]
    meal_type = models.IntegerField(choices=MEAL_TYPE_CHOICE, null=True)

    def __str__(self):
        return "{} {}".format(self.assessment.patient.name, self.food.food_name)



class Recipe(models.Model):

    name = models.CharField(max_length=30)
    recipe_type = models.CharField(max_length=30)
    generated_time = models.DateTimeField(auto_now=False, auto_now_add=True)
    generated_person = models.CharField(max_length=30, blank=True)
    foods = models.ManyToManyField(Food, through='RecipeUse', through_fields=('recipe','food'))
    operation = models.TextField(max_length=3000,blank=True)

    def __str__(self):
        return "{} {}".format(self.name, self.recipe_type)



class RecipeUse(models.Model):

    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    use_weight = models.DecimalField(max_digits=4, decimal_places=1, null=False)
    ELEMENT_TYPE_CHOICE = [(1, "main"), (2, "flavour"),]
    element_type = models.IntegerField(choices=ELEMENT_TYPE_CHOICE, null=True)

    def __str__(self):
        return "{} {}".format(self.recipe.name, self.food.food_name)
