from django.http import HttpResponse

def homepage(request):
    return HttpResponse("<h1>I love coffee!</h1>")