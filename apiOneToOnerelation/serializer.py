
from rest_framework  import fields, serializers
from .models import Posts,PostsRates

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ['id','post_title',' post_body','rates']
        depth = 1 # for forigen key data show

class PostsRatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostsRates
        fields = ['id','likes',' dislike',]