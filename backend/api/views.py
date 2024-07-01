import json
from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict

from products.models import Product


def api_home(request, *args, **kwargs):  
    model_data = Product.objects.all().order_by("?").first() 
    data = model_to_dict(model_data, fields=['id', 'title', 'price'])
    return JsonResponse(data)
    # print(data)
    # json_data_str = json.dumps(data)
    # return HttpResponse(json_data_str, headers={'application-type':'application/json' } )
