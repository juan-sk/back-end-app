from django.http import HttpResponse

class a:
    def __init__(self):
        self.nombre = "hola"
def index(request):
    # return HttpResponse(a())
    return HttpResponse("hola mundo")
def error(request):
    # return HttpResponse(a())
    return HttpResponse("error")
