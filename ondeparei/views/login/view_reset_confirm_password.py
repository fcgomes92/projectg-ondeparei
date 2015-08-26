__author__ = 'gomes'

from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.views.generic import *
from django.contrib import messages
from django.contrib.auth import get_user_model

from ondeparei.forms.login.form_set_new_password import SetPasswordForm
from ondeparei.util.strings import LOGIN_URL, PAGE_TITLE_BASE


# Ref: http://ruddra.com/blog/2014/10/21/make-own-forgot-slash-reset-password-in-django/
class PasswordResetConfirmView(FormView):
    template_name = "ondeparei/login/password_reset_confirm.html"
    success_url = LOGIN_URL
    form_class = SetPasswordForm

    def get_context_data(self, **kwargs):
        context = super(PasswordResetConfirmView, self).get_context_data(**kwargs)
        context['page_title'] = (PAGE_TITLE_BASE + ' - Register my new password')
        return context

    def post(self, request, uidb64=None, token=None, *arg, **kwargs):
        """
        View that checks the hash in a password reset link and presents a
        form for entering a new password.
        """
        user_model = get_user_model()
        form = self.form_class(request.POST)
        assert uidb64 is not None and token is not None
        try:
            uid = urlsafe_base64_decode(uidb64)
            user = user_model._default_manager.get(pk=uid)
        except (TypeError, ValueError, OverflowError, user_model.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            if form.is_valid():
                new_password = form.cleaned_data['new_password2']
                user.set_password(new_password)
                user.save()
                messages.success(request, 'Password has been reset.')
                return self.form_valid(form)
            else:
                messages.error(request, 'Password reset has not been unsuccessful.')
                return self.form_invalid(form)
        else:
            messages.error(request, 'The reset password link is no longer valid.')
            return self.form_invalid(form)
