__author__ = 'gomes'

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.views.generic import View
from ondeparei.util.strings import LOGIN_URL


class RequestLogout(View):
    http_method_names = ['get']

    def get(self, request, *arks, **kargs):
        logout(request=request)
        return HttpResponseRedirect(LOGIN_URL)

    @method_decorator(login_required(login_url=LOGIN_URL))
    def dispatch(self, *args, **kwargs):
        return super(RequestLogout, self).dispatch(*args, **kwargs)
