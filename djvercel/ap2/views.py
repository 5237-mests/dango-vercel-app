# from django.shortcuts import render

# # Create your views here.
# # appname/views.py
# from django.shortcuts import render

# def my_view(request):
#     context = {
#         'page_title': 'My Page',
#         'user_name': 'Mesfin',
#     }

#     return render(request, '/templates/index.html', context)

from django.http import HttpResponse
from django.template import loader

def my_view(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())
