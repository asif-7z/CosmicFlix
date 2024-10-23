from upload_video.models import video,Series_Name
from rest_framework.serializers import ModelSerializer,HyperlinkedIdentityField



class videoSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(view_name='videoDetails:detail',lookup_field='slug')
    class Meta:
        model = video
        fields = [
            'user',
            'title',
            'slug',
            'url',

        ]

class VideoDetailSerializer(ModelSerializer):
    class Meta:
        model = video
        fields = [
            'user',
            'title',
            'series',
            'slug',
            'file',
            'image',
            'content'

        ]

class seriesNameSerializer(ModelSerializer):
    class Meta:
        model = Series_Name
        fields = [
                    'Name', 
                    'poster',
                    'genre',
                    'type', 
                    'detail', 
                    'time_stamp',

        ]
     
class VideoCreateSerializer(ModelSerializer):
    SeriesNameFields = seriesNameSerializer()
    class Meta:
        model = video
        fields = '__all__'