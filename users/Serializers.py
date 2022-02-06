
from rest_framework import serializers
from .models import Resume, User


class ResumeSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = '__all__'


class UserSerilizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'resume', 'email', 'password']
        depth = 1

class UpdateUserSerializer(serializers.ModelSerializer):
    resume = serializers.FileField()
    class Meta:
        model = User
        fields = ['name','resume','email','password']

    def update(self, validated_data):
        name = validated_data.get('name')
        email = validated_data.get('email')
        resume = validated_data.get('resume')
        print(resume)
        # password = validated_data.get('password')
        # if password1 == password2:
        #     user = User(name=name, email=email, resume=resume)
        #     user.set_password(password1)
        #     user.save()
        #     return user
        # else:
        #     raise serializers.ValidationError({
        #         'error': 'Passwords do not Match'
        #     })

class RegisterUserSerializer(serializers.ModelSerializer):
    resume = serializers.FileField()
    password1 = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = ['name', 'email', 'resume', 'password1', 'password2']
        extra_kwargs = {
            'password1': {'write_only': True},
            'password2': {'write_only': True},
        }

    def create(self, validated_data):
        name = validated_data.get('name')
        email = validated_data.get('email')
        resume = validated_data.get('resume')
        password1 = validated_data.get('password1')
        password2 = validated_data.get('password2')
        resume = Resume(text=resume.name,resume=resume)
        if password1 == password2:
            resume.save()
            user = User(name=name, email=email, resume=resume)
            user.set_password(password1)
            user.save()
            return user
        else:
            raise serializers.ValidationError({
                'error': 'Passwords do not Match'
            })
