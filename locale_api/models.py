from django.db import models
from rest_framework import serializers

# Base DB - http://www.iamrohit.in/countries-states-and-cities-database-of-world-in-mysql/

class Country(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False)
    code = models.CharField(max_length=3, null=False, blank=False)

    class Meta:
        db_table = 'countries'
        app_label = 'locale_api'
        verbose_name = 'locale_api'
        verbose_name_plural = 'countries'


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name', 'code')


class State(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False)
    country = models.ForeignKey(Country, null=False, blank=False)

    class Meta:
        db_table = 'states'
        app_label = 'locale_api'
        verbose_name = 'region'
        verbose_name_plural = 'regions'


class StateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = State
        fields = ('id', 'name', 'country')
        depth = 1


class City(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False)
    state = models.ForeignKey(State)

    class Meta:
        db_table = 'cities'
        app_label = 'locale_api'
        verbose_name = 'city'
        verbose_name_plural = 'cities'


class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name', 'state')
        depth = 2
