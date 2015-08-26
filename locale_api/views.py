from rest_framework import viewsets
from locale_api import models
from rest_framework import generics


class CountryViewSet(viewsets.ModelViewSet):
    queryset = models.Country.objects.all()
    serializer_class = models.CountrySerializer


class StateViewSet(viewsets.ModelViewSet):
    queryset = models.State.objects.all()
    serializer_class = models.StateSerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = models.City.objects.all()
    serializer_class = models.CitySerializer


class StatePerCountryView(generics.ListAPIView):
    serializer_class = models.StateSerializer

    def get_queryset(self):
        country_id = self.kwargs.get('countryid', None)
        if country_id is not None:
            return models.State.objects.filter(country__id=country_id)
        else:
            return []


class CityPerStateView(generics.ListAPIView):
    serializer_class = models.CitySerializer

    def get_queryset(self):
        state_id = self.kwargs.get('stateid', None)
        if state_id is not None:
            return models.City.objects.filter(state__id=state_id)
        else:
            return []
