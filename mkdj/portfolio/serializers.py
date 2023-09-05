from rest_framework import serializers
from .models import Portfolio, Category, Subcategory



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = '__all__'

class PortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'
