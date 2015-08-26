__author__ = 'gomes'

from django.views.generic import TemplateView
import requests
import json

class Test(TemplateView):
    http_method_names = ['get']
    template_name = 'ondeparei/teste.html'
    
    def get(self, request, *args, **kwargs):
        super(Test, self).get(request, *args, **kwargs)
        context = self.get_context_data()

        response = requests.get('http://127.0.0.1:8000/locale/country/?format=json').json()

        context['countries'] = response
        return self.render_to_response(context=context)
