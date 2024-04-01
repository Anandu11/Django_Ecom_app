from rest_framework import serializers
from store.models import User


class Signup(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","password","email"]
        read_only_fields=['id']

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)    
    
class Login(serializers.ModelSerializer):
    username=serializers.CharField()
    password=serializers.CharField()    