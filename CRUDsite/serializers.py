from rest_framework import serializers
from models import db

class ElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = db.element
        fields = ('id', 'name', 'description', 'selector', 'page_id', 'component_id')

class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = db.component
        fields = ('id', 'name')

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = db.page
        fields = ('id', 'name', 'url')
