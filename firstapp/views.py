from firstapp.models import CarSpecs,CarPlan
from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.sessions.models import Session
from rest_framework import serializers, viewsets
from .serializer import CarSpacsSerializer
# Session.objects.all().delete()
# Create your views here.

@api_view()
@permission_classes([AllowAny])
def firstFunction(request):
    print(request.query_params['id'])
    print(request.query_params['key'])
    return Response({'message':'we recive your request '})


class CarSpecsViewset(viewsets.ModelViewSet):
    serializer_class = CarSpacsSerializer

    def get_queryset(self):

        car_space = CarSpecs.objects.all()

        return car_space

    def retrieve(self, request, *args, **kwargs):

        params = kwargs
        print(params['pk'])
        print(request.query_params['id'])
        paramslist = params['pk'].split('-')
        cars = CarSpecs.objects.filter(car_brand= paramslist[0],car_model=paramslist[1] )
        serializer = CarSpacsSerializer(cars, many= True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        car_data = request.data
        print(request.data.get("production_year"))
        new_car = CarSpecs.objects.create(car_plan=CarPlan.objects.get(id =car_data["car_plan"]),car_brand = car_data["car_brand"],car_model= car_data["car_model"],
        production_year= car_data["production_year"],car_body= car_data["car_body"],engine_type= car_data["engine_type"])

        new_car.save()

        serializer = CarSpacsSerializer(new_car)

        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        car  = self.get_object()
        car.delete()
        return Response({'message': "Item has been deleted"})

    def update(self, request, *args, **kwargs):

        car_object = self.get_object()
        data = request.data

        car_plan = CarPlan.objects.get(plan_name= data["plan_name"])

        car_object.car_plan = car_plan
        car_object.car_brand = data['car_brand']
        car_object.car_model = data["car_model"]
        car_object.production_year = data["production_year"]
        car_object.car_body = data["carbody"]
        car_object.engine_type = data["engine_type"]

        car_object.save()
        serializer = CarSpacsSerializer(car_object)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        car_object = self.get_object()

        data = request.data

        try:
            car_plan = CarPlan.objects.get(plan_name= data["plan_name"])
            car_object.car_plan = car_plan
        except KeyError:
            pass


        car_object.car_brand = data.get('car_brand', car_object.car_brand)
        car_object.car_brand = data.get('car_model', car_object.car_model)
        car_object.car_brand = data.get('production_year', car_object.production_year)
        car_object.car_brand = data.get('car_body', car_object.car_body)
        car_object.car_brand = data.get('engine_type', car_object.engine_type)

        car_object.save()

        serializer = CarSpacsSerializer(car_object)
        return Response(serializer.data)