from car.models import Cars
from rest_framework  import fields, serializers

class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = ['id','car_brand','car_model','production_year','car_body','engine_type']
        #depth = 1 # for forigen key data show