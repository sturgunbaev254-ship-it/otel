from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Hotels, Numbers, Booking, Reviews
from .serializers import   RegisterSerializer, LoginSerializer,HotelSerializer, NumberSerializer, BookingSerializer, ReviewSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import  SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser

@api_view(['POST'])
def registor(request):

     serializer=RegisterSerializer(
          data=request.data
     )
     if serializer.is_valid():
        user=serializer.save()

        return Response(
            {
                "Answer":"Successfull",
                "username":user.username
            },
            status=status.HTTP_201_CREATED
        )
     return Response(
         serializer.errors,
         status=status.HTTP_400_BAD_REQUEST
     )

@api_view(['POST'])
def logout(request):
    if request.user.is_authenticated:
        Token.objects.filter(
            user=request.user
        ).delete()
        return Response({"message":"Logout succesful"})
    return Response({"massage":"не был авторизован"})        

@api_view(['POST'])
def login(request):

    serializer=LoginSerializer(
        data=request.data
    )
    if serializer.is_valid():
        user=serializer.validated_data["user"]

        token,creeated=Token.objects.get_or_create(
            user=user
        )
        return Response({
            "massages":"login successful",
            "token":token.key
        })
    return Response(
        serializer.errors,
        status=400
    )

class HotelsViewSet(viewsets.ModelViewSet):
    queryset=Hotels.objects.all()
    serializer_class=HotelSerializer

class NumbersViewSet(viewsets.ModelViewSet):
    queryset=Numbers.objects.all()
    serializer_class=NumberSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset=Booking.objects.all()
    serializer_class=BookingSerializer
    permission_classes=[IsAuthenticated]

class ReviewsViewSet(viewsets.ModelViewSet):
    queryset=Reviews.objects.all()
    serializer_class=ReviewSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]