from rest_framework import serializers
from blog.models import Country


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = ('country', 'capital', 'region')
