__author__ = 'gomes'

from django.contrib.auth.tokens import default_token_generator
from django.http.response import HttpResponseRedirect
from django.template import loader
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.views.generic import FormView
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib import messages
from ondeparei.forms.login.form_register import RegisterRequestForm
from ondeparei.models import UserModel
from ondeparei.util.strings import LOGIN_URL, PAGE_TITLE_BASE
from config.config_email import *
from django.core.mail import send_mail


class RegisterRequestView(FormView):
    template_name = 'ondeparei/login/register.html'
    form_class = RegisterRequestForm
    success_url = LOGIN_URL

    @staticmethod
    def validate_email_address(email):
        try:
            validate_email(email)
            return True
        except ValidationError:
            return False

    def get(self, request, *args, **kwargs):
        return super(RegisterRequestView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if request.POST.get('register', None) is not None:
            if form.is_valid():
                email = form.cleaned_data['email']
                if self.validate_email_address(email):
                    u = User.objects.filter(email=email)
                    if u.exists():
                        result = self.form_invalid(form)
                        messages.error(request, 'Registered email! Try to reset your password!')
                        return result
                    else:

                        u = User.objects.create_user(username=email, email=email,
                                                     password=form.cleaned_data['password'],
                                                     first_name=form.cleaned_data['first_name'],
                                                     last_name=form.cleaned_data['last_name'],
                                                     )
                        u.is_active = False
                        u.save()

                        UserModel.objects.create(user=u, bday=form.cleaned_data['bday'], ).save()

                        c = {
                            'email': u.email,
                            'domain': request.META['HTTP_HOST'],
                            'site_name': 'your site',
                            'uid': urlsafe_base64_encode(force_bytes(u.pk)),
                            'user': u,
                            'token': default_token_generator.make_token(u),
                            'protocol': 'http',
                        }
                        subject = 'Register on OndeParei'
                        subject = ''.join(subject.splitlines())
                        email = loader.render_to_string('ondeparei/login/register_confirm.html', c)
                        send_mail(subject, email, DEFAULT_FROM_EMAIL, [u.email, ], fail_silently=False)
                        messages.add_message(request, messages.SUCCESS, 'Done! Now check your email, please ;D')
                        return HttpResponseRedirect('/ondeparei/login/', )
                else:
                    result = self.form_invalid(form)
                    messages.error(request, 'Invalid email!')
                    return result

    def get_context_data(self, **kwargs):
        context = super(RegisterRequestView, self).get_context_data(**kwargs)
        context['page_title'] = (PAGE_TITLE_BASE + ' - Register')
        return context
