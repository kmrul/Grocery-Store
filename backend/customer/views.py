from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Customer
from .serializers import CustomerSerializer

@api_view(['GET'])
def apiOverview(request):
    customer_api_urls = {
        'List': '/api/customer/list/',
        'Detail': '/api/customer/detail/<str:pk>/',
        'Create' : '/api/customer',
        'Update': '/api/customer/update/<str:pk>/',
        'Delete': '/api/customer/delete/<str:pk>/',

    }
    return Response(customer_api_urls)


@api_view(['GET'])
def customerList(request):
    customer = Customer.objects.all()
    if customer:
        serializer = CustomerSerializer(customer, many=True)
    
    else:
        return Response("No customer found")

    return Response(serializer.data)

@api_view(['GET'])
def customerDetail(request, pk):
    customer = Customer.objects.get(id=pk)
    if customer:
        serializer = CustomerSerializer(customer, many=True)
    else:
        return Response('No customer found')

    return Response(serializer.data)


@api_view(['POST'])
def customerCreate(request):
    serializer = CustomerSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def customerUpdate(request, pk):
    customer = Customer.objects.get(id=pk)

    serializer = CustomerSerializer(instance=customer, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def customerDelete(request, pk):
    customer = Customer.objects.get(id=pk)
    if customer:
        customer.delete()

    else:
        return Response('Customer is not found')

    return Response('Customer Deleted Successfully.')