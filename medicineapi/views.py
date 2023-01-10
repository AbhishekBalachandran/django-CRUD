from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK 
)
from rest_framework.response import Response
from django.contrib.auth import authenticate, logout
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer, MedicineSerializer
from medicine.models import Medicine
from rest_framework import filters, generics
# Create your views here.

class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},status=HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def logout(request):

    request.user.auth_token.delete()
    return Response('User Logged out successfully')

class CreateMedicine(generics.CreateAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    permission_classes = [IsAuthenticated,]

class ReadMedicine(generics.ListAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    permission_classes = [IsAuthenticated,]

class UpdateMedicine(generics.RetrieveUpdateAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    permission_classes = [IsAuthenticated,]

class DeleteMedicine(generics.DestroyAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    permission_classes = [IsAuthenticated,]


class MedicineSearch(generics.ListCreateAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ['product_name','name_of_manufacturer','price']
    permission_classes = [IsAuthenticated,]

