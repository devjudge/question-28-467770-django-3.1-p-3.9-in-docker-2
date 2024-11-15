import os
import json
import shutil
from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_exempt # Ismail: to allow POST request, if not it will be forbidden
from django.http import StreamingHttpResponse, JsonResponse


from . import views

# from .utils import script as aa_script

def add_numbers(request):
    data = json.loads(request.body)
    # print('data: ', data)
    total = data['number1'] + data['number2']
    # print(total)
    return JsonResponse({'sum': total})

urlpatterns = [
    path('api/add', csrf_exempt(add_numbers), name='api/add'),
]