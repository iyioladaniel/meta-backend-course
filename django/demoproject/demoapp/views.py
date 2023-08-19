from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    path = request.path
    method = request.method
    content = '''
    <center><h2>Testing Django Request Response Objects</h2>
    <p>Request path: "{}"</p>
    <p>Request Method: {}</p><center>
    '''.format(path,method)
    return HttpResponse(content)

def home(request):
    path = request.path
    scheme = request.scheme
    method = request.method
    address = request.META['REMOTE_ADDR']
    user_agent = request.META['HTTP_USER_AGENT']
    path_info = request.path_info

    response = HttpResponse()
    response.headers['Age'] = 20

    msg = f'''<br>
    <br>Path: {path}
    <br>Address: {address}
    <br>Scheme: {scheme}
    <br>Method: {method}
    <br>User agent: {user_agent}
    <br>Path info: {path_info}
    <br>Request headers: {response.headers}    
    '''

    response = HttpResponse(msg, content_type='text/html', charset='utf-8') #HttpResponse('This works!')
    return response #HttpResponse(path, content_type='text/html', charset='utf-8')