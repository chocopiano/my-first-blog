from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render

class Persona(object):
    def __init__(self,nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido
def saludo(request): #primera vista
    p1=Persona("Felie","Amigo")
    nombre='Juan'
    apellido="Díaz"
    temas_curso=["plantillas", "modelos"]
    ahora=datetime.datetime.now()
    #doc_externo=open("/Users/benjamindelpiano/Desktop/Proyectodjango/proyecto1/proyecto1/plantillas/wene.html")
    #plt=Template(doc_externo.read())
    #doc_externo.close()
    #doc_externo=loader.get_template("wene.html")
    ctx=Context({"nombre_persona":p1,"momento_actual":ahora,"temas":temas_curso})
    #documento=doc_externo.render({"nombre_persona":p1,"momento_actual":ahora,"temas":temas_curso})
    return render(request,"wene.html",{"nombre_persona":p1,"momento_actual":ahora,"temas":temas_curso})

def cursoc(request):
    fecha_actual = datetime.datetime.now()
    return render(request,"Cursoc.html",{"damefecha":fecha_actual})

def cursocss(request):
    fecha_actual = datetime.datetime.now()
    return render(request,"cursoCSS.html",{"damefecha":fecha_actual})

def despedida(request):
    return HttpResponse("chao")

def damefecha(request):
    fecha_actual=datetime.datetime.now()
    documento="""<html>
    <body
    <h1>
    Fecha y hora actual %s
    <h1/>
    <body/>
    <html/>""" % fecha_actual
    return HttpResponse(documento)

def calculaedad(request,edad, agno):
    periodo=agno-2019
    edadfutura=edad+periodo
    documento="<html><body><h2>En el año %s tendrás %s años<h2/><body><html/>" %(agno, edadfutura)
    return HttpResponse(documento)