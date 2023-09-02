from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect, HttpResponseNotFound, Http404
#from .models import Product
from django.urls import reverse
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

def pathview(request, name, id):
    return HttpResponse("Name: {}\n\nUserID: {}".format(name, id))

def queryview(request):
    name = request.GET['name']
    id = request.GET['id']
    return HttpResponse('Name: {} UserID: {}'.format(name,id))

def showform(request):
    return render(request, "form.html")

def getform(request):
    id = None
    name = None
    
    if request.method == "POST":
        id = request.POST['id']
        name = request.POST['name']
        age = request.POST['age']

        #print(request.POST['id'], request.POST['name'])
    return HttpResponse('Name: {} Age: {} UserID: {}'.format(name, age, id))

def menuitems(request, dish):
    items = {
        'pasta':'Pasta is a type of noodle made from the combination of wheat, water or eggs',
        'falafel' : 'Falafel are deep fried patties or balls made from ',
        'cheesecake' : 'Cheesecake is a type of dessert made with cream, soft cheese on top of cookie, pastry crust or graham cracker and fruit sauce toping.'
    }
    description = items[dish]
    return HttpResponse(f"<h2> {dish} </h2>" + description)

def drinks(request, drink_name):
    drinks = {
        'mocha': 'type of coffee',
        'tea': 'type of beverage',
        'lemonade': 'type of refreshment'
    }
    choice_of_drink = drinks[drink_name]
    return HttpResponse(f"<h2>{drink_name}</h2>" + choice_of_drink)

def display_menu_item(request, menu_id):

    return HttpResponse(f"This is number {menu_id} menu")

def login(request):
    return render(request, "login.html")

''' learning Http Error handling in Django
def my_view(request):
    #...
    if condition == True:
        return HttpResponseNotFound('<h1>Page not found</h1>')
        #return HttpResponse('<h1>Page not found</h1>', status_code='404')
    else: 
        return HttpResponse('<h1>Page was found</h1>')

def detail (request, id):
    try:
        p = Product.objects.get(pk=id)
        field = model._meta.get_field(field_name)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")
    except FieldDoesNotExist:
        return HttpResponse('Field does not exist')
    return HttpResponse(Product Found")

def myview(request):
    if not request.user.has_perm('myapp.view_mymodel'):
        raise PermissionDenied()
    return HttpResponse()

def myview(request):
    if request.metho == 'POST'
        form = MyForm(request.POST)
        if form.is_valid():
            #process the form data
        else:
            return HttpRespose('Form submitted with invalid data')

'''