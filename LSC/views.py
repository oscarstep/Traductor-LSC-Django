import json, requests
from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render
from panelControl.models import Institucion, Contacto, Equipo
from django.http import JsonResponse
#from LSC.kerasmodel import prediction

url = 'http://127.0.0.1:5000/'

def ayuda(request):
    #Con contexto 
    #doc_externo=open("C:/Users/edwar/oneDrive/Escritorio/2020 AUNAR/Proyecto/Proyectos Django/LSC/LSC/Plantillas/ayuda.html")
    #plt=Template(doc_externo.read())
    #doc_externo.close()
    #ayuda=plt.render(ctx)
    #ctx=Context()

    # Para loader 
    #doc_externo=loader.get_template('ayuda.html')
    #ayuda=doc_externo.render()

    #Return normal para ambos
    #return HttpResponse(ayuda)


    #Con Render
   
    Contacto1 = Contacto.objects.get(idContacto=1)
    Contaco2 = Contacto.objects.get(idContacto=2)
    Direccion = Institucion.objects.get(idInstitucion=1)
    Pais1 = Contacto.objects.get(idContacto=1)
    Ciudad1 = Contacto.objects.get(idContacto=1)
    dic = {'Descripcion1':Contacto1.Descripcion_Ayuda, 'Descripcion2':Contaco2.Descripcion_Ayuda, 'Direccion':Direccion.direccion}
    
    return render(request, "ayuda.html", dic)

def prueba(request):
    print("entreeee a prueba")
    if request.method == "POST":
        array_data = request.POST['data_url']
        data_img = json.loads(array_data)
        print("OK")
        response = requests.post(url, data=array_data)
        #pred_lsc = prediction(data)
        #print(pred_lsc)
        prediction = json.loads(response.content)
        prediction['letra'] = prediction['letra']['name']
        print(prediction)
        prediction.update({"result":True})
    return JsonResponse(prediction)

def nosotros(request):
    Direccion = Institucion.objects.get(idInstitucion=1)
    Nos = Contacto.objects.get(idContacto=1)
    Per = Equipo.objects.all()
    dic = {'Direccion':Direccion.direccion, 'Nosotros':Nos.Descripcion_Nosotros, 'int':Per}
    return render(request, "Nosotros.html", dic)

def Home_LSC(request):
    Direccion = Institucion.objects.get(idInstitucion=1)
    dic = {'Direccion':Direccion.direccion}
    return render(request, "Home_LSC.html", dic)
