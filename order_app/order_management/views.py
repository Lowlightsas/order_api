from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.core.cache import cache
from .models import Order,Product
from api.serializers import OrderSerializer,ProductSerializer

class OrderViewset(viewsets.ModelViewSet):
    queryset = Order.objects.filter(is_deleted=False)
    serializer_class = OrderSerializer

    def retrieve(self,request,*args,**kwargs):
        """ Получить заказ с использованием кэша """

        order_id = kwargs.get('pk')
        cached_order = cache.get(f"order_{order_id}")

        if cached_order:
            return Response(cached_order)
        
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        cahce.set(f"order_{order_id}",serializer.data,timeout=3600) #Кэш будет на 1 часик
        return Response(serializer.data)
    
