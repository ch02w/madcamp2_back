from rest_framework import viewsets
from .models import Ingredients
from .serializers import IngredientSerializer

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientSerializer