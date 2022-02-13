from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from newsapp.models import News


class NewsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
