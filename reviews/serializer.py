from rest_framework import serializers
from .models import Project,Profile,Rating

class ProjectSerializer(serializers.ModelSerializer):
    #create a meta class to define model
    class Meta:
        model = Project
        fields = ('name','owner','link','description','pub_date')
class ProfileSerializer(serializers.ModelSerializer):
    #create a meta class to define model
    class Meta:
        model = Profile
        fields = ('username','description','contact')
class RatingSerializer(serializers.ModelSerializer):
    #create a meta class to define model
    class Meta:
        model = Rating
        fields = ('design','usability','content','ratings','project', 'published_date')
