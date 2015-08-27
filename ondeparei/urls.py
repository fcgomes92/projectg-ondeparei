__author__ = 'gomes'

from django.conf.urls import url

from ondeparei.views.login.view_reset_password import ResetPasswordRequestView

from ondeparei.views.login.view_reset_confirm_password import PasswordResetConfirmView
from ondeparei.views.test import Test
from ondeparei.views.login.view_login import LoginRequestView
from ondeparei.views.login.view_logout import RequestLogout
from ondeparei.views.login.view_register import RegisterRequestView
from ondeparei.views.login.view_register_confirm import RegisterConfirmRequest
from ondeparei.views.user.view_user_home import UserHomeView
from ondeparei.views.product.view_create_product import CreateProductRequest
from ondeparei.views.product.view_list_product import ListProductsView
from ondeparei.views.detail_product.view_detail_product import CreateDetailRequest, ListDetailRequest

urlpatterns = [
    url('^$', Test.as_view(), name='teste'),

    # Login
    url(r'^login/$', LoginRequestView.as_view(), name='login'),
    url(r'^logout/$',RequestLogout.as_view(), name='logout'),
    url(r'^register/$', RegisterRequestView.as_view(), name='register'),
    url(r'^reset_password$', ResetPasswordRequestView.as_view(), name="reset_password"),
    url(r'^reset_password_confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', PasswordResetConfirmView.as_view(),
        name='reset_password_confirm'),
    url(r'^register_confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', RegisterConfirmRequest.as_view(),
        name='register_confirm'),

    # User part
    url(r'^home/$', UserHomeView.as_view(), name='user_home'),

    # Products
    url(r'^product/create/$', CreateProductRequest.as_view(), name='create_product'),
    url(r'^product/list/$', ListProductsView.as_view(), name='list_products'),
    # url(r'^product/list/(?P<pid>[0-9]+)/detail/$', .as_view(), name='detail'),

    # Detail
    url(r'^detail/create/$', CreateDetailRequest.as_view(), name='create_detail'),
    url(r'^detail/list/$', ListDetailRequest.as_view(), name='list_details'),
    # url(r'^detail/list/(?P<pid>[0-9]+)/detail/$', .as_view(), name='detail_detail'),
]
