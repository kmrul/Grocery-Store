from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ProductSerializer
from .models import Product

@api_view(['GET'])
def apiOverview(request):
    product_api_urls = {
        'List': '/api/product/list/',
        'Detail': '/api/product/detail/<str:pk>/',
        'Create' : '/api/productcreate',
        'Update': '/api/product/update/<str:pk>/',
        'Delete': '/api/product/delete/<str:pk>/',

    }
    return Response(product_api_urls)


@api_view(['GET'])
def productList(request):
    product = Product.objects.all()
    serializer = ProductSerializer(product, many=True)
    
    return Response(serializer.data)


@api_view(['GET'])
def productDetail(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product, many=False)

    return Response(serializer.data)

@api_view(['POST'])
def productCreate(request):
    serializer = ProductSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def productUpdate(request, pk):
    product = Product.objects.get(id=pk)
    if product:
        serializer = ProductSerializer(instance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()
    else:
        return Response("Product is not found")

    return Response(serializer.data)

@api_view(['DELETE'])
def productDelete(request, pk):
    product = Product.objects.get(id=pk)
    print("product:", product)
    if product:
        product.delete()
    else:
        return Response("Product is not found")

    return Response("Product is Deleted")
