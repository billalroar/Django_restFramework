from django.db import models
from rest_framework import fields, serializers
from ManyToManyR.models import Student,Modules

class ModulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modules
        fields = ['id','module_name','module_duration','class_room']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name','age','grade','modules']
        depth = 1