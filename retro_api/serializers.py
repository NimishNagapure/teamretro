from datetime import datetime
from django.db.models import fields
from django.db.models.base import Model
from django.db.models.query import QuerySet
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import  RetroUser
from django.contrib.auth.password_validation import validate_password



class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required = True,
            validators=[UniqueValidator(queryset = RetroUser.objects.all())]
    )

    password = serializers.CharField(write_only= True ,required = True, validators =[validate_password])
    modified_on = serializers.DateTimeField(source = 'modified_datetime',required=False)
    created_on = serializers.DateTimeField(source = 'created_datetime',required=False)
    
    class Meta:
        model = RetroUser
        fields = ('username' ,'password' ,'email','first_name','last_name','created_on','profile_pic','retro_user_role_id','login_provider_id','modified_on')
        extra_kwargs = {
            'first_name':{'required':True},
            'last_name':{'required' : True},
            'login_provider_id':{'required':False},
            'retro_user_role_id':{'required':False},
            'profile_pic':{'required' :False}
        }

    def create(self,validate_data):
        if validate_data['profile_pic']:
            image =validate_data['profile_pic']
        else :
            image = None
        user = RetroUser.objects.create(
            username = validate_data['username'],
            email = validate_data['email'],
            first_name = validate_data['first_name'],
            last_name= validate_data['last_name'],
            login_provider_id = validate_data['login_provider_id'],
            retro_user_role_id = validate_data['retro_user_role_id'],
            profile_pic = image

        )

        user.set_password(validate_data['password'])
        user.save()

        return user
