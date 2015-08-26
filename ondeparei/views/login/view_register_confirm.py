__author__ = 'gomes'

from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.utils.http import urlsafe_base64_decode
from django.views.generic import View
from django.contrib import messages
from ondeparei.util.strings import LOGIN_URL

class RegisterConfirmRequest(View):
    http_method_names = ['get']

    def get(self, request, uidb64=None, token=None, *arg, **kwargs):
        assert uidb64 is not None and token is not None
        user_model = get_user_model()
        try:
            uid = urlsafe_base64_decode(uidb64)
            user = user_model._default_manager.get(pk=uid)
        except (TypeError, ValueError, OverflowError, user_model.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            messages.add_message(request, messages.SUCCESS, 'Thanks! Now you can login!')
            return HttpResponseRedirect(LOGIN_URL)
