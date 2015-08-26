__author__ = 'gomes'

from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.views.generic import FormView
from django.contrib.auth import logout, login
from django.contrib import messages
from django.contrib.auth import authenticate
from ondeparei.forms.login.form_login import LoginForm
from ondeparei.util.strings import PAGE_TITLE_BASE, LOGIN_REALIZADO_COM_SUCESSO, USER_HOME, LOGIN_ERR, \
    EMAIL_ERR


class LoginRequestView(FormView):
    template_name = "ondeparei/login/login.html"
    success_url = USER_HOME
    form_class = LoginForm

    @staticmethod
    def validade_email_address(email):
        try:
            validate_email(email)
            return True
        except ValidationError:
            return False

    def get_context_data(self, **kwargs):
        context = super(LoginRequestView, self).get_context_data(**kwargs)
        context['page_title'] = (PAGE_TITLE_BASE + ' - Login')
        return context

    def post(self, request, *args, **kwargs):
        logout(request)
        form = self.form_class(request.POST)
        if request.POST.get('login', None) is not None:
            if form.is_valid():
                email = form.cleaned_data['email']
                if self.validade_email_address(email):
                    password = form.cleaned_data['password']
                    u = authenticate(username=email, password=password)
                    if u is not None:
                        login(request=request, user=u)
                        result = self.form_valid(form)
                        messages.add_message(request=request, level=messages.SUCCESS,
                                             message=LOGIN_REALIZADO_COM_SUCESSO)
                        return result
                    else:
                        messages.add_message(request=request, level=messages.ERROR,
                                             message=LOGIN_ERR)
                else:
                    messages.add_message(request=request, level=messages.ERROR,
                                             message=EMAIL_ERR)
            else:
                messages.add_message(request=request, level=messages.ERROR,
                                             message=LOGIN_ERR)
            result = self.form_invalid(form)
            return result
