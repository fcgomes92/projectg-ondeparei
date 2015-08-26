__author__ = 'gomes'

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import FormView
from django.contrib import messages
from ondeparei.forms.form_product_detail import CreateProductDetailForm
from ondeparei.util.strings import PAGE_TITLE_BASE, DETAIL_CREATE_SUCCESS, USER_HOME, LOGIN_URL, DETAIL_CREATE_ERR
from ondeparei.models import Detail, UserModel


class CreateDetailProduct(FormView):
    http_method_names = ['get', 'post']
    form_class = CreateProductDetailForm
    template_name = 'ondeparei/detail_product/create_detail_product.html'
    success_url = USER_HOME

    def get_context_data(self, **kwargs):
        context = super(CreateDetailProduct, self).get_context_data(**kwargs)
        context['page_title'] = (PAGE_TITLE_BASE + ' - Create Detail')
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if request.POST.get('create_detail', None) is not None:
            user = UserModel.objects.get(user=request.user)
            label = request.POST.get('label', None)
            value = request.POST.get('value', '')
            form = self.form_class(request.POST)

            if None not in (user, label, value):
                detail = Detail(label=label, user=user, value=value)
                detail.save()
                messages.add_message(request=request, level=messages.SUCCESS, message=DETAIL_CREATE_SUCCESS)
                result = self.form_valid(form)
            else:
                messages.add_message(request=request, level=messages.ERROR, message=DETAIL_CREATE_ERR)
                result = self.form_invalid(form)
        else:
            messages.add_message(request=request, level=messages.ERROR, message=DETAIL_CREATE_ERR)
            result = self.form_invalid(form)
        return result

    @method_decorator(login_required(login_url=LOGIN_URL))
    def dispatch(self, *args, **kwargs):
        return super(CreateDetailProduct, self).dispatch(*args, **kwargs)
