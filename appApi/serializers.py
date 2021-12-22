from rest_framework import serializers
from djoser.serializers import UserCreateSerializer, UserSerializer
from .models import *

class UserCreationSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = '__all__'


# class ProjectContractorSerializer(serializers.Serializer):
#     class Meta:
#         model = ProjectContractor
#         fields = '__all__'


# Without model serializer method
# class ProjectContractorSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=200)
#     created_on = serializers.DateTimeField()

#     def create(self, validated_data):
#         return ProjectContractor.objects.create(validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.created_on = validated_data.get('created_on', instance.created_on)
#         instance.save()
#         return instance

class ProjectContractorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectContractor
        fields = ['id', 'name']
        # fields = '__all__'


class ProjectStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectStage
        fields = ['id', 'name']
        # fields = '__all__'

class ProjectstgMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectStagesMapping
        # fields = ['id', 'site_name','phase_id','stage_id','sensor_count','start_date','end_date']
        fields = '__all__'

class ProjectAssignSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectAssigningDetails
        fields = '__all__'