from .models import Drink
from rest_framework.decorators import api_view
from .serializers import DrinkSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class drink_list(APIView):
    def get(self, request):
        drinks = Drink.objects.all()
        serializer = DrinkSerializer(drinks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class drink_id(APIView):
    def get_object(self, id):
        try:
            return Drink.objects.get(pk=id)
        except Drink.DoesNotExist:
            return None

    def get(self, request, id):
        drink = self.get_object(id)
        if drink is None:
            return Response(
                {"error": "Drink not found"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)

    def put(self, request, id):
        drink = self.get_object(id)
        if drink is None:
            return Response(
                {"error": "Drink not found"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        drink = self.get_object(id)
        if drink is None:
            return Response(
                {"error": "Drink not found"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = DrinkSerializer(drink, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        drink = self.get_object(id)
        if drink is None:
            return Response(
                {"error": "Drink not found"}, status=status.HTTP_404_NOT_FOUND
            )
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
