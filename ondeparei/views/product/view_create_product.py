__author__ = 'gomes'

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import FormView
from django.contrib import messages
from ondeparei.forms.product.form_product import CreateProductRequestForm
from ondeparei.models import UserModel, Product, Detail
from ondeparei.util.strings import LOGIN_URL, PAGE_TITLE_BASE, PRODUCT_CREATE_ERR, PRODUCT_CREATE_SUCCESS, USER_HOME


class CreateProductRequest(FormView):
    http_method_names = ['post', 'get']
    template_name = 'ondeparei/product/create_product.html'
    success_url = USER_HOME
    form_class = CreateProductRequestForm

    def get_context_data(self, **kwargs):
        context = super(CreateProductRequest, self).get_context_data(**kwargs)
        context['page_title'] = (PAGE_TITLE_BASE + ' - Create Product')
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if request.POST.get('create_product', None) is not None:
            user = UserModel.objects.get(user=request.user)
            name = request.POST.get('name', None)
            detail = request.POST.get('detail', None)
            form = self.form_class(request.POST)

            if None not in (user, detail, name):
                detail = Detail.objects.get(id=detail)
                product = Product(name=name, user=user)
                product.save()
                product.detail.add(detail)
                messages.add_message(request=request, level=messages.SUCCESS, message=PRODUCT_CREATE_SUCCESS)
                result = self.form_valid(form)
            else:
                messages.add_message(request=request, level=messages.ERROR, message=PRODUCT_CREATE_ERR)
                result = self.form_invalid(form)
        else:
            messages.add_message(request=request, level=messages.ERROR, message=PRODUCT_CREATE_ERR)
            result = self.form_invalid(form)
        return result

    @method_decorator(login_required(login_url=LOGIN_URL))
    def dispatch(self, *args, **kwargs):
        return super(CreateProductRequest, self).dispatch(*args, **kwargs)
