
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render

from backend_app.dominio.clases.persona import Persona

class a:



    def __init__(self):
        self.nombre = "hola"

def inicio(request):
    print (request)
    return render(request,"index.html")

def index(request):
    # return HttpResponse(a())
    return HttpResponse("hola mundo")
def error(request):
    # return HttpResponse(a())
    return HttpResponse("error")

def cierre(response):
    texto = """
  
  <!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css"
        integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
        integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo"
        crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.14.7/dist/umd/popper.min.js"
        integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1"
        crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/js/bootstrap.min.js"
        integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM"
        crossorigin="anonymous"></script>
</head>

<body>
    <div class="container">
        <div class="row">


           <h1  style="text-align: center;">Hola Mundo </h1>
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Consequuntur libero, soluta eum animi pariatur
                distinctio ipsam, officiis accusamus cumque nobis, facere laboriosam nihil doloremque maxime consectetur
                similique accusantium amet inventore.</p>

   <h1> La hora es:"""+ datetime.now().__str__()+"""


       <h1>
        </div>
    </div>
</body>

</html>
    """
    return HttpResponse(texto)

def formulario(req):
    return render(req,"formulario.html")
def respuesta(req):
    nombre = req.GET["txtnombre"]
    direccion= req.GET["txtdireccion"]
    p = Persona(nombre,direccion)
    return render(req,'respuesta.html',{'p':p})
