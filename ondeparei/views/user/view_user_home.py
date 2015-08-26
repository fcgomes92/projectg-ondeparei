__author__ = 'gomes'

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.contrib import messages
from ondeparei.util.strings import PAGE_TITLE_BASE, LOGIN_URL


class UserHomeView(TemplateView):
    http_method_names = ['get']
    template_name = 'ondeparei/user/user_home.html'

    def get_context_data(self, **kwargs):
        context = super(UserHomeView, self).get_context_data(**kwargs)
        context['page_title'] = (PAGE_TITLE_BASE + ' - User Home')
        return context

    @method_decorator(login_required(login_url=LOGIN_URL))
    def dispatch(self, *args, **kwargs):
        return super(UserHomeView, self).dispatch(*args, **kwargs)