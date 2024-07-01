In views.py file

from django.http import JsonResponse
import json


def api_home(request, *args, **kwargs):
    body = request.body
    data = {}
    try:
        data = json.loads(body)  # string of JSon data --> Python Dict
    except:
        pass
    print(data)

    data['headers'] = request.headers
    data['content_type'] = request.content_type

    return JsonResponse({"message": "Hi there, this is your Djngo APi response!!"})

In basic.py file:

import requests


#endpoint = "https://httpbin.org/status/200"
endpoint = "http://127.0.0.1:8000/api/"

get_response = requests.get(endpoint,params={'abc': 123}, json={"Query": "Hello La"}) # Http Request
#print(get_response.text)
#print(get_response.status_code)
print(get_response.json()['message'])




from django.http import JsonResponse
import json


def api_home(request, *args, **kwargs):
    body = request.body
    data = {}
    try:
        data = json.loads(body)  # string of JSon data --> Python Dict
    except:
        pass
    print(data)

    #data['headers'] = request.headers
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    
    return JsonResponse(data)

    o/p:
    
{'Query': 'Hello La'}
[01/Jul/2024 20:52:18] "GET /api/?abc=123 HTTP/1.1"
 200 277


Query Parameters:

parms = {'abc': 123}
in endpoint : endpoint = "http://127.0.0.1:8000/api/?this_arg=this_value"

this is query parameters: ?this_arg=this_value

in this case : endpoint = "http://127.0.0.1:8000/api/?abc=123"



def api_home(request, *args, **kwargs):

    print(request.GET)
    print(request.POST)


    body = request.body
    data = {}
    try:
        data = json.loads(body)  # string of JSon data --> Python Dict
    except:
        pass
    print(data)

    #data['headers'] = request.headers
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type

o/p: is 
print(request.GET)
    print(request.POST)

o/p:
<QueryDict: {'abc': ['123']}>
<QueryDict: {}>
{'Query': 'Hello La'}
[01/Jul/2024 20:56:39] "GET /api/?abc=12
3 HTTP/1.1" 200 277


from django.http import JsonResponse
import json


def api_home(request, *args, **kwargs):

    print(request.GET)
    print(request.POST)
    body = request.body
    data = {}
    try:
        data = json.loads(body)  # string of JSon data --> Python Dict
    except:
        pass
    print(data)

    #data['headers'] = request.headers
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
     
    
    return JsonResponse(data)

<QueryDict: {}>
<QueryDict: {}>
{'Query': 'Hello La'}
[01/Jul/2024 21:13:45] "GET /api/ HTTP/1
.1" 200 291

import requests


#endpoint = "https://httpbin.org/status/200"
endpoint = "http://127.0.0.1:8000/api/"

get_response = requests.get(endpoint, json={"Query": "Hello La"}) # Http Request
#print(get_response.text)
#print(get_response.status_code)
#print(get_response.json()['message'])
print(get_response.json())


(venv) PS F:\pythonProject\drf-course\py_client> python .\basic.py        
  {'Query': 'Hello La', 'params': {}, 'headers': {'Content-Length': '21', 
'Content-Type': 'application/json', 'Host': '127.0.0.1:8000', 'User-Agent': 'python-requests/2.32.3', 'Accept-Encoding': 'gzip, deflate', 'Accept': 
'*/*', 'Connection': 'keep-alive'}, 'content_type': 'application/json'}   
(venv) PS F:\pythonProject\drf-course\py_client> 


In Products app:

>>> from products.models import Product
>>> Product.objects.create(title='Hello world', content='this is amazing!', price=0.00)
<Product: Product object (1)>
>>> Product.objects.create(title='Hello world 1', content='this is amazing!', price=0.00) 
<Product: Product object (2)>
>>> products.objects.all()
<QuerySet [<Product: Product object (1)>, <Product: Product object (2)>]>
>>> Product.objects.all().order_by("?").first()
<Product: Product object (1)>
>>> Product.objects.all().order_by("?").first()
<Product: Product object (1)>
>>> Product.objects.all().order_by("?").first()
<Product: Product object (2)>
>>> Product.objects.all().order_by("?").first()
<Product: Product object (2)>
>>> Product.objects.all().order_by("?").first()
<Product: Product object (1)>
>>> Product.objects.all().order_by("?").first()
<Product: Product object (2)>
>>> Product.objects.create(title='Hello world 1', content='this is amazing!', price=12.00)  
<Product: Product object (3)>
>>> Product.objects.all().order_by("?").first()
<Product: Product object (1)>
>>> Product.objects.all().order_by("?").first()
<Product: Product object (1)>
>>> Product.objects.all().order_by("?").first()
<Product: Product object (3)>

In api.views.py file:

import requests


#endpoint = "https://httpbin.org/status/200"
endpoint = "http://127.0.0.1:8000/api/"

get_response = requests.get(endpoint, json={"Query": "Hello La"}) # Http Request
#print(get_response.text)
#print(get_response.status_code)
#print(get_response.json()['message'])
print(get_response.json())



In products.views.py file:

from django.http import JsonResponse
import json
from products.models import Product


def api_home(request, *args, **kwargs):  
    model_data = Product.objects.all().order_by("?").first() 
    data = {}
    if model_data:
        data['title'] = model_data.title
        data['content'] = model_data.content
        data['price'] = model_data.price

    return JsonResponse(data)

(venv) PS F:\pythonProject\drf-course\backend>python manage.py runserver 8000


(venv) PS F:\pythonProject\drf-course\py_client> python .\basic.py    itle': 'Hello
{'title': 'Hello world', 'content': 'this is amazing!', 'price': '0.00'}                                                                    itle': 'Hello
(venv) PS F:\pythonProject\drf-course\py_client> python .\basic.py    
{'title': 'Hello world', 'content': 'this is amazing!', 'price': '0.00'}
(venv) PS F:\pythonProject\drf-course\py_client> python .\basic.py    
{'title': 'Hello world 1', 'content': 'this is amazing!', 'price': '0.00'}
(venv) PS F:\pythonProject\drf-course\py_client> python .\basic.py    
{'title': 'Hello world 1', 'content': 'this is amazing!', 'price': '12.00'}
(venv) PS F:\pythonProject\drf-course\py_client> 

random data we are gettings:

add id:

def api_home(request, *args, **kwargs):  
    model_data = Product.objects.all().order_by("?").first() 
    data = {}
    if model_data:
        data['id'] = model_data.id
        data['title'] = model_data.title
        data['content'] = model_data.content
        data['price'] = model_data.price

    return JsonResponse(data)


Insted of above we are using model_to_dict:

import json
from django.http import JsonResponse
from django.forms.models import model_to_dict

from products.models import Product


def api_home(request, *args, **kwargs):  
    model_data = Product.objects.all().order_by("?").first() 
    data = model_to_dict(model_data)

    return JsonResponse(data)

se\py_client> python .\basic.py    
{'id': 3, 'title': 'Hello world 1', 'content': 'this is amazing!', 'price': '12.00'}

 data = model_to_dict(model_data, fields=['id', 'title'])

se\py_client> python .\basic.py    
{'id': 2, 'title': 'Hello world 1'}

Instead of JsonResponse and HtttpResponse

def api_home(request, *args, **kwargs):  
    model_data = Product.objects.all().order_by("?").first() 
    data = model_to_dict(model_data, fields=['id', 'title'])
    
    return HttpResponse(data)

in basic.py file

import requests


#endpoint = "https://httpbin.org/status/200"
endpoint = "http://127.0.0.1:8000/api/"

get_response = requests.get(endpoint, json={"Query": "Hello La"}) # Http Request

print(get_response.headers)
print(get_response.text) # print raw text response

o/p:
se\py_client> python .\basic.py    
{'Date': 'Mon, 01 Jul 2024 18:17:19 GMT', 'Server': 'WSGIServer/0.2 CPython/3.10.1', 'Content-Type': 'text/html; charset=utf-8', 'X-Frame-Options': 'DENY', 'Content-Length': '7', 'X-Content-Type-Options': 'nosniff', 'Referrer-Policy': 'same-origin', 'Cross-Origin-Opener-Policy': 
'same-origin'}
idtitle

'Content-Type': 'text/html;

If we want to change the content-type to Json format

def api_home(request, *args, **kwargs):  
    model_data = Product.objects.all().order_by("?").first() 
    data = model_to_dict(model_data, fields=['id', 'title'])
    
    return HttpResponse(data, headers={'application-type':'application/json' } )

O/P;

{'Date': 'Mon, 01 Jul 2024 18:20:26 GMT', 'Server': 'WSGIServer/0.2 CPython/3.10.1', 'application-type': 
'application/json', 'Content-Type': 'text/html; charset=utf-8', 'X-Frame-Options': 'DENY', 'Content-Length': '7', 'X-Content-Type-Options': 
'nosniff', 'Referrer-Policy': 'same-origin', 'Cross-Origin-Opener-Policy': 'same-origin'}
idtitle

'application-type': 
'application/json'

2case:

1.case:


def api_home(request, *args, **kwargs):  
    model_data = Product.objects.all().order_by("?").first() 
    data = model_to_dict(model_data, fields=['id', 'title'])
    json_data_str = json.dumps(data)
    return HttpResponse(json_data_str, headers={'application-type':'application/json' } )

o/p:

{'Date': 'Mon, 01 Jul 2024 18:27:23 GMT', 'Server': 'WSGIServer/0.2 CPython/3.10.1', 'application-type': 
'application/json', 'Content-Type': 'text/html; charset=utf-8', 'X-Frame-Options': 'DENY', 'Content-Length': '35', 'X-Content-Type-Options': 'nosniff', 'Referrer-Policy': 'same-origin', 'Cross-Origin-Opener-Policy': 'same-origin'}
{"id": 3, "title": "Hello world 1"}


if add price in fields it is decimal point so got error:

def api_home(request, *args, **kwargs):  
    model_data = Product.objects.all().order_by("?").first() 
    data = model_to_dict(model_data, fields=['id', 'title', 'pricee'])
    json_data_str = json.dumps(data)
    return HttpResponse(json_data_str, headers={'application-type':'application/json' } )


i got error in backend:

  File "C:\Users\hp\AppData\Local\Programs\Python\Python310\lib\json\encoder.py", line 179, in default
    raise TypeError(f'Object of type {o.__class__.__name__} '
TypeError: Object of type Decimal is not JSON serializable
[01/Jul/2024 23:58:40] "GET /api/ HTTP
/1.1" 500 80577

so then 


print out data:

def api_home(request, *args, **kwargs):  
    model_data = Product.objects.all().order_by("?").first() 
    data = model_to_dict(model_data, fields=['id', 'title', 'price'])
    print(data)
    json_data_str = json.dumps(data)
    return HttpResponse(json_data_str, headers={'application-type':'application/json' } )


Quit the server with CTRL-BREAK.
{'id': 2, 'title': 'Hello world 1', 'price': 
Decimal('0.00')}

    return _iterencode(o, 0)
  File "C:\Users\hp\AppData\Local\Programs\Python\Python310\lib\json\encoder.py", line 179, in default
    raise TypeError(f'Object of type {o.__class__.__name__} '
TypeError: Object of type Decimal is not JSON serializable
[02/Jul/2024 00:00:07] "GET /api/ HTTP
/1.1" 500 80585


