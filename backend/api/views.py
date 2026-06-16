from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note

# Create your views here.

class CreateUserView(generics.CreateAPIView): #generic builtin view of django that will automatically handle creating a new user/obj for us
    queryset = User.objects.all() # specift that here is the list of all the diff objects that we are gonna be looking at when we creating
    #a new one to make sure we dont accidentally create a user that alr exists
    serializer_class = UserSerializer #what kind of data we need to accept to make a new user
    permission_classes = [AllowAny] #specify who can actually call this view to create a new user

class NoteListCreate(generics.ListCreateAPIView): #we use list create so that it either lists all user notes or creates a note
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated] #this means that only the user that returns a valid jwt token will have access

    def get_queryset(self):
        user = self.request.user #in django, this gives us the user object
        return Note.objects.filter(author = user) #filters using the user aka author we could do .all instead of filter which will give all notes
    
    def perform_create(self, serializer): #when we pass the serializer class (NoteSerializer) different data it will tell us if it is valid or not
        #normally serializer checks using all the variables in it's class but we are checking manually here and here we are manually adding author
        #as it was made to be view only before
        if serializer.is_valid():
            serializer.save(author = self.request.user)
        else:
            print(serializer.errors)

class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author = user)
    