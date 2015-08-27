__author__ = 'gomes'

from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from ondeparei.util.strings import PAGE_TITLE_BASE, LOGIN_URL
from ondeparei.models import Product, UserModel


class ListProductsView(TemplateView):
    template_name = 'ondeparei/product/list_product.html'
    http_method_names = ['get', ]

    def get_context_data(self, **kwargs):
        context = super(ListProductsView, self).get_context_data(**kwargs)
        context['page_title'] = (PAGE_TITLE_BASE + ' - List Products')
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        user = UserModel.objects.get(user=request.user)
        context['products'] = Product.objects.filter(user=user).order_by('-timestamp')
        return self.render_to_response(context=context)

    @method_decorator(login_required(login_url=LOGIN_URL))
    def dispatch(self, *args, **kwargs):
        return super(ListProductsView, self).dispatch(*args, **kwargs)
