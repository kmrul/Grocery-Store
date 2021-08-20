from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Order, OrderLine
from .serializers import OrderSerializer, OrderLineSerializer

@api_view(['GET'])
def apiOverview(request):
    order_api_urls = {
        'List of Order': '/api/order/list/',
        'Detail of Order': '/api/order/detail/<str:pk>/',
        'Create Order' : '/api/order/create',
        'Update Order': '/api/order/update/<str:pk>/',
        'Delete Order': '/api/order/delete/<str:pk>/',
        'Create OrderLine': '/api/orderline/create',
        'OrderLine By Order': '/api/orderline/list/<str:pk>',
        'Update OrderLine': '/api/orderline/update/<str:pk>',
        'Delete OrderLine': '/api/orderline/delete/<str:pk>',

    }
    return Response(order_api_urls)

@api_view(['GET'])
def orderList(request):
    order = Order.objects.all()
    serializer = OrderSerializer(order, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def orderDetail(request, pk):
    order = Order.objects.get(id=pk)
    serializer = OrderSerializer(order, many=False)

    return Response(serializer.data)


@api_view(['POST'])
def orderCreate(request):
    serializer = OrderSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer)

@api_view(['POS'])
def orderUpdate(request, pk):
    order = Order.objects.get(id=pk)

    serializer = OrderSerializer(instance=order, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer)


@api_view(['DELETE'])
def orderDelete(request, pk):
    order = Order.objects.get(id=pk)

    serializer = OrderSerializer(order, many=False)
    if serializer.is_valid():
        serializer.delete()

    return Response("Order Deleted Successfully.")



@api_view(['GET'])
def orderLineByOrder(request, pk):
    orderLine = OrderLine.objects.get(order_id=pk)

    serializer = OrderLineSerializer(orderLine)

    return Response(serializer.data)


@api_view(['POST'])
def orderLineCreate(request):
    serializer = OrderLineSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def orderLineUpdate(request, pk):
    orderline = OrderLine.objects.get(id=pk)
    serializer = OrderLineSerializer(instance=orderline, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def orderLineDelete(request, pk):
    orderline = OrderLine.objects.get(id=pk)
    if orderline:
        orderline.delete()
    else:
        return Response("Product is not found.")

    return Response("Order Line deleted successfully")