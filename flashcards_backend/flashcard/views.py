from ast import Is
from wsgiref.util import request_uri
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .serializers import CollectionSerializer
from .serializers import FlashcardSerializer
from .models import Collection
from .models import Flashcard
from django.contrib.auth.models import User
from .serializers import UserSerializer

# Create your views here.
#!all temporarily allow any

#collections
@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_collections(request):
    collections = Collection.objects.all()
    serializer = CollectionSerializer(collections, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([AllowAny])
def add_collection(request):
    serializer = CollectionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_collection(request, collection_id):
    collection = Collection.objects.get(id=collection_id)
    if request.user.id == collection.user.id:
        serializer = CollectionSerializer(collection, many=False) #will display deleted collection
        collection.delete()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['PUT'])
@permission_classes([AllowAny])
def update_collection(request, collection_id):
    collection = Collection.objects.get(id=collection_id)
    serializer = CollectionSerializer(collection, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#flashcards
@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_flashcards(request, collection_id):
    flashcards = Flashcard.objects.filter(collection_id=collection_id)
    serializer = FlashcardSerializer(flashcards, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([AllowAny])
def add_flashcard(request):
    serializer = FlashcardSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_flashcard(request, flashcard_id):
    flashcard = Flashcard.objects.get(id=flashcard_id)
    if request.user.id == flashcard.user.id:
        serializer = FlashcardSerializer(flashcard, many=False) #will display deleted flashcard
        flashcard.delete()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['PUT'])
@permission_classes([AllowAny])
def update_flashcard(request, flashcard_id):
    flashcard = Flashcard.objects.get(id=flashcard_id)
    serializer = FlashcardSerializer(flashcard, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)