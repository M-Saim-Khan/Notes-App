from django.contrib.auth.models import User
from rest_framework import serializers #converts python object (user) into json data to be used as we use json for authentication(jws)
#convert json to python and viseversa
from.models import Note

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username","password"] #these are all the fields we wanna serialize when we are accepting a new user
        #and when we are returning a new user
        extra_kwargs = {"password" : {"write_only": True}} 
        #it tells django that we wanna accept password when we create a new user but we dont want to return the password when we are 
        #giving info about a user

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data) #create user
        return user #implements a method that is called when we create a new user. The serializer basically checks all the field in meta model
    #and then validate them and if they are validated, it will pass them to this function to create the user

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "author"]
        extra_kwargs = {"author":{"read_only":True}} #able to read who the author is but can't write who the author is