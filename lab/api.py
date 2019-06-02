from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

from .serializers import (FoodSerializer, PatientSerializer, AssessmentSerializer, AssessmentUseSeriazlizer,
    RecipeSerializer, RecipeUseSeriazlizer, RecipeOperationSerializer)
from .models import Food, Patient, Assessment, AssessmentUse, Recipe, RecipeUse


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login_api(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)


@csrf_exempt
@api_view(["GET","POST"])
@authentication_classes((TokenAuthentication,))
def food_list_api(request):
    if request.method == 'GET':
        param = request.GET.get('name')
        page = request.GET.get('page')
        if param == None:
            all_food = Food.objects.all().order_by("-id")
        if param != None:
            all_food = Food.objects.filter(food_name__contains=param).order_by("-id")
        paginator = Paginator(all_food, 20)
        try:
            food_list = paginator.page(page)
        except PageNotAnInteger:
            food_list = paginator.page(1)
        except EmptyPage:
            food_list = paginator.page(paginator.num_pages)
        serializer = FoodSerializer(food_list, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = FoodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@authentication_classes((TokenAuthentication,))
@api_view(['GET','PUT','DELETE'])
def food_change_api(request,id):
    food_detail = Food.objects.get(id=id)
    if request.method == "GET":
        serializer = FoodSerializer(food_detail)
        return Response(serializer.data)
    if request.method == "PUT":
        serializer = FoodSerializer(food_detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        food_detail.delete()
        return Response({"msg": "A-OK"}, status=status.HTTP_201_CREATED)


@csrf_exempt
@api_view(["GET","POST"])
@authentication_classes((TokenAuthentication,))
def patient_list_api(request):
    if request.method == "GET":
        param = request.GET.get('name')
        page = request.GET.get('page')
        if param == None:
            all_patient = Patient.objects.all().order_by("-id")
        if param != None:
            all_patient = Patient.objects.filter(name__contains=param).order_by("-id")
        paginator = Paginator(all_patient, 20)
        try:
            patient_list = paginator.page(page)
        except PageNotAnInteger:
            patient_list = paginator.page(1)
        except EmptyPage:
            patient_list = paginator.page(paginator.num_pages)
        serializer = PatientSerializer(patient_list, many=True, context={'request': request})
        return Response(serializer.data)
    if request.method == "POST":
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@authentication_classes((TokenAuthentication,))
@api_view(['GET','PUT','DELETE'])
def patient_change_api(request,id):
    patient_detail = Patient.objects.get(id=id)
    if request.method == "GET":
        serializer = PatientSerializer(patient_detail)
        return Response(serializer.data)
    if request.method == "PUT":
        serializer = PatientSerializer(patient_detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        patient_detail.delete()
        return Response({"msg": "A-OK"}, status=status.HTTP_201_CREATED)


@csrf_exempt
@api_view(["GET","POST"])
@authentication_classes((TokenAuthentication,))
def assessment_list_api(request):
    if request.method == "GET":
        page = request.GET.get('page')
        all_assessment = Assessment.objects.all().order_by("-generated_time")
        paginator = Paginator(all_assessment, 20)
        try:
            assessment_list = paginator.page(page)
        except PageNotAnInteger:
            assessment_list = paginator.page(1)
        except EmptyPage:
            assessment_list = paginator.page(paginator.num_pages)
        serializer = AssessmentSerializer(assessment_list, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = AssessmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@authentication_classes((TokenAuthentication,))
@api_view(['GET','PUT','DELETE'])
def assessment_change_api(request,id):
    assessment_detail = Assessment.objects.get(id=id)
    if request.method == "GET":
        serializer = AssessmentSerializer(assessment_detail)
        return Response(serializer.data)
    if request.method == "PUT":
        serializer = AssessmentSerializer(assessment_detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        assessment_detail.delete()
        return Response({"msg": "A-OK"}, status=status.HTTP_201_CREATED)


@csrf_exempt
@api_view(["GET","POST"])
@authentication_classes((TokenAuthentication,))
def get_detail_api(request,assessment_id):
    if request.method == "GET":
        assessment_use_list = AssessmentUse.objects.filter(assessment_id=assessment_id)
        serializer = AssessmentUseSeriazlizer(assessment_use_list, many=True, context={'request': request})
        return Response(serializer.data)
    if request.method == "POST":
        serializer = AssessmentUseSeriazlizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@authentication_classes((TokenAuthentication,))
@api_view(['GET','PUT','DELETE'])
def modify_detail_api(request,log_id):
    detail_log = AssessmentUse.objects.get(id=log_id)
    if request.method == "GET":
        serializer = AssessmentUseSeriazlizer(detail_log)
        return Response(serializer.data)
    if request.method == "PUT":
        serializer = AssessmentUseSeriazlizer(detail_log, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        detail_log.delete()
        return Response({"msg": "A-OK"}, status=status.HTTP_201_CREATED)


@csrf_exempt
@api_view(["GET","POST"])
@authentication_classes((TokenAuthentication,))
def recipe_list_api(request):
    if request.method == "GET":
        all_recipe = Recipe.objects.all()
        page = request.GET.get('page')
        paginator = Paginator(all_recipe, 20)
        try:
            recipe_list = paginator.page(page)
        except PageNotAnInteger:
            recipe_list = paginator.page(1)
        except EmptyPage:
            recipe_list = paginator.page(paginator.num_pages)
        serializer = RecipeSerializer(recipe_list, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@authentication_classes((TokenAuthentication,))
@api_view(['GET','PUT','DELETE'])
def recipe_change_api(request,id):
    recipe_detail = Recipe.objects.get(id=id)
    if request.method == "GET":
        serializer = RecipeSerializer(recipe_detail)
        return Response(serializer.data)
    if request.method == "PUT":
        serializer = RecipeSerializer(recipe_detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        recipe_detail.delete()
        return Response({"msg": "A-OK"}, status=status.HTTP_201_CREATED)


@csrf_exempt
@api_view(["GET","POST"])
@authentication_classes((TokenAuthentication,))
def get_recipe_detail_api(request,recipe_id):
    if request.method == "GET":
        recipe_use_list = RecipeUse.objects.filter(recipe_id=recipe_id)
        serializer = RecipeUseSeriazlizer(recipe_use_list, many=True, context={'request': request})
        return Response(serializer.data)
    if request.method == "POST":
        serializer = RecipeUseSeriazlizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@authentication_classes((TokenAuthentication,))
@api_view(['GET','PUT','DELETE'])
def modify_recipe_detail_api(request,log_id):
    detail_log = RecipeUse.objects.get(id=log_id)
    if request.method == "GET":
        serializer = RecipeUseSeriazlizer(detail_log)
        return Response(serializer.data)
    if request.method == "PUT":
        serializer = RecipeUseSeriazlizer(detail_log, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        detail_log.delete()
        return Response({"msg": "A-OK"}, status=status.HTTP_201_CREATED)


@csrf_exempt
@authentication_classes((TokenAuthentication,))
@api_view(['GET','PUT'])
def recipe_operation_api(request,recipe_id):
    recipe_operation = Recipe.objects.get(id=recipe_id)
    if request.method == "GET":
        serializer = RecipeOperationSerializer(recipe_operation)
        return Response(serializer.data)
    if request.method == "PUT":
        serializer = RecipeOperationSerializer(recipe_operation, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@authentication_classes((TokenAuthentication,))
@api_view(['GET','POST','PUT','DELETE'])
def fake_api(request):
    return Response({"msg": "You must use this fake api directly"}, status=status.HTTP_201_CREATED)
