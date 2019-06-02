from rest_framework import serializers
from .models import Food, Patient, Assessment, AssessmentUse, Recipe, RecipeUse


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = "__all__"


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ("id", "index", "name", "age", "gender", "height", "weight", "disease",)


class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = ("id", "index", "generated_time", "patient", "generated_person",)

    def to_representation(self, instance):
        self.fields['patient'] =  PatientSerializer(read_only=True)
        return super().to_representation(instance)


class AssessmentBreifSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = ("id",)


class AssessmentUseSeriazlizer(serializers.ModelSerializer):
    class Meta:
        model = AssessmentUse
        fields = ("assessment","id","food","use_weight","meal_type",)

    def to_representation(self, instance):
        self.fields['assessment'] =  AssessmentBreifSerializer(read_only=True)
        self.fields['food'] =  FoodSerializer(read_only=True)
        return super().to_representation(instance)


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ("id", "name", "recipe_type", "generated_time", "generated_person",)


class RecipeBreifSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ("id","name",)


class RecipeOperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ("id","operation",)


class RecipeUseSeriazlizer(serializers.ModelSerializer):
    class Meta:
        model = RecipeUse
        fields = ("recipe","id","food","use_weight","element_type",)

    def to_representation(self, instance):
        self.fields['recipe'] =  RecipeBreifSerializer(read_only=True)
        self.fields['food'] =  FoodSerializer(read_only=True)
        return super().to_representation(instance)
