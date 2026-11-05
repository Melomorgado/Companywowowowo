from django.shortcuts import render
from rest_framework.views import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Manager
from .serializers import  ManagerSerializer
# Create your views here.
class ManagerView(APIView):
    def get(self, request):
        manager = Manager.objects.all()
        serializer = ManagerSerializer(manager, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ManagerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            data = serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )