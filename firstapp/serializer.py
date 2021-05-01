from rest_framework  import fields, serializers
from firstapp.models import CarSpecs

class CarSpacsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarSpecs
        fields = ['id','car_plan','car_brand','car_model','production_year','car_body','engine_type']
        depth = 1 # for forigen key data show