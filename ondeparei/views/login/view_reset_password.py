__author__ = 'gomes'

from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template import loader
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.views.generic import *
from django.contrib import messages
from django.contrib.auth.models import User

from config.config_email import DEFAULT_FROM_EMAIL
from ondeparei.forms.login.form_reset_password import PasswordResetRequestForm
from ondeparei.util.strings import LOGIN_URL, PAGE_TITLE_BASE


class ResetPasswordRequestView(FormView):
    template_name = "ondeparei/login/password_reset.html"
    success_url = LOGIN_URL
    form_class = PasswordResetRequestForm

    @staticmethod
    def validate_email_address(email):
        try:
            validate_email(email)
            return True
        except ValidationError:
            return False

    def get_context_data(self, **kwargs):
        context = super(ResetPasswordRequestView, self).get_context_data(**kwargs)
        context['page_title'] = (PAGE_TITLE_BASE + ' - Register my password!')
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data["email"]
        else:
            data = False
        if self.validate_email_address(data) is True:
            associated_users = User.objects.filter(email=data)
            if associated_users.exists():
                for user in associated_users:
                    c = {
                        'email': user.email,
                        'domain': request.META['HTTP_HOST'],
                        'site_name': 'your site',
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'user': user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    subject = 'Password reset from CBSCA'
                    subject = ''.join(subject.splitlines())
                    email = loader.render_to_string('ondeparei/login/password_reset_email.html', c)
                    send_mail(subject, email, DEFAULT_FROM_EMAIL, [user.email], fail_silently=False)
                result = self.form_valid(form)
                messages.success(request,
                                 'An email has been sent to ' + data + ". Please check its inbox to continue reseting password.")
                return result
            result = self.form_invalid(form)
            messages.error(request, 'No user is associated with this email address')
            return result
        messages.error(request, 'Invalid Input')
        return self.form_invalid(form)
