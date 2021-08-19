from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import CategorySerializer
from .models import Category

@api_view(['GET'])
def apiOverview(request):
    category_api_urls = {
        'List': '/category/list/',
        'Detail': '/category/detail/<str:pk>/',
        'Create' : '/category/create',
        'Update': '/category/update/<str:pk>/',
        'Delete': '/category/delete/<str:pk>/',

    }
    return Response(category_api_urls)


@api_view(['GET'])
def categorylist(request):
    category = Category.objects.all()
    serializer = CategorySerializer(category, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def categoryDetail(request, pk):
    category = Category.objects.get(id=pk)
    serializer = CategorySerializer(category, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def categoryCreate(request):
    serializer = CategorySerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def categoryUpdate(request, pk):
    category = Category.objects.get(id=pk)
    serializer = CategorySerializer(instance=category,data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def categoryDelete(request, pk):
    category = Category.objects.get(id=pk)
    if category:
        category.delete()

    return Response('Item Delete Successfully')