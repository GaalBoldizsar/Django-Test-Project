from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>This Is the Music Homepage</h1>")
