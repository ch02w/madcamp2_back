# my_fridge/views.py
from rest_framework import generics, status
from rest_framework.response import Response
from .models import MyFridge
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
            food_id = serializer.validated_data['food_id']
            amount = serializer.validated_data['amount']
            expiration_date = serializer.validated_data['expiration_date']
            
            my_fridge_item, created = MyFridge.objects.update_or_create(
                user_id=user_id,
                food_id=food_id,
                defaults={'amount': amount, 'expiration_date': expiration_date}
            )
            
            return Response(MyFridgeSerializer(my_fridge_item).data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MyFridgeUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MyFridgeSerializer
    lookup_field = 'food_id'

    def get_queryset(self):
        user_id = self.kwargs['userId']
        return MyFridge.objects.filter(user_id=user_id, food_id=self.kwargs['food_id'])

    def update(self, request, *args, **kwargs):
        user_id = self.kwargs['userId']
        food_id = self.kwargs['food_id']
        serializer = MyFridgeUpdateSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            my_fridge_item = MyFridge.objects.filter(user_id=user_id, food_id=food_id).first()
            if my_fridge_item:
                my_fridge_item.amount = serializer.validated_data.get('amount', my_fridge_item.amount)
                my_fridge_item.expiration_date = serializer.validated_data.get('expiration_date', my_fridge_item.expiration_date)
                my_fridge_item.save()
                return Response(MyFridgeSerializer(my_fridge_item).data)
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        user_id = self.kwargs['userId']
        food_id = self.kwargs['food_id']
        my_fridge_item = MyFridge.objects.filter(user_id=user_id, food_id=food_id).first()
        if my_fridge_item:
            my_fridge_item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
