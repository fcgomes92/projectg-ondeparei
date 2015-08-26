__author__ = 'gomes'

from django.conf.urls import url, include
from rest_framework import routers
from locale_api import views

router = routers.DefaultRouter()
router.register(r'country',  views.CountryViewSet)
router.register(r'state',  views.StateViewSet)
router.register(r'city',  views.CityViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('^statepercountry/(?P<countryid>.+)/$', views.StatePerCountryView.as_view(), name='state_per_country'),
    url('^cityperstate/(?P<stateid>.+)/$', views.CityPerStateView.as_view(), name='city_per_state'),
]