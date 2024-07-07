# my_fridge/views.py
from rest_framework import generics, status
from rest_framework.response import Response
from .models import MyFridge, User, Ingredient
from .serializers import MyFridgeSerializer, MyFridgeCreateSerializer, MyFridgeUpdateSerializer

class MyFridgeListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = MyFridgeSerializer

    def get_queryset(self):
        user_id = self.kwargs['userId']
        return MyFridge.objects.filter(user_id=user_id)

    def create(self, request, *args, **kwargs):
        user_id = self.kwargs['userId']
        serializer = MyFridgeCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=user_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MyFridgeUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MyFridge.objects.all()
    serializer_class = MyFridgeSerializer
    lookup_field = 'fridge_id'

    def update(self, request, *args, **kwargs):
        fridge_id = self.kwargs['fridge_id']
        instance = self.get_object()
        serializer = MyFridgeUpdateSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        fridge_id = self.kwargs['fridge_id']
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
