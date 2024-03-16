from rest_framework import serializers

from watchlist_app.models import Reviews, StreamPlatform, WatchList

class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Reviews
        fields = "__all__"

class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many = True, read_only = True)
    class Meta:
        model = WatchList
        fields = "__all__"
        
class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True )
    
    class Meta:
        model = StreamPlatform
        fields = "__all__"
        
        
    # # use object (or any other variable name you choose) to refer to the 
    # # instance of the object being serialized within serializer methods. 
    # # Use self to refer to the serializer instance itself.
    # def get_len_name(self, object):
    #     return len(object.name)
        
        
    # # Validation on object [Object Validation]
    # def validate(self, data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError("Name and Description should be different")
    #     return data
    
    # # Validation on the field [Field validation]
    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short!!")
    #     return value

# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name is too short!!")
#     return value
    
    
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only = True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
#     # ** is unpacking operator, used to unpack the key-value pairs
#     #  and pass them as keyword arguments
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
    
#     # Validation on object [Object Validation]
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Name and Description should be different")
#         return data
    
#     # # Validation on the field [Field validation]
#     # def validate_name(self, value):
#     #     if len(value) < 2:
#     #         raise serializers.ValidationError("Name is too short!!")
#     #     return value