from django.http import HttpResponse, HttpResponseNotFound

def handler404(request, exception):
    return HttpResponse("404: Page not Found! <br><br> <button onclick='' href='';''> Go to Homepage")

def home(request):
    return HttpResponseNotFound("404: Page not Found!")
